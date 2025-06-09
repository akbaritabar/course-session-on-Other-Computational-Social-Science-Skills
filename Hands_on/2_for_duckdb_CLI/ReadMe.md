# Using DuckDB Command Line Interface (CLI) on any platform

After installing it using the instructions in the ReadMe file in Hands-on folder, open the DuckDB CLI (or shell), by double clicking on its icon on Windows, or opening a terminal in Windows/Linux/Mac, changing the directory to where it is downloaded, and either entering its name `duckdb.exe` (Windows), or `sh duckdb` (Linux/Mac), then follow the guidelines below (read the comments starting with `--` for more context on commands).

# Example use case

To see the help and list of available commands to start, enter `.help` and press enter.

```sql
-- for a list of commands
.help
-- as of today, June 6, 2025, and for the version "v1.2.2 7c039464e4" on Windows, it returns:

-- .bail on|off             Stop after hitting an error.  Default OFF
-- .binary on|off           Turn binary output on or off.  Default OFF
-- .cd DIRECTORY            Change the working directory to DIRECTORY
-- .changes on|off          Show number of rows changed by SQL
-- .check GLOB              Fail if output since .testcase does not match
-- .columns                 Column-wise rendering of query results
-- .databases               List names and files of attached databases
-- .decimal_sep SEP         Sets the decimal separator used when rendering numbers. Only for duckbox mode.
-- .dump ?TABLE?            Render database content as SQL
-- .echo on|off             Turn command echo on or off
-- .excel                   Display the output of next command in spreadsheet
-- .exit ?CODE?             Exit this program with return-code CODE
-- .explain ?on|off|auto?   Change the EXPLAIN formatting mode.  Default: auto
-- .fullschema ?--indent?   Show schema and the content of sqlite_stat tables
-- .headers on|off          Turn display of headers on or off
-- .help ?-all? ?PATTERN?   Show help text for PATTERN
-- .highlight_colors [element] [color]  ([bold])? Configure highlighting colors
-- .highlight_errors [on|off] Toggle highlighting of errors in the shell on/off
-- .highlight_results [on|off] Toggle highlighting of results in the shell on/off
-- .import FILE TABLE       Import data from FILE into TABLE
-- .indexes ?TABLE?         Show names of indexes
-- .large_number_rendering all|footer|off Toggle readable rendering of large numbers (duckbox only)
-- .log FILE|off            Turn logging on or off.  FILE can be stderr/stdout
-- .maxrows COUNT           Sets the maximum number of rows for display (default: 40). Only for duckbox mode.
-- .maxwidth COUNT          Sets the maximum width in characters. 0 defaults to terminal width. Only for duckbox mode.
-- .mode MODE ?TABLE?       Set output mode
-- .nullvalue STRING        Use STRING in place of NULL values
-- .once ?OPTIONS? ?FILE?   Output for the next SQL command only to FILE
-- .open ?OPTIONS? ?FILE?   Close existing database and reopen FILE
-- .output ?FILE?           Send output to FILE or stdout if FILE is omitted
-- .print STRING...         Print literal STRING
-- .prompt MAIN CONTINUE    Replace the standard prompts
-- .quit                    Exit this program
-- .read FILE               Read input from FILE
-- .rows                    Row-wise rendering of query results (default)
-- .safe_mode               Enable safe-mode
-- .schema ?PATTERN?        Show the CREATE statements matching PATTERN
-- .separator COL ?ROW?     Change the column and row separators
-- .shell CMD ARGS...       Run CMD ARGS... in a system shell
-- .show                    Show the current values for various settings
-- .system CMD ARGS...      Run CMD ARGS... in a system shell
-- .tables ?TABLE?          List names of tables matching LIKE pattern TABLE
-- .testcase NAME           Begin redirecting output to 'testcase-out.txt'
-- .thousand_sep SEP        Sets the thousand separator used when rendering numbers. Only for duckbox mode.
-- .timer on|off            Turn SQL timer on or off
-- .width NUM1 NUM2 ...     Set minimum column widths for columnar output
-- .utf8                    Enable experimental UTF-8 console output mode

```

Here we start with the example.

```sql
-- to change directory and go where your data/project is
-- remember on Windows, you have to skip slash i.e., 'folder1\\folder2
.cd 'PATH-TO-FOLDER'

-- if you want to run a shell command e.g., to check if the folder is right, or what are the files here
.shell dir
-- on linux/mac
.shell ls

-- to read the first 5 rows of csv file
select * from 'bipartite_author_paper_edges.csv'
limit 5;

-- ┌─────────────┬────────────┬─────────┬───────┐
-- │   source    │   target   │ row_num │ year  │
-- │   varchar   │  varchar   │  int64  │ int64 │
-- ├─────────────┼────────────┼─────────┼───────┤
-- │ author_1717 │ paper_1121 │       6 │  2000 │
-- │ author_7315 │ paper_1121 │       7 │  2000 │
-- │ author_1714 │ paper_1121 │       8 │  2000 │
-- │ author_1716 │ paper_1121 │       9 │  2000 │
-- │ author_1715 │ paper_1121 │      11 │  2000 │
-- └─────────────┴────────────┴─────────┴───────┘

-- to do a group by year and count the number of papers, authors
select year, count(distinct source) as n_author, count(distinct target) as n_paper
from 'bipartite_author_paper_edges.csv'
group by year
;

-- ┌───────┬──────────┬─────────┐
-- │ year  │ n_author │ n_paper │
-- │ int64 │  int64   │  int64  │
-- ├───────┼──────────┼─────────┤
-- │  2002 │        7 │       2 │
-- │  2005 │        9 │       2 │
-- │  2001 │        5 │       1 │
-- │  2003 │        6 │       1 │
-- │  2006 │        7 │       1 │
-- │  2000 │        5 │       1 │
-- │  2004 │        5 │       1 │
-- └───────┴──────────┴─────────┘


-- to convert the csv file into parquet format
copy (
    select * from 'bipartite_author_paper_edges.csv'
)
to 'bipartite_author_paper_edges.parquet' (format parquet)
;

-- to read the first 5 rows of the parquet file
select * from 'bipartite_author_paper_edges.parquet'
limit 5;

-- ┌─────────────┬────────────┬─────────┬───────┐
-- │   source    │   target   │ row_num │ year  │
-- │   varchar   │  varchar   │  int64  │ int64 │
-- ├─────────────┼────────────┼─────────┼───────┤
-- │ author_1717 │ paper_1121 │       6 │  2000 │
-- │ author_7315 │ paper_1121 │       7 │  2000 │
-- │ author_1714 │ paper_1121 │       8 │  2000 │
-- │ author_1716 │ paper_1121 │       9 │  2000 │
-- │ author_1715 │ paper_1121 │      11 │  2000 │
-- └─────────────┴────────────┴─────────┴───────┘

-- to do a group by year and count the number of papers, authors
select year, count(distinct source) as n_author, count(distinct target) as n_paper
from 'bipartite_author_paper_edges.parquet'
group by year
;

-- ┌───────┬──────────┬─────────┐
-- │ year  │ n_author │ n_paper │
-- │ int64 │  int64   │  int64  │
-- ├───────┼──────────┼─────────┤
-- │  2002 │        7 │       2 │
-- │  2005 │        9 │       2 │
-- │  2001 │        5 │       1 │
-- │  2003 │        6 │       1 │
-- │  2006 │        7 │       1 │
-- │  2000 │        5 │       1 │
-- │  2004 │        5 │       1 │
-- └───────┴──────────┴─────────┘

-- If you have a SQL script with a long query
-- note that folder paths for data should be absolute or you include the script where you went with ".cd"
.read '../for_duckdb_CLI/example_script.SQL'

-- ┌───────┬──────────┬─────────┐
-- │ year  │ n_author │ n_paper │
-- │ int64 │  int64   │  int64  │
-- ├───────┼──────────┼─────────┤
-- │  2000 │        5 │       1 │
-- │  2001 │        5 │       1 │
-- │  2002 │        7 │       2 │
-- │  2005 │        9 │       2 │
-- │  2004 │        5 │       1 │
-- │  2006 │        7 │       1 │
-- │  2003 │        6 │       1 │
-- └───────┴──────────┴─────────┘

```

If you are thinking that my toy example data is too small to show the speed, I challenge you to use the above commands with a "larger than RAM/memory dataset" and see DuckDB's magic at work. 

Below I share a link and instructions on how to use New York taxi data for a test.

# An example with larger dataset to test on laptop

Go to this link and download New York taxi data from Kaggle (there are more updated versions that you can find online) `https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data?resource=download`. The downloaded file as of June 6, 2025, named `yellow_tripdata_2015-01.csv` is **1.84GB** with 12,748,986 rows. I made 7 copies of the same file in my hard disk so in total I have **14.7GB** of data with 101,991,888 rows (for 8 files).

**Specifications**: My laptop has 31.5GB or RAM and Windows task manager shows 12 cores running Window 11 pro.

```SQL
-- to time queries, I turn Duckdb's timer on (passing "off" will turn it off)
.timer on

-- if you want to go pro, this allows more profiling details: `PRAGMA enable_profiling` wait, what is that "pragma"? They are special commands, search on DuckDB documentation for a list.

-- code to count the number of rows and unique vendors for 1 CSV file of 1.84GB
select count(*) as n, count(distinct VendorID) from 'yellow_tripdata_2015-01.csv';

-- 100% ?████████████████████████████████████████████████████████████?
-- ┌──────────┬──────────────────────────┐
-- │    n     │ count(DISTINCT VendorID) │
-- │  int64   │          int64           │
-- ├──────────┼──────────────────────────┤
-- │ 12748986 │            2             │
-- └──────────┴──────────────────────────┘
-- Run Time (s): real 3.246 user 19.265625 sys 2.046875


-- Now let's try with all 8 files, the only change I need to make is to use a wild card "*" in the csv file instead of one file's full name

-- how many rows will we have? hmm, can we do math in DuckDB console?

select 12748986 * 8;

-- ┌──────────────────┐
-- │  (12748986 * 8)  │
-- │      int32       │
-- ├──────────────────┤
-- │    101991888     │
-- │ (101.99 million) │
-- └──────────────────┘

-- now the query with wild card file name
select count(*) as n, count(distinct VendorID) from 'yellow*.csv';

-- 100% ?████████████████████████████████████████████████████████████?
-- ┌───────────┬──────────────────────────┐
-- │     n     │ count(DISTINCT VendorID) │
-- │   int64   │          int64           │
-- ├───────────┼──────────────────────────┤
-- │ 101991888 │            2             │
-- └───────────┴──────────────────────────┘
-- Run Time (s): real 23.850 user 148.718750 sys 13.375000


-- at the end to leave DuckDB terminal/CLI
.quit


```


# Where to find more?

See more guidelines on DuckDB SQL dialect here: [https://duckdb.org/docs/stable/sql/introduction](https://duckdb.org/docs/stable/sql/introduction)

## Book

See this book for a wealth of examples.

```
Needham, M., Hunger, M., & Simons, M. (2024). Duckdb in Action. Manning Publications.

```

## Videos from

Or these videos by one of the book's authors:

[https://www.youtube.com/@learndatawithmark](https://www.youtube.com/@learndatawithmark)
