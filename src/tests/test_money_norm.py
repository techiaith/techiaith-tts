"""
Test money normaliser
"""
from techiaith.tts.testun.money import clean_money

tests = [
    # PUNNOEDD
    ["£4.99", "pedwar punt a naw deg naw ceiniog"],
    ["£200", "dau gan punt"],
    ["£1", "punt"],
    ["£1m", "un miliwn o bunnoedd"],
    ["£10m", "deg miliwn o bunnoedd"],
    ["£5.5m", "pump pwynt pump miliwn o bunnoedd"],
    ["€1", "un ewro"],
    ["$100", "cant o ddoleri"],
    ["£2", "dau punt"],
    ["£3", "tri punt"],
    ["£4", "pedwar punt"],
    ["£5", "pump punt"],
    ["£6", "chwech punt"],
    ["£7", "saith punt"],
    ["£8", "wyth punt"],
    ["£9", "naw punt"],
    ["£10", "deg punt"],
    ["£500", "pum cant punt"],
    ["£600", "chwe chan punt"],
    ["£1050.25", "mil pum deg punt a dau ddeg pump ceiniog"],
    ["£20m", "ugain miliwn o bunnoedd"],
    ["£2.3m", "dau pwynt tri miliwn o bunnoedd"],
    ["£2.3b", "dau pwynt tri biliwn o bunnoedd"],
    ["£99", "naw deg naw punt"],
    # CEINIOGAU
    ["1c", "ceiniog"],
    ["2c", "dwy geiniog"],
    ["3c", "tair ceiniog"],
    ["4c", "pedair ceiniog"],
    ["5c", "pum ceiniog"],
    ["6c", "chwe cheiniog"],
    ["7c", "saith ceiniog"],
    ["20c", "ugain ceiniog"],
    [
        "50c",
        "hanner can ceiniog",
    ],  # 'chweugain' traditional but increasingly archaic (and is technically 120c)
]


def test_clean_money():
    for test in tests:
        result = clean_money(test[0], "")
        assert test[1] == result
