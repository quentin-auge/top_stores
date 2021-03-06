import argparse
import csv
import gzip
import os

from top_stores.aggregations import TopStoresAggregator


def main():
    # Arguments parsing

    parser = argparse.ArgumentParser(description='Aggregate top stores')
    parser.add_argument('transactions_file',
                        help='input file containing transactions (gzipped pipe separated file)')
    parser.add_argument('--out', '-o', required=True,
                        help='output folder (will be created, shall not exist)')
    args = parser.parse_args()

    # Create output folder (crash if already existing)

    os.mkdir(args.out)

    # Create aggregators

    top_stores_aggregator = TopStoresAggregator()

    # Ingest transactions

    with gzip.open('randomized-transactions-202009.psv.gz', 'rt') as file:
        reader = csv.DictReader(file, delimiter='|')

        i = 0
        for transaction in reader:
            top_stores_aggregator.ingest(transaction)
            if i > 10000:
              break
            i += 1

    # Write top stores

    with open(os.path.join(args.out, 'top-50-stores.csv'), 'w') as f:
        fieldnames = ['code_magasin', 'ca']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in top_stores_aggregator.get_top_stores():
            writer.writerow(row)


if __name__ == '__main__':
    main()
