from .lexicon import build_lexicon
from .lookups import fem_mu

lexicon = build_lexicon()


def mutate_number(number, next_word):
    """
    mutate known numbers
    :param number:
    :param next_word:
    :return:
    """
    black_list = ["miliwn"]
    if next_word and next_word not in black_list and next_word in lexicon:
        info = lexicon[next_word]
        if "Fem" in info:
            for num in number.split(" "):
                for mut in fem_mu:
                    if mut[0] == num:
                        number = mut[1]
    return number


soft_mutations = [
    ["c", "g"],
    ["p", "b"],
    ["t", "d"],
    ["g", " "],
    ["b", "f"],
    ["d", "dd"],
    ["ll", "l"],
    ["rh", "r"],
    ["m", "f"],
]

nasal_mutations = [
    ["c", "ngh"],
    ["p", "mh"],
    ["t", "nh"],
    ["g", "ng"],
    ["b", "m"],
    ["d", "n"],
]

aspirate_mutations = [
    ["c", "ch"],
    ["p", "ph"],
    ["t", "th"],
]

soft_mutators = [
    # SOFT
    "dyma",
    "dyna",
    "wele",
    "y",
    "neu",
    "dy",
    "ei",
    "a'i",
    "i'w",
    "pa",
    "sut",
    "yn",
    "'n",
    "am",
    "ar",
    "at",
    "dan",
    "dros",
    "drwy",
    "gan",
    "heb",
    "hyd",
    "o",
    "tros",
    "trwy",
    "wrth",
    "i",
    "yna",
    "cafodd",
]
nasal_mutators = [
    # NASAL
    "fy",
    "'y",  # "yn",
]
aspirate_mutators = [
    # ASPIRATE
    "gyda",
    "tua",  # "ei", "'i", "a",
]


def mutate_on_previous(number, previous):
    previous = previous.rstrip()
    if previous in soft_mutators or previous.endswith("o"):
        for mutation in soft_mutations:
            if len(number) > 1 and mutation[0] == number[0]:
                number = number.replace(mutation[0], mutation[1], 1)
                break
    elif previous in nasal_mutators:
        for mutation in nasal_mutations:
            if len(number) > 1 and mutation[0] == number[0]:
                number = number.replace(mutation[0], mutation[1], 1)
                break
    elif previous in aspirate_mutators:
        for mutation in aspirate_mutations:
            if len(number) > 1 and mutation[0] == number[0]:
                number = number.replace(mutation[0], mutation[1], 1)
                break
    return number
