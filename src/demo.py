"""
Normaliser demo
"""
from techiaith.tts.testun.normaliser import parse_text


def _parse_user_input():
    msg = """
◊---------------------------------◊
|  Normaliser Demo Normaleiddiwr  |
◊---------------------------------◊
| Teipiwch 'exit' i cau'r prompt. |
| Type 'exit' to quit the prompt. |
◊---------------------------------◊
    """
    print(msg)
    while True:
        text = input("\nprompt: ")
        clean_text = parse_text(text)
        print("\nresult: ", clean_text)
        if clean_text == "exit":
            break


if __name__ == "__main__":
    _parse_user_input()

