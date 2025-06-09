## File name to use in search: summary_author_papers.py ##

# Python script that use DuckDB and SQL script for data processing/reshaping

# for data handling
import duckdb
import pandas as pd

#### Results log and progress report ####
from tolog import lg

# to see more pandas columns & not to use scientific notation
pd.set_option('max_colwidth',100)
pd.set_option('display.float_format', '{:.2f}'.format)


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
select source, count(distinct target) as n_paper_per_author
from '{args.input[0]}'
group by source
)
to '{args.output[0]}' (format parquet)
;
"""

duckdb.sql(q_2use)

# status report in log
lg('DuckDB ran the query and successfully finished!')
lg(f"Parquet file created at: {args.output[0]}")
