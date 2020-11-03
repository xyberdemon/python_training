from typing import Tuple

import pytest
from minMaxInFile.findMinMax import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ("testData01.txt", [-123, 756]),
        ("testData02.txt", [6, 987]),
    ],
)
def test_find_min_and_max(value: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(value)

    assert actual_result == expected_result
