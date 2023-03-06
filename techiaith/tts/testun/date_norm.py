"""
Date normaliser
"""
import re

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

months = {
    1: "Ionawr",
    2: "Chwefror",
    3: "Mawrth",
    4: "Ebrill",
    5: "Mai",
    6: "Mehefin",
    7: "Gorffennaf",
    8: "Awst",
    9: "Medi",
    10: "Hydref",
    11: "Tachwedd",
    12: "Rhagfyr"
}

days = {
    1: "cyntaf",
    2: "ail",
    3: "trydydd",
    4: "pedwerydd",
    5: "pumed",
    6: "chweched",
    7: "seithfed",
    8: "wythfed",
    9: "nawfed",
    10: "degfed",
    11: "unfed ar ddeg",
    12: "deuddegfed",
    13: "trydydd ar ddeg",
    14: "pedwerydd ar ddeg",
    15: "pymthegfed",
    16: "unfed ar bymtheg",
    17: "ail ar bymtheg",
    18: "deunawfed",
    19: "pedwerydd ar bymtheg",
    20: "ugeinfed",
    21: "unfed ar hugain",
    22: "ail ar hugain",
    23: "trydydd ar hugain",
    24: "pedwerydd ar hugain",
    25: "pumed ar hugain",
    26: "chweched ar hugain",
    27: "seithfed ar hugain",
    28: "wythfed ar hugain",
    29: "nawfed ar hugain",
    30: "degfed ar hugain",
    31: "unfed ar ddeg ar hugain",
}


def mutate(time_input: str) -> str:
    """
    mutate the know times
    :param time_input:
    :return:
    """
    replacements = []
    for replacement in replacements:
        time_input = time_input.replace(replacement[0], replacement[1])
    return time_input


def _expand_date_welsh(match: "re.Match") -> str:
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


def expand_date_welsh(text: str) -> str:
    """
    expand and mutate time
    :param text:
    :return:
    """
    return mutate(re.sub(_time_re, _expand_date_welsh, text))
