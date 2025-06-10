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

# Bonus content: Scaled up example on 16GB RAM laptop

Now let's use the NY taxi data in R and see the speed up using my work laptop that has 16GB or RAM and 5 CPU cores.

```R
library(tidyverse)

df_NY <- tbl(con, "read_csv('./NYtaxi/yellow*.csv')")

df_NY

# # Source:   SQL [?? x 19]
# # Database: DuckDB v1.3.0 [Akbaritabar@Windows 10 x64:R 4.4.3/:memory:]
#    VendorID tpep_pickup_datetime tpep_dropoff_datetime passenger_count
#       <dbl> <dttm>               <dttm>                          <dbl>
#  1        2 2015-01-15 19:05:39  2015-01-15 19:23:42                 1
#  2        1 2015-01-10 20:33:38  2015-01-10 20:53:28                 1
#  3        1 2015-01-10 20:33:38  2015-01-10 20:43:41                 1
#  4        1 2015-01-10 20:33:39  2015-01-10 20:35:31                 1
#  5        1 2015-01-10 20:33:39  2015-01-10 20:52:58                 1
#  6        1 2015-01-10 20:33:39  2015-01-10 20:53:52                 1
#  7        1 2015-01-10 20:33:39  2015-01-10 20:58:31                 1
#  8        1 2015-01-10 20:33:39  2015-01-10 20:42:20                 3
#  9        1 2015-01-10 20:33:39  2015-01-10 21:11:35                 3
# 10        1 2015-01-10 20:33:40  2015-01-10 20:40:44                 2
# # ℹ more rows
# # ℹ 15 more variables: trip_distance <dbl>, pickup_longitude <dbl>,
# #   pickup_latitude <dbl>, RateCodeID <dbl>, store_and_fwd_flag <chr>,
# #   dropoff_longitude <dbl>, dropoff_latitude <dbl>, payment_type <dbl>,
# #   fare_amount <dbl>, extra <dbl>, mta_tax <dbl>, tip_amount <dbl>,
# #   tolls_amount <dbl>, improvement_surcharge <dbl>, total_amount <dbl>
# # ℹ Use `print(n = ...)` to see more rows


# Let's run the same query we did in DuckDB CLI, now in R

# one csv file
dbGetQuery(con, "select count(*) as n, count(distinct VendorID) from './NYtaxi/yellow_tripdata_2015-01.csv';")

# all 8 files
dbGetQuery(con, "select count(*) as n, count(distinct VendorID) from './NYtaxi/yellow*.csv';")

# filter data and count rows
df_NY %>% 
  filter(tpep_pickup_datetime == '2015-01-15 19:05:39') %>% 
  summarize(n_rows = n())


# how to collect a subset of the data?
sm_dt <- df_NY %>% 
  filter(tpep_pickup_datetime == '2015-01-15 19:05:39') %>% 
  summarize(n_rows = n()) %>% 
  collect()

class(sm_dt)
# [1] "tbl_df"     "tbl"        "data.frame"

> typeof(sm_dt)
# [1] "list"

```