"""
Test money normaliser
"""
from techiaith.tts.testun.money import clean_money

tests = [
    ["£4.99", "pedair punt a naw deg naw ceiniog"],
    ["£200", "dau gan punt"],
    ["£1", "punt"],
    ["£2", "dwy bunt"],
    ["£3", "tair punt"],
    ["£4", "pedair punt"],
    ["£5", "pum punt"],
    ["£6", "chwe phunt"],
    ["£7", "saith bunt"],
    ["£8", "wyth bunt"],
    ["£9", "naw punt"],
    ["£10", "deg punt"],
    ["£1050.25", "mil pum deg punt a dau ddeg pump ceiniog"],
    ["£20m", "ugain miliwn o bunnoedd"],
    ["£2.3m", "dau bwynt tri miliwn o bunnoedd"],
    ["£2.3b", "dau bwynt tri biliwn o bunnoedd"],
    ["£99", "naw deg naw punt"],
]


def test_clean_money():
    for test in tests:
        result = clean_money(test[0], "")
        assert test[1] == result
