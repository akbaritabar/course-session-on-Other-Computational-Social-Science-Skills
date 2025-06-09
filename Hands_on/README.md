# Required software for Hands-on session that uses R, Python, and SQL in DuckDB
For the hands-on part of this week on "Other CSS skills" and for the example code, I used R, Python, and SQL (using DuckDB).

If you have not yet done that, follow the **instructions in week 3 (using digital trace data and web scrapping)** to install vanilla Python (instructions are copied also below). 

After installing Python using Pyenv, set the local Python for this project (using `pyenv local PYTHON-VERSION-NUMBER` see Week 3, or below, for details), then create a virtual environment (with this command `python -m virtualenv project-env-name` for Windows), and finally, install the requirements for this week's hands-on part using `python -m pip install -r requirements.txt`.


# Folder `data`
In the folder `data` I have left a few toy examples that are used in the R, and Python codes or SQL scripts. In the ReadMe file for DuckDB CLI, I have provided instructions on how to download a much larger dataset to test it on the laptop. I shared the timing of queries on my laptop.

# How to install DuckDB?
## To install the DuckDB command line interface (CLI)

Visit the link below. It has versions for Windows, Mac, and Linux. 

[https://duckdb.org/docs/installation/](https://duckdb.org/docs/installation/)

## To test it without installing

Visit the link below, however, **note** that the available memory (RAM) is about 4GB, and cores are only 1, which is the resources your web browser can use from the laptop/computer.

[https://shell.duckdb.org/](https://shell.duckdb.org/)

# How to install R and Python?

It is necessary to have these two software installed and check if they are functioning e.g., by importing a package or checking their installed versions.

In Python, we will use [virtual environments](https://realpython.com/python-virtual-environments-a-primer/) to isolate our projects and their required packages. This helps with reproducibility practices and making sure your code could be taken by someone else to re-run on their machine to recreate the results you have shown.

In R, if you are familiar with [Renv](https://rstudio.github.io/renv/index.html), feel free to use it to isolate your projects and R package requirements. The concepts are the same, but there are small differences in the details and syntax.

# Install R and RStudio

The IT should already have installed R and RStudio on the class' lab computers.

To install it on your own, please follow these links. If you are using R on Linux, I recommend using [R2U](https://github.com/eddelbuettel/r2u) to enable installing packages from binary instead of source that takes much less time.

- **For Windows**: [https://cran.r-project.org/bin/windows/base/](https://cran.r-project.org/bin/windows/base/)
- **For Mac**: [https://cran.r-project.org/bin/macosx/](https://cran.r-project.org/bin/macosx/)
- **For Linux**: [https://cran.r-project.org/](https://cran.r-project.org/) Click on the button for Linux, then select your distribution, i.e., "Ubuntu" and follow the steps outlined to add it to Linux sources list and install using `sudo apt-get`

And once you installed R, visit this link to download and install RStudio: [https://posit.co/download/rstudio-desktop/](https://posit.co/download/rstudio-desktop/)

# Pyenv for Windows
0. This is a good introduction to Pyenv: https://realpython.com/intro-to-pyenv/
1. Open `Powershell` in Windows (by opening the start menu and typing Powershell) and then put these and enter which asks Powershell to run scripts "only" for your user: `Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser`
2. Close and reopen Powershell. Follow the steps in this link for installation: https://github.com/pyenv-win/pyenv-win
3. Next, confirm that installation was successful with `pyenv --version`. Running `pyenv commands` lists available commands and what they do.
4. After the installation, it is now possible to write `pyenv install --list` to see which Python distributions are available to install e.g., it can also install miniforge and conda ones, similar to vanilla Python using `pyenv install PYTHON-VERSION-NUMBER` (or conda/miniforge name from the list). I suggest installing the latest Python 3 vanilla version i.e., "3.13" and later.
5. Next, change the **local** python from the system one to the one installed with pyenv to prevent messing up the system one i.e., activate it with `pyenv local PYTHON-VERSION-NUMBER` and check it with `pyenv versions` (star shows the Python in use)
6. Afterwards, `pyenv local PY-VERSION` allows setting it locally in a project folder which could be checked with `pyenv versions` and also `pyenv which python` or `pyenv which pip` and `python -m pip list`
7. You can then use `pip install virtualenv` for `virtualenv` to create virtual environments.
8. Check its correct installation with `python -m virtualenv --version` (which also prints where it is installed which should be under your newly installed vanilla Python)
9. Now `python -m pip list` should only show python, pip, and virtualenv, and a few things that are their requirements
10. For a project and its environment, select a name and create it with `python -m virtualenv project-env-name` which will create a subfolder with that name and install some base libraries and Python
11. After environment is created you can cd to the project directory with `cd project-env-name` and if you are using Windows Command Prompt do  `.\Scripts\activate.bat` which activates the environment. Instead, if you are using Windows Powershell terminal, you can do `.\Scripts\activate.ps1`. Now, if you do `python -m pip list` it should only list pip itself as the installed package and nothing else. This in addition to the name of virtual environment printed in parenthesis at the start of command line i.e., "(project-env-name)" means you have successfully created the environment and activated it.
12. Then copy the "requirements.txt" file into this project folder and do `python -m pip install -r requirements.txt` to use this environment and install the required packages.
13. **Please note**: On Windows, it can often happen that creating a new virtual environment in a subfolder lead to "file path name too long" error. The reason is your folder path should not exceed 256 characters (including spaces) and the solution is to create your project in another folder with shorter folder name(s).

# Pyenv for Linux and Mac: Use Pyenv with vanilla, or conda, miniforge, etc Python versions on Linux or Mac "without" affecting the system installation of python
1. This is a good introduction to Pyenv: https://realpython.com/intro-to-pyenv/
2. Follow installation steps from this link (available for Mac and Linux, for Windows refer to a different fork, discussed in the above section): https://github.com/pyenv/pyenv
3. After the step on adding it to .bashrc, .bash_profile, and .profile, if you had an issue with bash not seeing it right i.e., if `pyenv --version` was giving an error like `/usr/bin/env: ‘bash\r’: No such file or directory`. You have to remove pyenv (go to the folder where it is installed i.e., `~/.pyenv` or something similar, and delete that folder), then edit `git` configuration and set this from true to false i.e., `git config --global core.autocrlf false` and then reinstall pyenv and add it to bash as outlined above
4. Next, confirm that installation was successful with `pyenv --version`. Here are a list of pyenv commands: https://github.com/pyenv/pyenv/blob/master/COMMANDS.md
5. After the installation, it is now possible to write `pyenv install --list` to see which Python distributions are available to install e.g., it can also install miniforge and conda ones, similar to vanilla Python using `pyenv install PYTHON-VERSION-NUMBER` (or conda/miniforge name from the list). I suggest installing the latest Python 3 vanilla version i.e., "3.13" and later.
6. Next, change the **local** python from the system one to the one installed with pyenv to prevent messing up the system one i.e., activate it with `pyenv local PYTHON-VERSION-NUMBER` and check it with `pyenv versions` (star shows the Python in use)
7. **NOTE** do NOT use `pyenv global` for instance on Ubuntu as some apps rely on system's installation of python and this changes the python in use by system and causes those apps to fail. Instead, open a project folder and set the pyenv local only for that project and then do 'pyenv activate' as below
8. It also installs a plugin called `pyenv-virtualenv` (https://github.com/pyenv/pyenv-virtualenv) which works to create virtual environments.
9. To start a new project and its own virtual environment, do `pyenv virtualenv NAME-OF-ENV`
10. Activate it with `pyenv activate NAME-OF-ENV`
11. Seeing `python -m pip --version` or `python --version` should confirm and `python -m pip list` will give only pip in this folder/project
12. Install packages with pip i.e., `python -m pip install -r requirements.txt` and at the end `pyenv deactivate` to exit this environment.

# An alternative option is to install and use the Miniforge or the Anaconda distribution of Python
- I prioritize this lower as this distribution is larger in size to download and install. But it comes with `conda` package and environment manager which is very helpful for the beginner level.
- Here is a step by step guide from a previous course of mine: [https://github.com/akbaritabar/BiblioDemography_IMPRS_PHDS_2022_IDEM187/blob/main/0_code/01_Required_installation_setup_python.md](https://github.com/akbaritabar/BiblioDemography_IMPRS_PHDS_2022_IDEM187/blob/main/0_code/01_Required_installation_setup_python.md)

# List current environment's requirements
1. Activate the environment by following steps outlined above or "cd project-env-name" and `source ./bin/activate` or for Windows `.\Scripts\activate.bat`
2. Run `python -m pip freeze --local > requirements.txt` which will export all installed requirements in this environment and their exact versions into a requirements text file
3. Deactivate this environment with "deactivate"
4. Go back to the folder where you want to create a replication folder for this project and test reproducibility and follow steps above with `python -m virtualenv project-env-name` but use a different name for replication environment

# If you messed up the virtual environment
- Most importantly **Stay calm!** 
    - The goal of installing a light-weight vanilla Python and using virtual environments was to keep things clean and isolated from each other or the system not to cause any problems.
- Create a new environment following steps outlined above and install the required packages.


# Where to learn basics of R and Python?
## To start with Python

Check this website first:

[https://www.w3schools.com/python/python_intro.asp](https://www.w3schools.com/python/python_intro.asp)


Check this repository by Vincent Traag and others, for an introductory course and code:

[https://github.com/vtraag/intro-python](https://github.com/vtraag/intro-python)


Or this one by Data Carpentry:

[https://datacarpentry.org/python-ecology-lesson/](https://datacarpentry.org/python-ecology-lesson/)

## To start with R
Check this website first:

[https://www.w3schools.com/r/default.asp](https://www.w3schools.com/r/default.asp)
      

This "very short introduction to R" is a good start: 

[https://cran.r-project.org/doc/contrib/Torfs+Brauer-Short-R-Intro.pdf](https://cran.r-project.org/doc/contrib/Torfs+Brauer-Short-R-Intro.pdf)


Or this course by Data Carpentry:

[https://datacarpentry.org/R-genomics/index.html](https://datacarpentry.org/R-genomics/index.html)

