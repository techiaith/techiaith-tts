"""
Test number normaliser
"""

from techiaith.tts.testun.number_norm import find_numbers

# numbers_traditional = [
#     ["0", "dim"],
#     ["1", "un"],
#     ["2", "dau"],  # FEMININE: dwy
#     ["3", "tri"],  # FEMININE: tair
#     ["4", "pedwar"],  # FEMININE: pedair
#     ["5", "pump"],  # BEFORE NOUNS: pum
#     ["6", "chwech"],  # BEFORE NOUNS: chwe
#     ["7", "saith"],
#     ["8", "wyth"],
#     ["9", "naw"],
#     ["10", "deg"],  # BEFORE MIL, MLYNEDD: deng
#     ["11", "un ar ddeg"],
#     ["12", "deuddeg"],
#     ["13", "tri ar ddeg"],  # FEMININE: tair ar ddeg
#     ["14", "pedwar ar ddeg"],  # FEMININE: pedair ar ddeg
#     ["15", "pymtheg"],
#     ["16", "un ar bymtheg"],
#     ["17", "dau ar bymtheg"],  # FEMININE: un ar bymtheg
#     ["18", "deunaw"],
#     ["19", "pedwar ar bymtheg"],  # FEMININE: pedair ar bymtheg
#     ["20", "ugain"],  # ugain yn fwy traddodiadol, gyda phunnoedd ac amser
#     ["21", "un ar hugain"],
#     ["30", "deg ar hugain"],
#     ["31", "un ar ddeg ar hugain"],
#     ["31", "deuddeg ar hugain"],
#     ["40", "deugain"],
#     ["43", "pedwar a deugain"],
#     ["45", "pump a deugain"],
#     ["50", "hanner cant"],
#     ["51", "hanner cant ac un"],
#     ["52", "hanner cant a dau"],
#     ["60", "trigain"],
#     ["61", "un a thrigain"],
#     ["65", "pump un a thrigain"],
#     ["70", "deg a thrigain"],
#     ["71", "un ar ddeg a thrigain"],
#     ["76", "chwech ar ddeg a thrigain"],
#     ["80", "pedwar ugain"],
#     ["82", "dau a phedwar ugain"],
#     ["87", "saith a phedwar ugain"],
#     ["90", "deg a phedwar ugain"],
#     ["92", "deuddeg a phedwar ugain"],
#     ["99", "pedwar ar bymtheg a phedwar ugain"],
# ]

# numbers_modern = [
#     ["0", "dim"],
#     ["1", "un"],
#     ["2", "dau"],  # FEMININE: dwy
#     ["3", "tri"],  # FEMININE: tair
#     ["4", "pedwar"],  # FEMININE: pedair
#     ["5", "pump"],  # BEFORE NOUNS: pum
#     ["6", "chwech"],  # BEFORE NOUNS: chwe
#     ["7", "saith"],
#     ["8", "wyth"],
#     ["9", "naw"],
#     ["10", "deg"],  # BEFORE MIL, MLYNEDD: deng
#     ["11", "un deg un"],
#     ["12", "un deg dau"],
#     ["13", "un deg tri"],
#     ["14", "un deg pedwar"],
#     ["15", "un deg pump"],
#     ["16", "un deg chwech"],
#     ["17", "un deg saith"],
#     ["18", "un deg wyth"],
#     ["19", "un deg naw"],
#     ["20", "dau ddeg"],  # ugain yn fwy traddodiadol, gyda phunnoedd ac amser
#     ["21", "dau ddeg un"],
#     ["30", "tri deg"],
#     ["32", "tri deg dau"],
#     ["40", "pedwar deg"],
#     ["43", "pedwar deg tri"],
#     ["50", "pum deg"],
#     ["54", "pum deg pedwar"],
#     ["60", "chwe deg"],
#     ["65", "chwe deg pump"],
#     ["70", "saith deg"],
#     ["76", "saith deg chwech"],
#     ["80", "wyth deg"],
#     ["90", "naw deg"],
#     ["93", "naw deg tri"],
#     ["99", "naw deg naw"],
# ]

numbers_mixed = [
    ["0", "dim"],
    ["1", "un"],
    ["2", "dau"],  # FEMININE: dwy
    ["3", "tri"],  # FEMININE: tair
    ["4", "pedwar"],  # FEMININE: pedair
    ["5", "pump"],  # BEFORE NOUNS: pum
    ["6", "chwech"],  # BEFORE NOUNS: chwe
    ["7", "saith"],
    ["8", "wyth"],
    ["9", "naw"],
    ["10", "deg"],  # BEFORE MIL, MLYNEDD: deng
    ["11", "un ar ddeg"],
    ["12", "deuddeg"],
    ["13", "un deg tri"],
    ["14", "un deg pedwar"],
    ["15", "pymtheg"],
    ["16", "un deg chwech"],
    ["17", "un deg saith"],
    ["18", "deunaw"],
    ["19", "un deg naw"],
    ["20", "ugain"],  # ugain yn fwy traddodiadol, gyda phunnoedd ac amser
    ["21", "dau ddeg un"],
    ["30", "tri deg"],
    ["32", "tri deg dau"],
    ["40", "pedwar deg"],
    ["43", "pedwar deg tri"],
    ["50", "pum deg"],
    ["54", "pum deg pedwar"],
    ["60", "chwe deg"],
    ["65", "chwe deg pump"],
    ["70", "saith deg"],
    ["76", "saith deg chwech"],
    ["80", "wyth deg"],
    ["90", "naw deg"],
    ["93", "naw deg tri"],
    ["99", "naw deg naw"],
]

large_numbers = [
    ["101", "cant ac un"],
    ["111", "cant un deg un"],
    ["112", "cant un deg dau"],
    ["202", "dau gant a dau"],
    ["303", "tri chant a thri"],
    ["504", "pum cant a phedwar"],
    ["605", "chwe chant a phump"],
    ["793", "saith cant naw deg tri"],
    ["1050", "mil pum deg"],
    ["1100", "mil a chant"],
    ["2020", "dwy fil ac ugain"],
    ["2010", "dwy fil a deg"],
    ["16789", "un deg chwe mil saith cant wyth deg naw"],
    ["11110", "un deg un mil un cant a deg"],
    ["273693", "dau gant saith deg tri mil chwe chant naw deg tri"],
    ["73693", "saith deg tri mil chwe chant naw deg tri"],
    ["10020360", "deg miliwn dau ddeg mil tri chant a chwe deg"],
    [
        "123456789",
        "cant dau ddeg tri miliwn pedwar cant pum deg chwe mil saith cant wyth deg naw",
    ],
]

# deng mil, deuddeng mil

comma_number_phrases = [
    [
        "123,456,789",
        "cant dau ddeg tri miliwn pedwar cant pum deg chwe mil saith cant wyth deg naw",
    ],
]

decimal_phrases = [
    ["4.99", "pedwar pwynt naw naw"],
    ["499,000.34", "pedwar cant naw deg naw mil pwynt tri pedwar"],
]

phone_number_phrases = [
    # ["07984", "dim saith naw wyth pedwar"],
    ["07984663484", "dim saith naw wyth pedwar chwech chwech tri pedwar wyth pedwar"],
    ["079846634840", "dim saith naw wyth pedwar chwech chwech tri pedwar wyth pedwar dim"],
    [
        "+4479846634840",
        "plws pedwar pedwar saith naw wyth pedwar chwech chwech tri pedwar wyth pedwar dim",
    ],
    ["01248 345321", "dim un dau pedwar wyth tri pedwar pump tri dau un"],
]

tests = (
    numbers_mixed + large_numbers + comma_number_phrases + decimal_phrases + phone_number_phrases
)  # + numbers_traditional + numbers_modern


def test_wordify():
    for test in tests:
        words = find_numbers(test[0])
        assert test[1] == words
