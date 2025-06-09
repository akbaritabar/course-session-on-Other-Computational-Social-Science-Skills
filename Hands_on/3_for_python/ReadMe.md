# Folder structure and examples included for Python

Here there are two examples, one using Dask, and the other using DuckDB inside a SnakeMake workflow:

- Subfolder `dask` includes an example of parallelization using dask library in Python. It uses the 500 example XML files provided in the data folder in root directory of hands-on part.
- Subfolder `snakemake_workflows_with_duckdb` 
- File `requirements` is a list of Python libraries that you need to install to run the scripts for these examples. See the ReadMe in root directory of hands-on part for instructions on how to use it to set up Python.

# To install the DuckDB and use it inside Python

If you build your vanilla python environment using the `requirements.txt` that I provide in this directory, `pip` is going to install duckdb and you can simply do:

```python

import duckdb as dd

# for a list of available methods
dir(dd)

``` 

If you want to install it yourself without creating the whole environment, open a terminal shell, and do:

```shell

python -m pip install duckdb --upgrade

```

