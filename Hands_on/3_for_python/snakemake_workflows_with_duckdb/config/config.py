## File name to use in search: config.py ##

# ===========
## Author details ##
# ===========

# Script's author:      Aliakbar Akbaritabar
# Version:              2025-06-06
# Email:                akbaritabar@demogr.mpg.de
# GitHub:               https://github.com/akbaritabar
# Website:              https://www.demogr.mpg.de/en/about_us_6113/staff_directory_1899/aliakbar_akbaritabar_4098/

# Script for replication of analysis of session on "Other" CSS skills as part of the course on "Introduction to Computational Social Science" at the University of Rostock, Germany.

# ===========
## Imports ##
# ===========
# shortcut for path join function
from os.path import join as ojn
from os import getcwd

# ===========
## Folders ##
# ===========

# TODO NOTE modify this according to the project folder
PROJECT_DIR = getcwd()

# An if condition to define if scratch drive should be used (during development) or the manuscript's folder (once finalized) to include figures in text
# TODO NOTE modify this according to the intended results/figures folder
SCRATCH_DRIVE = [False, True][1]

if SCRATCH_DRIVE:
    OUTPUTS_DIR = ojn(PROJECT_DIR, 'results')
else:
    # MANUSCRIPT FIGURES DIR
    MANUSCRIPT_DIR = ojn('manuscript', 'outputs')
    OUTPUTS_DIR = ojn(MANUSCRIPT_DIR, 'results')

INPUTS_DIR = ojn(PROJECT_DIR, 'resources')
LOGS_DIR = ojn(PROJECT_DIR, 'logs')
VIS_DIR = ojn(OUTPUTS_DIR, 'figures')
TABS_DIR = ojn(OUTPUTS_DIR, 'tables')
SCRIPTS_DIR = ojn(PROJECT_DIR, 'workflow', 'scripts')

# ===========
## Raw data ##
# ===========

TOY_DATA = ojn(INPUTS_DIR, 'bipartite_author_paper_edges.csv')

# ===========
## Parameters ##
# ===========

# here you can define parameters for the workflow to have multiple iterations using different combinations of parameters.

# ===========
## Scripts to use ##
# ===========

SRC1 = ojn(SCRIPTS_DIR, 'prepare_parquet_of_toy_data.py')
SRC2 = ojn(SCRIPTS_DIR, 'summary_papers_authors_yearly.py')
SRC3 = ojn(SCRIPTS_DIR, 'summary_author_papers.py')
SRC4 = ojn(SCRIPTS_DIR, 'summary_author_papers_yearly.py')

# ===========
## Processed data ##
# ===========

# Convert toy data to parquet
TOY_DATA_PARQUET = ojn(OUTPUTS_DIR, 'toy_data.parquet')
# log for it
TOY_DATA_PARQUET_LOG = ojn(LOGS_DIR, 'lg_create_parquet_data.log')


# Summary of number of papers and authors per year
SUM_PAPERS_AUTHORS_YEARLY = ojn(OUTPUTS_DIR, 'papers_author_yearly_summary.parquet')
# log for it
SUM_PAPERS_AUTHORS_YEARLY_LOG = ojn(LOGS_DIR, 'lg_papers_author_yearly_sum.log')


# Summary of number of papers per unique author
SUM_AUTHOR_PAPERS = ojn(OUTPUTS_DIR, 'author_papers_summary.parquet')
# log for it
SUM_AUTHOR_PAPERS_LOG = ojn(LOGS_DIR, 'lg_author_papers_sum.log')


# Summary of number of papers per unique author, per year
SUM_AUTHOR_PAPERS_YEARLY = ojn(OUTPUTS_DIR, 'author_papers_yearly_summary.parquet')
# log for it
SUM_AUTHOR_PAPERS_YEARLY_LOG = ojn(LOGS_DIR, 'lg_author_papers_yearly_sum.log')

# ===========
## Figures ##
# ===========

# here could be figures exported for the paper, etc. that go in "VIS_DIR"

# ===========
## Table of results ##
# ===========

# here could be tables exported for the paper, etc. that go in "TABS_DIR"
