# Top stores aggregation

This take home project is about aggregating a file containing 160M monthly purchases in 3651 stores into:
 * A list of the 50 stores with the largest revenue
 * A list of the 10 products bought the largest number of times for each store

The code runs with Python >= 3.6. It is a locally pip-installable pure python package relying
exclusively on standard library (no dependency), exposing a `top-stores` command line tool.
It is tested using `tox` and `pytest` with 100% coverage (excluding the main).

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

usage: top-stores [-h] --out OUT transactions_file

Aggregate top stores

positional arguments:
  transactions_file  input file containing transactions (gzipped pipe
                     separated file)

optional arguments:
  -h, --help         show this help message and exit
  --out OUT, -o OUT  output folder (will be created, shall not exist)
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

Tox outputs the coverage at the end (100%).

Sample run:

```
$ tox

GLOB sdist-make: setup.py
py3 recreate: .tox/py3
py3 installdeps: .
py3 inst: .tox/.tmp/package/1/top-stores-0.1.zip
py3 run-test: commands[0] | pytest --cov top_stores
======================== test session starts ========================
platform linux -- Python 3.6.9, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
cachedir: .tox/py3/.pytest_cache
rootdir: .
plugins: cov-2.11.1
collected 1 item

test_aggregations.py .                                                                                                                                                                                                                [100%]

----------- coverage: platform linux, python 3.6.9 -----------
Name                           Stmts   Miss Branch BrPart  Cover
-----------------------------------------------------------------------------------------------
top_stores/aggregations.py      14      0      2      0   100%
-----------------------------------------------------------------------------------------------
TOTAL                           14      0      2      0   100%


====================================== 1 passed in 0.08s ======================================
____________________________________________ summary __________________________________________
  py3: commands succeeded
  congratulations :)
```
