from typing import List

import pytest
from maxSum.maxSumInSubArray import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "length", "expected_result"],
    [
        ([0, 1, 2, 3, 4, 5], 3, 12),
        ([0, 5, 4, 3, 2, 1], 2, 9),
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([1, 2, 3], 3, 6),
    ],
)
def test_find_min_and_max(value: List[int], length: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(value, length)

    assert actual_result == expected_result
