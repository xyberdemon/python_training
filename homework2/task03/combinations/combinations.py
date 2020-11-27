"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List

# from itertools import product


# def combinations_check(*args: List[Any]) -> List[List]:
#     return list(product(*args))


def combinations(*args: List[Any]) -> List[List]:
    result = args[0]
    for each in args[1:]:
        temp_result = []
        for first in result:
            for second in each:
                temp_first = flatten(first)
                temp_first.append(second)
                temp_result.append(temp_first)
        result = temp_result
    return result


def flatten(value):
    if isinstance(value, List):
        return [x for x in value]
    else:
        temp_list = [value]
        return temp_list


# Tests
# print(combinations([1, 2], [3, 4], [5, 6]))
# print(combinations(['abc', 2], ['def', 4], [5, 6]))
