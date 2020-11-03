from typing import List

import pytest
from zeroTuples.findZeroTuples import check_sum_of_four


@pytest.mark.parametrize(
    ["list1", "list2", "list3", "list4", "expected_result"],
    [
        ([0, 1, 2, 3], [3, 4, 5, 9], [-3, 2, -4, 8], [1, 5, 0, 0], 7),
        ([0, 1, 2, 3], [3, 4, 5, -2], [6, 2, -10, -7], [1, 2, 3, 4], 15),
        ([0, 1, 2, 3], [3, 4, 5, 8], [6, 2, 9, 12], [1, 2, 3, 4], 0),
        ([0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [-1, -1, -1, -1], 256),
    ],
)
def test_find_min_and_max(
    list1: List[int],
    list2: List[int],
    list3: List[int],
    list4: List[int],
    expected_result: int,
):
    actual_result = check_sum_of_four(list1, list2, list3, list4)

    assert actual_result == expected_result
