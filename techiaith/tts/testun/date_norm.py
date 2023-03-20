"""
Date normaliser
"""
import re
from typing import List

from .lookups import days, months, mutations
from .number_norm import wordify

_time_re = re.compile(
    r"""\b
                          ((0?[0-9])|(1[0-9])|(2[0-9])|(3[0-1]))  # diwrnod
                          /
                          ((0?[0-9])|(1[0-2]))  # mis
                          /
                          ([0-9]{4})  # blywddyn
                          \b""",
    re.IGNORECASE | re.X,
)


def mutate(time_input, replacements):
    """
    mutate the know times
    :param time_input:
    :param replacements:
    :return:
    """
    for replacement in replacements:
        time_input = time_input.replace(replacement[0], replacement[1])
    return time_input


def _expand_date_welsh(match):
    date = []
    day = 0
    if match.group(1):
        day = int(match.group(1))
    elif match.group(2):
        day = int(match.group(2))
    elif match.group(3):
        day = int(match.group(3))
    elif match.group(4):
        day = int(match.group(4))
    date.append(days[day])
    date.append("o")
    month = 0
    if match.group(6):
        month = int(match.group(6))
    elif match.group(7):
        month = int(match.group(7))
    date.append(months[month])
    date.append(wordify(match.group(9)))
    return " ".join(date)


def expand_date_welsh(text):
    """
    expand and mutate time
    :param text:
    :return:
    """
    return mutate(re.sub(_time_re, _expand_date_welsh, text), mutations)
