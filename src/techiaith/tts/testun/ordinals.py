"""
Normalisation of ordinals
"""

from .lookups import days


def replace_ordinal(token):
    """
    Look up the relevant ordinal from the token input
    :param token:
    :return:
    """
    # a blank string to hold the remaining integers from the token
    lookup = ""
    for char in token:
        if char.isnumeric():
            lookup += char
    lookup = int(lookup)
    if lookup in days:
        token = days[lookup]
    return token
