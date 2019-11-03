import inspect
import logging
import os
import sys
import pandas as pd
import spacy
# importing user defined modules
import field_extraction
import lib
import resume_sectioning

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))  # get location of main.py
parentdir = os.path.dirname(currentdir)  # get parent directory of main.py (where repository is on local)
sys.path.insert(0, parentdir)  # sys.path is the module search path


def main():

    logging.getLogger().setLevel(logging.WARNING)  # essentially does print statements to help debug (WARNING)
    # logging explained https://appdividend.com/2019/06/08/python-logging-tutorial-with-example-logging-in-python/

    observations = extract()  # get text from resumes

    # from https://www.kaggle.com/maitrip/resumes/download, did some data cleaning on it and resaved it
    kaggle_resumes = pd.read_csv('~/PycharmProjects/Resume-Parser/data/input/resumes/Kaggle_resume_dataset.csv', usecols=[0, 1, 2])
    # observations = pd.concat([observations, kaggle_resumes], sort=False)

    # to get the start (as an int) of resume sections
    observations = resume_sectioning.section_into_columns(observations)
    output_path = os.path.join(lib.get_conf('summary_output_directory'), 'resume_parsed_int.csv')
    observations.to_csv(path_or_buf=output_path, index=False)

    # get only words pertaining each sub-section
    observations = resume_sectioning.word_put_in_sections(observations)

    # to combine the sub-sections
    observations = resume_sectioning.combine_sections_preparse(observations)
    output_path = os.path.join(lib.get_conf('summary_output_directory'), 'resume_sections.csv')
    observations.to_csv(path_or_buf=output_path, index=False)

    # to skip the section above
    # observations = pd.read_csv('~/PycharmProjects/Resume-Parser/data/output/resume_sections.csv')

    nlp = spacy.load('en_core_web_sm')  # spacy NLP

    observations = transform(observations, nlp)  # extract data from resume sections

    # to combine the sub-sections one last time
    observations = resume_sectioning.combine_sections_postparse(observations)

    load(observations)  # save to csv to finish

    pass


def extract():
    logging.info('Begin extract')

    candidate_file_agg = list()  # for creating list of resume file paths
    for root, subdirs, files in os.walk(lib.get_conf('resume_directory')):  # gets path to resumes from yaml file
        # os.walk(parentdir + '/data/input/example_resumes'): would do the same thing
        files = filter(lambda f: f.endswith(('.pdf', '.PDF')), files)  # only read pdfs
        folder_files = map(lambda x: os.path.join(root, x), files)
        candidate_file_agg.extend(folder_files)

    observations = pd.DataFrame(data=candidate_file_agg, columns=['file_path'])  # convert to df
    logging.info('Found {} candidate files'.format(len(observations.index)))
    observations['extension'] = observations['file_path'].apply(lambda x: os.path.splitext(x)[1])  # e.g. pdf or doc
    observations = observations[observations['extension'].isin(lib.AVAILABLE_EXTENSIONS)]
    logging.info('Subset candidate files to extensions w/ available parsers. {} files remain'.
                 format(len(observations.index)))
    observations['text'] = observations['file_path'].apply(lib.convert_pdf)  # get text from .pdf files

    # Archive schema and return
    lib.archive_dataset_schemas('extract', locals(), globals())  # saving the schema
    logging.info('End extract')
    return observations


def transform(observations, nlp):
    logging.info('Begin transform')

    observations['candidate_name'] = observations['text'].apply(lambda x: field_extraction.candidate_name_extractor(x, nlp))
    observations['email'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.EMAIL_REGEX))
    observations['phone'] = observations['text'].apply(lambda x: lib.term_match(x, field_extraction.PHONE_REGEX))
    observations['GPA'] = observations['text'].apply(lambda x: field_extraction.gpa_extractor(x))

    # observations['work_dates'] = observations['Work'].apply(
    #     lambda x: field_extraction.spacy_extractor_by_type(str(x).replace('\n', '. '), nlp, 'DATE', 2))

    # observations['uni'] = observations['Edu'].apply(
    #     lambda x: field_extraction.spacy_extractor_by_type(str(x), nlp, 'ORG', 2))

    observations = field_extraction.extract_fields(observations)  # search for terms in whole resume

    # Archive schema and return
    lib.archive_dataset_schemas('transform', locals(), globals())
    logging.info('End transform')
    return observations


def load(observations):
    logging.info('Begin load')
    output_path = os.path.join(lib.get_conf('summary_output_directory'), 'resume_summary.csv')

    logging.info('Results being output to {}'.format(output_path))
    print('Results output to {}'.format(output_path))

    observations.to_csv(path_or_buf=output_path, index_label='index')
    logging.info('End transform')
    pass


if __name__ == '__main__':
    main()
