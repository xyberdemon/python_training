from typing import Any, List

import pytest
from combinations.combinations import combinations

# Tests don't work
# test_combinations: in "parametrize" the number of names (2):
#   ['value', 'expected_result']
# must be equal to the number of values (4):


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (
            [1, 2],
            [3, 4],
            [5, 6],
            [
                [1, 3, 5],
                [1, 3, 6],
                [1, 4, 5],
                [1, 4, 6],
                [2, 3, 5],
                [2, 3, 6],
                [2, 4, 5],
                [2, 4, 6],
            ],
        ),
        (
            ["abc", 2],
            ["def", 4],
            [5, 6],
            [
                ["abc", "def", 5],
                ["abc", "def", 6],
                ["abc", 4, 5],
                ["abc", 4, 6],
                [2, "def", 5],
                [2, "def", 6],
                [2, 4, 5],
                [2, 4, 6],
            ],
        ),
    ],
)
def test_combinations(value: List[Any], expected_result: List[List]):
    actual_result = combinations(value)
    assert actual_result == expected_result
