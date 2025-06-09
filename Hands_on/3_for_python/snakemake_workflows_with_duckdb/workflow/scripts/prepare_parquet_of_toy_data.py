## File name to use in search: prepare_parquet_of_toy_data.py ##

# Python script that use DuckDB and SQL script for data processing/reshaping

# for data handling
import duckdb

#### Results log and progress report ####
from tolog import lg


lg(f"These items are in the environment: {dir()}")

# ============================
#### For command line arguments ####
# ============================
import argparse
parser = argparse.ArgumentParser()

# System arguments
# use ", nargs='+'" if more than one input is given, below have to choose args.input[] and list element number to use
parser.add_argument("-i", "--input", help = "Input file to use",
                    type = str, required = True, nargs='+')
parser.add_argument("-o", "--output", help = "Output data path",
                    type = str, required = False, nargs='+')

args = parser.parse_args()

lg(f"Arguments received from command line: \n {args}")

# ============================
#### Run DuckDB SQL script ####
# ============================

q_2use = f"""
copy (
    select * from '{args.input[0]}'
)
to '{args.output[0]}' (format parquet)
;
"""

duckdb.sql(q_2use)

# status report in log
lg('DuckDB ran the query and successfully finished!')
lg(f"Parquet file created at: {args.output[0]}")
