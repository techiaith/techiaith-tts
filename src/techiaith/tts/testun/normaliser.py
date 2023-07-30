"""
Parse text using spacy to find the required normalisation
"""
from string import punctuation

import spacy

from .date_norm import expand_date_welsh, expand_day_month, expand_year, find_cardinal
from .known_phrases import replace_phrase
from .money import clean_money
from .mutate import mutate_number, mutate_on_previous
from .number_norm import find_numbers
from .ordinals import replace_ordinal
from .time_norm import expand_time_welsh

nlp = spacy.load("cy_techiaith_tag_lem_ner_lg")

DATE = 391
TIME = 392
PERCENT = 393
MONEY = 394
QUANTITY = 395
ORDINAL = 396
CARDINAL = 397
EVENT = 387
entities = [CARDINAL, DATE, MONEY, ORDINAL, PERCENT, QUANTITY, TIME, EVENT]

parser_errors = [["pumped", "pumed"], ["£", ""], [" .", "."]]


def parse_text(text):
    """
    Parse the text using NLP to find entities
    Parsio'r testun yn defnyddio NLP i chwilio am endidau
    :param text:
    :return:
    """
    text = replace_phrase(text)
    text = expand_date_welsh(text)
    text = expand_time_welsh(text)
    doc = nlp(text)
    previous_token = ""
    next_token = {}
    tokens = []
    c = 0
    for t in doc:
        if c < len(doc) - 1:
            next_token = doc[c + 1]
        text = t.text_with_ws
        new_num = _number_from_text(text)
        if new_num != "NN" and (t.pos_ == "NUM" or t.ent_type in entities):
            entity = find_entity(t.ent_type, text, previous_token, next_token)
            if len(entity) > 0 and not t.text == entity:
                tokens.append(entity)
            else:
                tokens.append(text)
        else:
            tokens.append(text)
        if text == "y " and previous_token == "'":
            previous_token = "'y"
        elif text in ["'i ", "'w ", "'n ", "'", "n "]:
            previous_token += text
        else:
            if text not in punctuation + "£":
                previous_token = text
        c += 1
    return fix_parser_errors("".join(tokens)).strip()


def _number_from_text(text):
    number = ""
    for c in text:
        if c.isdigit():
            number += c
    try:
        int(number)
    except ValueError:
        number = "NN"
    return number


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


def find_entity(ent_type, value, previous, next_token):
    """
    Call the function associated with the entity type
    Galw y function sy'n mynd gyda'r fath o endid
    :param previous:
    :param next_token:
    :param ent_type:
    :param value:
    :return result:
    """
    fnd_digit = False
    result = ""
    has_white_space = value[len(value) - 1] == " "
    for c in value:
        if c.isdigit() or not c.isalnum():
            fnd_digit = True
            break
    if fnd_digit:
        if ent_type == TIME:
            result = expand_time_welsh(value)
            if result == value:
                result = find_numbers(value)
        elif ent_type in [DATE, EVENT]:
            if _is_cardinal(value):
                result = find_cardinal(value)
            elif len(value) == 4:
                result = expand_year(value)
            elif len(value) <= 2:
                result = expand_day_month(value, is_month(next_token))
            else:
                result = expand_date_welsh(value)
            if result == value:
                result = find_numbers(value)
        elif ent_type == CARDINAL or ent_type == PERCENT or ent_type == QUANTITY:
            result = find_numbers(value)
            if next_token:
                result = mutate_number(result, next_token.text)
        elif ent_type == ORDINAL:
            result = replace_ordinal(value)
        elif ent_type == MONEY:
            if value != "£":
                value = value.replace(",", "")
                result = clean_money(value, "")
        else:
            result = find_numbers(value)
        if len(previous) > 0:
            result = mutate_on_previous(result, previous.rstrip())
    else:
        result = value
    if len(result) > 1 and result[len(result) - 1] != " " and has_white_space:
        result += " "
    return result


def _is_cardinal(text):
    fnd = False
    cardinals = ["ed", "ydd", "ail", "af"]
    for cardinal in cardinals:
        if cardinal in text:
            fnd = True
            break
    return fnd


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


def is_month(token):
    """
    Check if token is a month
    Checio os mae'r token yn mis
    :param token:
    :return:
    """
    is_month_name = (
        str(token).lower()
        in "ionawr,chwefror,mawrth,ebrill,mai,mehefin,gorffennaf,awst,medi,hydref,tachwedd,rhagfyr"
    )
    return is_month_name
