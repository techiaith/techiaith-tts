"""
Script to replace known phrases in text
"""

black_list = [
    ["golwg360", "golwg tri chwech dim"],
    ["golwg 360", "golwg tri chwech dim"],
    ["bro360", "bro tri chwech dim"],
    ["ogwen360", "ogwen tri chwech dim"],
    ["mon360", "mon tri chwech dim"],
    ["tegid360", "tegid tri chwech dim"],
    ["aeron360", "aeron tri chwech dim"],
    ["bangorfelin360", "bangorfelin tri chwech dim"],
    ["broaber360", "broaber tri chwech dim"],
    ["brocardi360", "brocardi tri chwech dim"],
    ["browyddfa360", "browyddfa tri chwech dim"],
    ["caernarfon360", "caernarfon tri chwech dim"],
    ["caron360", "caron tri chwech dim"],
    ["carthen360", "carthen tri chwech dim"],
    ["clonc360", "clonc tri chwech dim"],
    ["cwilt360", "cwilt tri chwech dim"],
    ["dyffrynnantlle360", "dyffrynnantlle tri chwech dim"],
    ["s4c", "es pedwar ec"],
    ["...", ","],
    ["*", "seren"],
    ["S4C", "es pedwar ec"],
    ["%", " y cant"],
    [" 999", " naw naw naw"],
    ["@", " at "],
    # ["/", "i"],
    ["°C", " gradd selsiws"],
    ["#", "hash nod "],
    ["cm", " centimetr"],
    ["km", " cilometr"],
    ["mm", " milomedr"],
    ["OpenWeatherMap", "Open Weather Map"],
    ["openweathermap", "Open Weather Map"],
    ["Mr.", "mistyr"],
    ["Ms.", "misus"],
    ["Mrs.", "mizz"],
    ["Dr.", " doctor "],
    [" Mr ", " mistyr "],
    [" Ms ", " misus "],
    [" Mrs ", " mizz "],
    [" Dr ", "doctor"],
    ["Parch.", "parchedig"],
    ["Capt.", "capten"],
]


def replace_phrase(text):
    """
    Replace known phrases so as not to put normal numbers into the mix
    :param text:
    :return:
    """
    for item in black_list:
        if len(item) == 2:
            text = text.replace(item[0], item[1])
            text = text.replace(item[0].lower(), item[1].lower())
            text = text.replace(item[0].capitalize(), item[1].capitalize())
            text = text.replace(item[0].title(), item[1].title())
            text = text.replace(item[0].upper(), item[1].upper())
        else:
            print("Invalid text pair, you have {} items and should have 2", len(item))
    text = text.replace("  at", " at")
    return text.rstrip()
