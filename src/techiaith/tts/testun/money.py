"""
Parse monitory values
"""
from .lookups import fem_mu, number_dict
from .number_norm import errors, find_numbers, find_replace

ceiniog = {
    "1": "ceiniog",
    "2": "dwy geiniog",
    "3": "tair ceiniog",
    "4": "pedair ceiniog",
    "5": "pum ceiniog",
    "6": "chwe cheiniog",
    "7": "saith ceiniog",
    "20": "ugain ceiniog",
    "50": "hanner can ceiniog",
}


def clean_money(number, append):
    """
    Clean a monitory string value
    :param number:
    :param append:
    :return:
    """
    money_number = number.replace("£", "")
    cleaned_string = ""
    if "m" in number:
        append += number_dict["m"]["lemma"] + " o bunnoedd"
        number = money_number.replace("m", "")
        cleaned_string = find_numbers(number) + " " + append
    elif "b" in number:
        append += number_dict["b"]["lemma"] + " o bunnoedd"
        number = money_number.replace("b", "")
        cleaned_string = find_numbers(number) + " " + append
    elif "c" in number:
        append += number_dict["c"]["lemma"] + " "
        number = money_number.replace("c", "")
        if number in ceiniog:
            cleaned_string = ceiniog[number]
        else:
            cleaned_string = find_numbers(number) + " " + append
    else:
        if "." in money_number:
            nums = money_number.split(".")
            c = 1
            for num in nums:
                if c == 2:
                    if len(num) == 1:
                        num += "0"
                cleaned_string += find_numbers(num)
                if c < len(nums):
                    cleaned_string += " " + number_dict["£"]["lemma"] + " a "
                c += 1
            cleaned_string += " " + number_dict["c"]["lemma"] + " "
        else:
            cleaned_string = find_numbers(money_number) + " " + number_dict["£"]["lemma"]
    if "punt" in cleaned_string:
        for mut in fem_mu:
            if not cleaned_string.startswith("un deg") and mut[0] in cleaned_string:
                cleaned_string = cleaned_string.replace(mut[0], mut[1])
    cleaned_string = find_replace(cleaned_string, errors, False, False)
    return cleaned_string
