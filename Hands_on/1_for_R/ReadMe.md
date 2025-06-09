# To install the DuckDB and use it inside R

```R

install.packages("duckdb")

```

Note from DuckDB website (as of June 6, 2025):

```
On certain platforms, such as Linux AArch64 (arm64), the DuckDB R package needs to be compiled from source. To speed up this process, follow the instructions on the R build page (https://duckdb.org/docs/stable/dev/building/r).

```

# Where to find more examples?

See here [https://duckdb.org/docs/stable/clients/r](https://duckdb.org/docs/stable/clients/r)

```R
# copied from the link above
library("duckdb")
# to start an in-memory database
con <- dbConnect(duckdb())
# or
con <- dbConnect(duckdb(), dbdir = ":memory:")

```

Now you can run examples similar to the one in DuckDB command line interface (CLI), but inside R!

For instance, letting DuckDB read/write data and convert it to data.frame or similar formats for you will substantially speed up your I/O.

```R
setwd('PATH-TO-DATA/PROJECT')
# check current directory with
getwd()

# to do a group by year and count the number of papers, authors
dbGetQuery(con, "select year, count(distinct source) as n_author, count(distinct target) as n_paper from read_parquet('bipartite_author_paper_edges.parquet') group by year;")
#   year n_author n_paper
# 1 2002        7       2
# 2 2000        5       1
# 3 2004        5       1
# 4 2001        5       1
# 5 2005        9       2
# 6 2006        7       1
# 7 2003        6       1

```

Or if you want to only benefit from DuckDB's speed in Input/Output (I/O), you can use Dplyr (part of Tidyverse library and packages) to create a connection to the file using DuckDB as follows which is similar to connecting to a SQL database using Dplyr and DBplyr, see more in [https://duckdb.org/docs/stable/clients/r](https://duckdb.org/docs/stable/clients/r)

```R
library(tidyverse)
# that will import dplyr, or instead
library(dplyr)

df <- tbl(con, "read_csv('bipartite_author_paper_edges.csv')")

df

# # Source:   SQL [?? x 4]
# # Database: DuckDB v1.3.0 [Aliakbar Akbaritabar@Windows 10 x64:R 4.5.0/:memory:]
#    source      target     row_num  year
#    <chr>       <chr>        <dbl> <dbl>
#  1 author_1717 paper_1121       6  2000
#  2 author_7315 paper_1121       7  2000
#  3 author_1714 paper_1121       8  2000
#  4 author_1716 paper_1121       9  2000
#  5 author_1715 paper_1121      11  2000
#  6 author_1891 paper_1260      23  2001
#  7 author_7323 paper_1260      24  2001
#  8 author_1890 paper_1260      25  2001
#  9 author_1892 paper_1260      26  2001
# 10 author_3889 paper_1260      44  2001
# # ℹ more rows
# # ℹ Use `print(n = ...)` to see more rows

```
