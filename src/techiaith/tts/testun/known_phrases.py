"""
Script to replace known phrases in text
"""
black_list = [
    ["golwg360", "golwg tri chwech dim"],
    ["s4c", "es pedwar ec"],
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
