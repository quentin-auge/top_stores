import argparse
import os


def main():
  # Arguments parsing

  parser = argparse.ArgumentParser(description='Aggregate top stores')
  parser.add_argument('transactions_file', help='input file containing transactions')
  parser.add_argument('--out', '-o', required=True,
                      help='output folder (will be created, shall not exist)')
  args = parser.parse_args()

  # Create output folder

  os.mkdir(args.out)

if __name__ == '__main__':
  main()
