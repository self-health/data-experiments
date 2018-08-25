# data-experiments
experiments in processing NLM data

## Setup

Python 2 is used. The reason is that some of the needed packages have not been
upgraded to 3 as of yet.

Pipenv is used for package management.

To install:

pip install pipenv

To install required packages cd to project and run:

pipenv install

To add packages cd to project and run:

pipenv install package_name

To run the project you will need to activate the virtual environment created
by pipenv.

pipenv shell




## Getting NLM License

1. go to [UML-S license](https://uts.nlm.nih.gov//license.html)
2. accept conditions and create account
3. respond to email link, should receive activation within 3 days

## Download relevant datasets

Currently working with UML-S concepts mapped to Medline and extracted relationships from abstracts.

1. [UML-S concepts to Medline](https://ii.nlm.nih.gov/MMBaseline/index.shtml)
2. [Medline abstract extracts](https://skr3.nlm.nih.gov/SemMedDB/dbinfo.html)

## usage

Just create a folder to hold your current experiment.
