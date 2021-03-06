# Top stores aggregation

This take home project is about aggregating a file containing 160M monthly purchases in 3651 stores into:
 * A list of the 50 stores with the largest revenue
 * A list of the 100 most popular products for each store

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
$ time top-stores -o out/ randomized-transactions-202009.psv.gz

real	17m49.060s
user	16m47.599s
sys	0m5.732s
```

Results:

```
$ wc -l out/top-50 stores.csv
51

$ head out/top-50-stores.csv
code_magasin|ca
13800|7286310.21
13314|4954346.51
20001|4837372.02
74339|4704957.65
06829|4669147.82
06312|4652404.54
42830|4633373.37
38336|4607381.01
33848|4396928.37

$ wc -l out/top-products-by-store/top-100-products-store-*.csv | head
101 out/top-products-by-store/top-100-products-store-0021.csv
101 out/top-products-by-store/top-100-products-store-0022.csv
101 out/top-products-by-store/top-100-products-store-0026.csv
101 out/top-products-by-store/top-100-products-store-0027.csv
101 out/top-products-by-store/top-100-products-store-0030.csv
101 out/top-products-by-store/top-100-products-store-0033.csv
101 out/top-products-by-store/top-100-products-store-0034.csv
101 out/top-products-by-store/top-100-products-store-0035.csv
101 out/top-products-by-store/top-100-products-store-0036.csv
101 out/top-products-by-store/top-100-products-store-0037.csv

$ head out/top-products-by-store/top-100-products-store-0021.csv
code_magasin|identifiant_produit|ca
0021|951CF7DC78|7804.83
0021||7128.14
0021|525B4556D1|2826.27
0021|B580E681DE|3926.79
0021|81D966D6EC|3373.19
0021|AED8DA0F93|4013.50
0021|25561B13AA|5399.38
0021|0129F49447|2894.03
0021|3D367B92F0|3576.07
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
top_stores/aggregations.py      31      0      8      0   100%
-----------------------------------------------------------------------------------------------
TOTAL                           31      0      8      0   100%


====================================== 1 passed in 0.08s ======================================
____________________________________________ summary __________________________________________
  py3: commands succeeded
  congratulations :)
```
