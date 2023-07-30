"""
Make a lexicon of words and their gender
"""
import importlib.resources as ir

from . import data


def mutate_number(number, next_word):
    """
    mutate known numbers
    :param text:
    :param number:
    :return:
    """
    black_list = ["miliwn"]
    if next_word and next_word not in black_list and next_word[0] in lexicon:
        info = lexicon[next_word[0]]
        if "Fem" in info:
            for num in number.split(" "):
                for mut in fem_mu:
                    if mut[0] == num:
                        text = text.replace(mut[0], mut[1])
    return text


def build_lexicon():
    """
    build a dict lookup from the lexicon file
    :return:
    """
    lex = ir.read_text(data, "lecsicon_cc0.txt")
    lexicon = {}
    for line in lex.splitlines():
        if "Gender" in line:
            cells = line.split("\t")
            for cell in cells:
                if "Gender" in cell:
                    lexicon[cells[0]] = cell[cell.index("Gender") :]
                    break
    return lexicon
