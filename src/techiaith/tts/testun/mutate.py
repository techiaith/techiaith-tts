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
    ["p", "b", ""],
    ["t", "d", ""],
    ["d", "dd", "dd"],
    ["c", "g", "ch"],
]


def mutate_on_previous(number, previous_char):
    if previous_char in "aeiou":
        for mutation in soft_mutations:
            if len(number) > 1 and mutation[0] == number[0] and not mutation[2] == number[:2]:
                number = number.replace(mutation[0], mutation[1], 1)
    return number
