from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        numbers = [int(line) for line in fi]
        return [min(numbers), max(numbers)]
