# Resume Parser

This module converts pdfs to text, sections the resume into main sections, pulls pertinent information, and cleans the data. The results are then aggregated and saved in a convenient summary CSV.

## Quick Use Guide

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

## Repo structure

 - `bin/main.py`: Code entry point
 - `confs/confs.yaml.template`: Configuration file template
 - `data/input/resumes`: Resumes
 - `data/output/resume_summary.csv`: Results from parsing example resumes
 - `data/output/resume_sections.csv`: Resumes sectioned into sections (each its own column)


