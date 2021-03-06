import argparse
import csv
import gzip
import os

from top_stores.aggregations import TopProductsAggregator, TopStoresAggregator


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
    top_products_aggregator = TopProductsAggregator()

    # Ingest transactions

    with gzip.open('randomized-transactions-202009.psv.gz', 'rt') as file:
        reader = csv.DictReader(file, delimiter='|')

        for transaction in reader:
            top_stores_aggregator.ingest(transaction)
            top_products_aggregator.ingest(transaction)

    # Write top stores

    with open(os.path.join(args.out, 'top-50-stores.csv'), 'w') as f:
        fieldnames = ['code_magasin', 'ca']
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')
        writer.writeheader()
        for row in top_stores_aggregator.get_top_stores(n=50):
            writer.writerow(row)

    # Write top products

    top_products_folder = os.path.join(args.out, 'top-products-by-store')
    os.mkdir(top_products_folder)

    top_products = top_products_aggregator.get_top_products_by_store(n=100).items()

    for store_id, top_products_rows in top_products:
        top_products_file = os.path.join(top_products_folder,
                                         f'top-100-products-store-{store_id}.csv')

        with open(top_products_file, 'w') as f:
            fieldnames = ['code_magasin', 'identifiant_produit', 'ca']
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter='|')
            writer.writeheader()
            for row in top_products_rows:
                writer.writerow(row)


if __name__ == '__main__':
    main()
