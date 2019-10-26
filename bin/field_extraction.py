import logging

from gensim.utils import simple_preprocess

import lib

EMAIL_REGEX = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"
PHONE_REGEX = r"\(?(\d{3})?\)?[\s\.-]{0,2}?(\d{3})[\s\.-]{0,2}(\d{4})"


def candidate_name_extractor(input_string, nlp):

    doc = nlp(input_string.replace('\n','.'))

    doc_entities = doc.ents  # extract entities

    # Subset to person type entities
    doc_persons = filter(lambda x: x.label_ == 'PERSON', doc_entities)
    doc_persons = filter(lambda x: len(x.text.strip().split()) >= 2, doc_persons)
    doc_persons = map(lambda x: x.text.strip(), doc_persons)
    doc_persons = list(doc_persons)

    if len(doc_persons) > 0:  # assume that the first Person entity is the candidate's name
        return doc_persons[0]
    return "NOT FOUND"


def spacy_extractor_by_type(input_string, nlp, spacy_type, num_of_words):

    doc = nlp(input_string)

    doc_entities = doc.ents  # extract entities

    # Subset to spaCy_type type entities https://spacy.io/api/annotation#named-entities
    doc_persons = filter(lambda x: x.label_ == spacy_type, doc_entities)
    doc_persons = filter(lambda x: len(x.text.strip().split()) >= num_of_words, doc_persons)
    doc_persons = map(lambda x: x.text.strip(), doc_persons)
    doc_persons = list(doc_persons)

    return doc_persons


def extract_fields(df):
    for extractor, items_of_interest in lib.get_conf('case_agnostic_whole_resume').items():
        # column name is title of the sections in the yaml file
        df[extractor] = df['text'].apply(lambda x: extract_skills_case_agnostic(x, items_of_interest))

    for extractor, items_of_interest in lib.get_conf('case_agnostic_education').items():
        df[extractor] = df['Edu'].apply(lambda x: extract_skills_case_agnostic(x, items_of_interest))
    for extractor, items_of_interest in lib.get_conf('case_sensitive_education').items():
        df[extractor] = df['Edu'].apply(lambda x: extract_skills_case_sensitive(x, items_of_interest))

    for extractor, items_of_interest in lib.get_conf('case_agnostic_languages').items():
        df[extractor] = df['Language'].apply(lambda x: extract_skills_case_agnostic(x, items_of_interest))

    return df


def extract_skills_case_agnostic(resume_text, items_of_interest):
    potential_skills_dict = dict()
    matched_skills = set()

    for skill_input in items_of_interest:
        # Format list of strings inputs
        if type(skill_input) is list and len(skill_input) >= 1:
            potential_skills_dict[skill_input[0]] = skill_input
        # Format string inputs
        elif type(skill_input) is str:
            potential_skills_dict[skill_input] = [skill_input]
        else:
            logging.warning('Unknown skill listing type: {}. Please format as a string or a list of strings'.format(skill_input))

    for (skill_name, skill_alias_list) in potential_skills_dict.items():

        skill_matches = 0
        # iterate through each string in the list of equivalent words (i.e. a line in the yaml file)
        # TODO incorporate word2vec here?
        for skill_alias in skill_alias_list:
            skill_matches += lib.term_count(resume_text, skill_alias.lower())  # add the # of matches for each alias

        if skill_matches > 0:  # if at least one alias is found, add skill name to set of skills
            matched_skills.add(skill_name)

    if len(matched_skills) == 0:  # so it doesn't save 'set()' in the csv when it's empty
        matched_skills = ''

    return matched_skills


def extract_skills_case_sensitive(resume_text, items_of_interest):
    potential_skills_dict = dict()
    matched_skills = set()

    for skill_input in items_of_interest:
        if type(skill_input) is list and len(skill_input) >= 1:
            potential_skills_dict[skill_input[0]] = skill_input
        elif type(skill_input) is str:
            potential_skills_dict[skill_input] = [skill_input]
        else:
            logging.warning('Unknown skill listing type: {}.'.format(skill_input))

    for (skill_name, skill_alias_list) in potential_skills_dict.items():

        skill_matches = 0
        # TODO incorporate word2vec here?
        for skill_alias in skill_alias_list:
            skill_matches += lib.term_count_case_sensitive(resume_text, skill_alias)

        if skill_matches > 0:
            matched_skills.add(skill_name)

    if len(matched_skills) == 0:
        matched_skills = ''

    return matched_skills
