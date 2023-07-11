"""
Test number normaliser
"""
from techiaith.tts.testun.number_norm import find_numbers

tests = [
    ["0", "dim"],
    ["1", "un"],
    ["2", "dau"],
    ["2 glustog", "dwy glustog"],
    ["2 cwmwl", "dau cwmwl"],
    ["2 gadair", "dwy gadair"],
    ["3", "tri"],
    ["3 cwmwl", "tri cwmwl"],
    ["3 chlustog", "tair chlustog"],
    ["3 gadair", "tair gadair"],
    ["4", "pedwar"],
    ["5", "pump"],
    ["6", "chwech"],
    ["7", "saith"],
    ["8", "wyth"],
    ["9", "naw"],
    ["10", "deg"],
    ["11", "un deg un"],
    ["12", "deuddeg"],
    ["13", "un deg tri"],
    ["14", "un deg pedwar"],
    ["15", "un deg pump"],
    ["16", "un deg chwech"],
    ["17", "un deg saith"],
    ["18", "un deg wyth"],
    ["019", "un deg naw"],
    ["20", "ugain"],  # ugain yn fwy traddodiadol, gyda phunnoedd ac amser
    ["30", "tri deg"],
    ["40", "pedwar deg"],
    ["50", "pum deg"],
    ["60", "chwe deg"],
    ["70", "saith deg"],
    ["80", "wyth deg"],
    ["90", "naw deg"],
    ["93", "naw deg tri"],
    ["100", "cant"],
    ["110", "cant a deg"],
    ["120", "cant ac ugain"],
    ["500", "pum cant"],
    ["1000", "mil"],
    ["10000", "deg mil"],
    ["21", "dau ddeg un"],
    ["32", "tri deg dau"],
    ["43", "pedwar deg tri"],
    ["54", "pum deg pedwar"],
    ["65", "chwe deg pump"],
    ["76", "saith deg chwech"],
    ["87", "wyth deg saith"],
    ["98", "naw deg wyth"],
    ["99", "naw deg naw"],
    ["101", "cant ac un"],
    ["111", "cant un deg un"],
    ["112", "cant un deg dau"],
    ["118", "cant un deg wyth"],
    ["119", "cant un deg naw"],
    ["202", "dau gant a dau"],
    ["303", "tri chant a thri"],
    ["504", "pum cant a phedwar"],
    ["605", "chwe chant a phump"],
    ["793", "saith cant naw deg tri"],
    ["1050", "mil pum deg"],
    ["1100", "mil a chant"],
    ["2020", "dwy fil ac ugain"],
    ["2010", "dwy fil a deg"],
    ["2015", "dwy fil ac un deg pump"],
    ["2019", "dwy fil ac un deg naw"],
    ["16789", "un deg chwe mil saith cant wyth deg naw"],
    ["11110", "un deg un mil un cant a deg"],
    ["273693", "dau gant saith deg tri mil chwe chant naw deg tri"],
    ["73693", "saith deg tri mil chwe chant naw deg tri"],
    ["10020360", "deg miliwn dau ddeg mil tri chant a chwe deg"],
    ["07984663484", "dim saith naw wyth pedwar chwech chwech tri pedwar wyth pedwar"],
    ["079846634840", "dim saith naw wyth pedwar chwech chwech tri pedwar wyth pedwar dim"],
    [
        "+4479846634840",
        "plws pedwar pedwar saith naw wyth pedwar chwech chwech tri pedwar wyth pedwar dim",
    ],
    ["01248 345321", "dim un dau bedwar wyth tri pedwar pump tri dau un"],
    [
        "123,456,789",
        "cant dau ddeg tri miliwn pedwar cant pum deg chwe mil saith cant wyth deg naw",
    ],
    ["4.99", "pedwar pwynt naw naw"],
    ["499,000.34", "pedwar cant naw deg naw mil pwynt tri pedwar"],
    ["mae yna 2 gath", "mae yna dwy gath"],
    ["Dwi am fynd adref cyn 12", "Dwi am fynd adref cyn deuddeg"],
]


def test_wordify():
    for test in tests:
        words = find_numbers(test[0])
        assert test[1] == words
