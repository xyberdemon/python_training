"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    list_of_longest = set()
    number_of_words = 10
    # read all words from file to list
    words = []
    with open(file_path, encoding="unicode_escape", errors="backslashreplace") as fi:
        for line in fi:
            inner_list = re.findall(r"[\w-]+", line)
            if len(inner_list) != 0:
                words.extend(inner_list)
    # remove word wrapping
    for each in words:
        if each[-1] == "-":
            words[words.index(each) + 1] = (
                words[words.index(each)][:-1] + words[words.index(each) + 1]
            )
            words.pop(words.index(each))
    # find the longest words
    while len(list_of_longest) < number_of_words:
        longest_word = max(words, key=len)
        list_of_longest.add(longest_word)
        words.pop(words.index(longest_word))
    return sorted(list_of_longest, key=len, reverse=True)


def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...


print(get_longest_diverse_words("../tests/data.txt"))
