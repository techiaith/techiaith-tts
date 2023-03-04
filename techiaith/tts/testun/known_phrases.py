def replace_phrase(text):
    for item in black_list:
        if len(item) == 2:
            text = text.replace(item[0], item[1])
        else:
            print("Invalid text pair, you have {} items and should have 2", len(item))
    return text


black_list = [
    ["golwg360", "golwg tri chwech ddim"],
    ["s4c", "es pedwar ec"],
    ["%", " y cant"]
]
