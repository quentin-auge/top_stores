# Top stores aggregation

This take home project is about aggregating a file containing 160M monthly purchases in 3651 stores into:
 * A list of the 50 stores with the largest revenue
 * A list of the 10 products bought the largest number of times for each store

The code runs with Python >= 3.6. It is a locally pip-installable pure python package relying
exclusively on standard library (no dependency), exposing a `top-stores` command line tool.
It is tested using `tox` and `pytest`.

## Setup

* Clone this repository

* Move into project directory
  ```
  cd top_stores/
  ```

* Create a virtual environment and activate it:
  ```
  virtualenv -p python3 .venv
  source .venv/bin/activate
  ```

* Install the application inside the virtualenv
  ```
  pip install .
  ```

It exposes a `top-stores` command line tool.

## Run the application

Usage:

```
$ top-stores --help

usage: top-stores [-h] --output OUTPUT transactions_file

Aggregate top stores

positional arguments:
  transactions_file     input file containing transactions

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        output folder (will be created, shall not exist)
```

Aggregate file `randomized-transactions-202009.psv.gz`:

```
$ top-stores -o out/ randomized-transactions-202009.psv.gz
```

## Run the tests

Install `tox` and run it:

```
pip install tox
tox
```

Tox outputs the coverage at the end.

Sample run:

```
$ tox
```
