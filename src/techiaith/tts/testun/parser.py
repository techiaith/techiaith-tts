"""
Parse text using spacy to find the required normalisation
"""
from string import punctuation

import spacy

from .date_norm import expand_date_welsh
from .known_phrases import replace_phrase
from .money import clean_money
from .number_norm import find_numbers
from .ordinals import replace_ordinal
from .time_norm import expand_time_welsh
from .mutate import mutate_on_previous

nlp = spacy.load("cy_techiaith_tag_lem_ner_lg")

PERCENT = 393
ORDINAL = 396
CARDINAL = 397
MONEY = 394
DATE = 391
TIME = 392
QUANTITY = 395
entities = [CARDINAL, DATE, MONEY, ORDINAL, PERCENT, QUANTITY, TIME]

parser_errors = [["pumped", "pumed"], ["£", ""]]


def parse_text(text):
    """
    Parsio'r testun yn defnyddio NLP i chwilio am endidau
    Parse the text using NLP to find entities
    :param text:
    :return:
    """
    text = replace_phrase(text)
    text = expand_date_welsh(text)
    doc = nlp(text)
    replacements = []
    previous_token = {}
    for t in doc:
        # print(t, "\t", t.pos_, "\t", t.ent_type_)
        if t.pos_ is "NUM" or t.ent_type in entities:
            previous = "*"
            if previous_token:
                previous = previous_token.text
            entity = find_entity(t.ent_type, t.text, previous)
            if len(entity) > 0 and not t.text == entity:
                replacements.append([t.text, entity])
            if previous_token:
                pass
        if t.text.isalnum():
            previous_token = t
    tokens = replace_results(replacements, doc.text)
    return fix_parser_errors(" ".join(tokens))


def replace_results(replacements, text):
    """
    Replace the original text with the results of the parser
    Newid y destun gwreiddiol gyda'r calyniadau o'r parsiwr
    :param replacements:
    :param text:
    :return:
    """
    tokens = text.split()
    for action in replacements:
        index = 0
        for word in tokens:
            if action[0] == word.strip(punctuation + "£"):
                tokens[index] = word.replace(action[0], action[1])
            index += 1
    return tokens


def find_entity(ent_type, value, previous):
    """
    Galw y function sy'n mynd gyda'r fath o endid
    Call the function associated with the entity type
    :param ent_type:
    :param value:
    :return result:
    """
    fnd_digit = False
    result = ""
    for c in value:
        if c.isdigit() or not c.isalnum():
            fnd_digit = True
            break
    if fnd_digit:
        if ent_type == TIME:
            result = expand_time_welsh(value)
        elif ent_type == DATE:
            result = expand_date_welsh(value)
        elif ent_type == CARDINAL or ent_type == PERCENT or ent_type == QUANTITY:
            result = find_numbers(value)
        elif ent_type == ORDINAL:
            result = replace_ordinal(value)
        elif ent_type == MONEY:
            if value != "£":
                value = value.replace(",", "")
                result = clean_money(value, "")
        else:
            result = find_numbers(value)
        result = mutate_on_previous(result, previous[len(previous) - 1])
    else:
        result = value
    return result


def fix_parser_errors(text):
    """
    Fix parser errors
    Trwsio gwallau yn y parsio
    :param text:
    :return:
    """
    for err in parser_errors:
        text = text.replace(err[0], err[1])
    return text
