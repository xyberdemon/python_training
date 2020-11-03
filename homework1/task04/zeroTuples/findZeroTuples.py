from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    result = 0
    sums = {}
    for x in a:
        for y in b:
            if x + y not in sums:
                sums[x + y] = 1
            else:
                sums[x + y] += 1
    for i in c:
        for j in d:
            if -1 * (i + j) in sums:
                result += sums[-1 * (i + j)]
    return result
