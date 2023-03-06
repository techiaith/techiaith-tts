"""
Test number normaliser
"""
from techiaith.tts.testun.date_norm import expand_date_welsh

tests = [
    ["1/1/2020", "cyntaf o Ionawr dau mil dau ddeg"],
    ["01/10/1920", "cyntaf o Hydref mil naw cant dau ddeg"],
    ["21/12/2024", "unfed ar hugain o Rhagfyr dau mil dau ddeg pedwar"],
]


def test_date():
    for date in tests:
        result = expand_date_welsh(date[0])
        assert result == date[1]
