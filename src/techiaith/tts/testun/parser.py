"""
Parse text using spacy to find the required normalisation
"""
import spacy

from .time_norm import expand_time_welsh
from .date_norm import expand_date_welsh
from .number_norm import find_numbers

nlp = spacy.load("cy_techiaith_tag_lem_ner_lg")

PERCENT = 393
ORDINAL = 396
CARDINAL = 397
MONEY = 394
DATE = 391
TIME = 392
QUANTITY = 395
entities = [CARDINAL, DATE, MONEY, ORDINAL, PERCENT, QUANTITY, TIME]


def parse_text(text):
    """
    Parsio'r testun yn defnyddio NLP i chwilio am endidau
    Parse the text using NLP to find entities
    :param text:
    :return:
    """
    doc = nlp(text)
    for t in doc:
        find_entity(t.ent_type, t.text)


def find_entity(ent_type, value):
    """
    Galw y function sy'n mynd gyda'r fath o endid
    Call the function associated with the entity type
    :param ent_type:
    :param value:
    :return:
    """
    fnd_digit = False
    for c in value:
        if c.isdigit():
            fnd_digit = True
            break
    if fnd_digit:
        if ent_type == TIME:
            result = expand_time_welsh(value)
            print("TIME", value, result)

        elif ent_type == DATE:
            result = expand_date_welsh(value)
            print("DATE", value, result)

        elif ent_type == CARDINAL:
            result = find_numbers(value)
            print("CARDINAL", value, result)

        elif ent_type == ORDINAL:
            result = find_numbers(value)
            print("ORDINAL", value, result)

        elif ent_type == MONEY:
            print("MONEY", value)

        elif ent_type == PERCENT:
            print("PERCENT", value)

        elif ent_type == QUANTITY:
            print("QUANTITY", value)
