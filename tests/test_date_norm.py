"""
Test number normaliser
"""
from techiaith.tts.testun.date_norm import expand_date_welsh

# TODO: Ychwanegu pob mis i xx/xx/xx

## Trin yn + nnnn fel blwyddyn o fewn cyfnod penodol?
# TODO: ym + 19xxx = ym mil naw x x
# TODO: yn + 2000 - 2050(?) = yn nwy fil x x

# TODO: Degawdau
# 1920au - "un naw dau ddegau" (?)
# 20au - "ugeiniau"


tests = [
    [
        "1/1/2020",
        "cyntaf o Ionawr dwy fil ac ugain",
    ],  # arolwg Twitter yn rhoi 53% o blaid "ac ugain vs 19% "dau ddeg" (n=206)
    ["02/2/2023", "ail o Chwefror dwy fil dau ddeg tri"],
    ["3/03/2021", "trydydd o Fawrth dwy fil dau ddeg un"],
    ["04/04/2021", "pedwerydd o Ebrill dwy fil dau ddeg un"],
    ["5/5/1995", "pumed o Fai mil naw naw pump"],
    ["15/06/2021", "pymthegfed o Fehefin dwy fil dau ddeg un"],
    ["31/7/2000", "tri deg un o Orffennaf dwy fil"],
    ["25/8/2010", "pumed ar hugain o Awst dwy fil a deg"],
    ["6/9/1999", "chweched o Fedi mil naw naw naw"],
    ["01/10/1920", "cyntaf o Hydref mil naw dau ddeg"],
    ["9/11/2024", "nawfed o Dachwedd dwy fil dau ddeg pedwar"],
    ["21/12/2024", "dau ddeg un o Ragfyr dwy fil dau ddeg pedwar"],  # unfed ar hugain?
]


def test_date():
    for date in tests:
        result = expand_date_welsh(date[0])
        assert result == date[1]
