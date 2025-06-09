-- to do a group by year and count the number of papers, authors
select year, count(distinct source) as n_author, count(distinct target) as n_paper
from '../data/bipartite_author_paper_edges.parquet'
group by year
;