"""
Test known_phrases
"""
from techiaith.tts.testun.known_phrases import replace_phrase

# ERAILL POSIB: S4C ("es pedwar ec")
tests = [
    ["gwefan yw golwg360", "gwefan yw golwg tri chwech dim"],
    ["S4C", "es pedwar ec"],
    ["@S4C", " at es pedwar ec"],
]


def test_replace_phrase():
    for text in tests:
        result = replace_phrase(text[0])
        assert text[1] == result
