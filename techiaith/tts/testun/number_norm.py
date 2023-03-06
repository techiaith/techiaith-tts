"""
Main number normalisation
"""
import re

from .lexicon import build_lexicon
from .lookups import mutations, number_dict, fem_mu

errors = [
    ["dwy cant", "dau gant"],
    ["dwy gant", "dau gant"],
    ["dwy punt", "dwy bunt"],
    ["chwe punt", "chwe phunt"],
    ["saith punt", "saith bunt"],
    ["wyth punt", "wyth bunt"],
    ["un deg dim", "deg"],
    ["un deg mil", "deg mil"],
    ["un deg miliwn", "deg miliwn"],
    [" dim cant", ""],
    [" dim deg", ""],
    [" dim mil", ""],
]

start_errors = [
    ["un cant", "cant"],
    ["un mil", "mil"],
    ["un miliwn", "miliwn"],
]

band_markers = ["", "deg", "cant"]
markers = ["", "mil", "miliwn"]
lexicon = build_lexicon()


def find_numbers(text):
    """
    find the numbers in a string
    :param text:
    :return:
    """
    text = text.replace(",", "")
    is_mob, new_num = is_mobile(text)
    if is_mob:
        new_numbers = wordify(new_num)
        text = text.replace(new_num, new_numbers)
    else:
        text = wordify_and_replace(r"£\d+\.\d+m?", text)
        text = wordify_and_replace(r"£\d+m?", text)
        text = wordify_and_replace(r"\d+\.\d+", text)
        text = wordify_and_replace(r"\d+", text)
    return text


def wordify_and_replace(regex, text):
    """
    replace the results of wordify in the string matching the regex
    :param regex:
    :param text:
    :return:
    """
    nums = re.findall(regex, text)
    if len(nums) > 0:
        for num in nums:
            new_numbers = wordify(num)
            if "punt" in new_numbers or "bunt" in new_numbers:
                for mut in fem_mu:
                    if mut[0] in new_numbers:
                        new_numbers = new_numbers.replace(mut[0], mut[1])
            text = text.replace(num, new_numbers)
            if text != new_numbers:
                text = mutate_number(text, new_numbers)
    text = find_replace(text, errors, False)
    return text


def mutate_number(text, number):
    """
    mutate known numbers
    :param text:
    :param number:
    :return:
    """
    next_word = text.split(number, maxsplit=1)[-1].split(maxsplit=1)
    if next_word:
        info = lexicon[next_word[0]]
        if "Fem" in info:
            for num in number.split(" "):
                for mut in fem_mu:
                    if mut[0] == num:
                        text = text.replace(mut[0], mut[1])
    return text


def wordify(number):
    """
    convert a digit in string form into word form
    :param number:
    :return:
    """
    word_list = []
    cleaned_string = ""
    append = " "
    is_mob, new_num = is_mobile(number)
    if is_mob:
        for char in new_num:
            if char not in " ":
                word_integer = number_dict[char]["lemma"]
                word_list.append(word_integer)
        cleaned_string = " ".join(word_list)
    elif number in number_dict:
        cleaned_string = number_dict[number]["lemma"]
    elif "£" in number:
        money_number = number.replace("£", "")
        if "m" in number:
            append += number_dict["m"]["lemma"] + " " + number_dict["£"]["lemma"]
            number = money_number.replace("m", "")
            cleaned_string = wordify(number)
        else:
            if "." in money_number:
                nums = money_number.split(".")
                c = 1
                for num in nums:
                    cleaned_string += wordify(num)
                    if c < len(nums):
                        cleaned_string += " " + number_dict["£"]["lemma"] + " "
                    c += 1
                cleaned_string += " " + number_dict["c"]["lemma"] + " "
            else:
                cleaned_string = wordify(money_number) + " " + number_dict["£"]["lemma"]
    elif "." in number:
        nums = number.split(".")
        c = 1
        for num in nums:
            cleaned_string += wordify(num)
            if c < len(nums):
                cleaned_string += " " + number_dict["."]["lemma"] + " "
            c += 1
    else:
        band = []
        band_count = 0
        marker_count = 0
        for char in number[::-1]:
            band.append(char)
            exit_condition = len(band) + (band_count * 3)
            if len(band) == 3 or exit_condition == len(number):
                band_count += 1
                place_count = 0
                word_list.append(markers[marker_count])
                marker_count += 1
                for digit in band:
                    word_integer = number_dict[digit]["lemma"]
                    if word_integer != "dim" and len(number) > 1:
                        word_list.append(band_markers[place_count])
                        word_list.append(word_integer)
                    elif len(number) == 1:
                        word_list.append(word_integer)
                    place_count += 1
                band = []
        clean_words = []
        for word in word_list[::-1]:
            if word != "":
                clean_words.append(word + " ")
        cleaned_string = " ".join(clean_words)
    cleaned_string = cleaned_string.replace("  ", " ")
    cleaned_string = find_replace(cleaned_string, errors, False)
    cleaned_string = find_replace(cleaned_string, start_errors, True)
    cleaned_string = find_replace(cleaned_string, mutations, False)
    if append != " ":
        cleaned_string += append
    cleaned_string = cleaned_string.strip()
    return cleaned_string


def is_mobile(word_number):
    """
    regex to find mobile numbers
    :param word_number:
    :return:
    """
    phone_regex = (
        "^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$"
    )
    result = re.match(phone_regex, word_number)
    if result:
        if len(result.group(0)) >= 11:
            return True, result.group(0)
    return False, ""


def find_replace(word_number, black_list, strats_with):
    """
    Find and replace words from a list
    :param word_number:
    :param black_list:
    :param strats_with:
    :return:
    """
    for replacement in black_list:
        word_number = word_number.replace(replacement[0], replacement[1])
    if strats_with:
        for error in black_list:
            if word_number.startswith(error[0]):
                word_number = word_number.replace(error[0], error[1])
    return word_number
