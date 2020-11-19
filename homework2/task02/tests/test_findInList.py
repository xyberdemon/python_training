from typing import List, Tuple

import pytest
from mostAndLeastCommon.findInList import major_and_minor_elem


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [([3, 3, 3, 3, 2, 2, 1, 0], (3, 0)), ([324, 53, 123, 54, 324], (324, 54))],
)
def test_major_and_minor_elem(value: List, expected_result: Tuple[int, int]):
    actual_result = major_and_minor_elem(value)
    assert actual_result == expected_result
