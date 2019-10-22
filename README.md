# ResumeParser

A utility to make handling many resumes easier by automatically pulling contact information, required skills and custom text fields. These results are then surfaced as a convenient summary CSV.

## Quick Start Guide

```bash
# Install requirements
pip install -r requirements.txt

# Retrieve language model from spacy
python -m spacy download en

# Run code (with default configurations)
cd bin/
python main.py

# Review output
open ../data/output/resume_summary.csv

```

## Getting started

### Repo structure

 - `bin/main.py`: Code entry point
 - `confs/confs.yaml.template`: Configuration file template
 - `data/input/example_resumes`: Example resumes, which are parsed w/ default configurations
 - `data/output/resume_summary.csv`: Results from parsing example resumes

### Python Environment

Python code in this repo utilizes packages that are not part of the common library. To make sure you have all of the 
appropriate packages, please use `pip` to install the `requirements.txt` file. For more details, please see the [pip 
documentation](https://pip.pypa.io/en/stable/user_guide/#requirements-files)

### Configuration file

This program utilizes a configuration file to set program parameters. You can run this program with the default
parameters view sample output, but you'll probably want to create a config file and modify it to get the most value
from this program.

```bash

# Create configuration file from template
scp confs/confs.yaml.template confs/confs.yaml

# Modify confs to match your needs
open confs/confs.yaml
```

The configuration file has a few parameters you can tweak:
 - `resume_directory`: A directory containing resumes you'd like to parse
 - `summary_output_directory`: Where to place the .csv file, summarizing your resumes
 - `data_schema_dir`: The directory to store table schema. This is mostly for development purposes
 - `skills`: A YAML list of skills. Each element in this list can either be a string (e.g. `skill1` or
 `machine learning`), or a list aliases for the same skill (e.g. `[skill2_alias_A, skill2_alias_B]` or `[ml,
 machine learning, machine-learning]`)
 - `universities`: A YAML list of universities you'd like to search for
