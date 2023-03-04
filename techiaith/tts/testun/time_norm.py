"""
Time normaliser
"""
import re

_time_re = re.compile(
    r"""\b
                          ((0?[0-9])|(1[0-1])|(1[2-9])|(2[0-3]))  # oriau
                          :
                          ([0-5][0-9])                            # munud
                          \s*(y\\.b\\.|yb|yh|y\\.h\\.)? # yb/yh
                          \b""",
    re.IGNORECASE | re.X,
)

mut_numbers = {
    1: "un",
    2: "ddau",
    3: "dri",
    4: "bedwar",
    5: "bump",
    6: "chwech",
    7: "saith",
    8: "wyth",
    9: "naw",
    10: "deg",
    11: "unarddeg",
    12: "ddeuddeg",
}

numbers = {
    0: "",
    1: "un",
    2: "dau",
    3: "tri",
    4: "pedwar",
    5: "pump",
    6: "cwhwech",
    7: "saith",
    8: "wyth",
    9: "naw",
    10: "deg",
    11: "un ar ddeg",
    12: "deuddeg",
    13: "tair ar ddeg",
    14: "pedwar ar ddeg",
    15: "chwater",
    16: "un ar bymtheg",
    17: "dau ar bymtheg",
    18: "deunaw",
    19: "pedwar ar bymtheg",
    20: "ugain",
    21: "un ar hugain",
    22: "dau ar hugain",
    23: "tri ar hugain",
    24: "pedwar ar hugain",
    25: "pump ar hugain",
    26: "chwech ar hugain",
    27: "saith ar hugain",
    28: "wyth ar hugain",
    29: "naw ar hugain",
    30: "hanner",
}


def known_times(hour):
    time = ""
    if hour == 12:
        time = "hanner dydd"
    if hour == 0:
        time = "hanner nos"
    return time


def _expand_num(n: int, pre: str) -> str:
    exp_num = numbers[n]
    if pre == "i":
        exp_num = mut_numbers[n]
    return exp_num


def mutate(time_input: str) -> str:
    replacements = [
        ["dau munud", "dau funud"],
        ["chwech munud", "chwe munud"]
    ]
    for replacement in replacements:
        time_input = time_input.replace(replacement[0], replacement[1])
    return time_input


def _expand_time_welsh(match: "re.Match") -> str:
    time = []
    # nifer munud (wedi/i) nifer awr o'r gloch y bore/nos
    minute = int(match.group(6))
    sep = "i"
    if minute <= 30:
        sep = "wedi"
    hour = int(match.group(1))
    if sep == "i":
        hour += 1
        minute = 60 - minute
    if minute > 0:
        ex_min = _expand_num(minute, "")
        ex_min = ex_min.replace(" ar ", " munud ar ")
        time.append(ex_min)
        if minute not in [15, 30]:
            if "munud" not in ex_min:
                time.append("munud")
        else:
            time.append("awr")
        time.append(sep)
    past_noon = hour >= 12
    if hour > 12:
        hour -= 12

    kt = known_times(hour)
    if kt:
        time.append(kt)
    else:
        time.append(_expand_num(hour, sep))
        am_pm = match.group(7)
        if am_pm is None:
            time.append("y hwyr" if past_noon else "y bore")
        else:
            if "h" in am_pm:
                time.append("y hwyr")
            else:
                time.append("y bore")

    return " ".join(time)


def expand_time_welsh(text: str) -> str:
    return mutate(re.sub(_time_re, _expand_time_welsh, text))
