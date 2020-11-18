from collections.abc import Sequence

import pytest
from findInFile.findInFile import *


def test_get_longest_diverse_words():
    actual_result = get_longest_diverse_words("../tests/data.txt")
    for each in actual_result:
        assert each in [
            "politisch-strategischen",
            "Verfassungsverletzungen",
            "symbolischsakramentale",
            "Mehrheitsvorstellungen",
            "Souveränitätsansprüche",
            "Wiederbelebungsübungen",
            "zoologisch-politischen",
            "Geschichtsphilosophie",
            "Menschheitsgeschichte",
            "Werkstättenlandschaft",
        ]


def test_get_rarest_char():
    actual_result = get_rarest_char("../tests/data.txt")
    for each in actual_result:
        assert each in ["›", "‹", "Y", "î", "’", "X", "(", ")"]


def test_count_punctuation_chars():
    actual_result = count_punctuation_chars("../tests/data.txt")
    assert actual_result == 5308
