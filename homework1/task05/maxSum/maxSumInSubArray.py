from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    sum_of_sub_arrays = []
    while len(nums) - k + 1:
        temp_sum = 0
        for i in range(k):
            temp_sum += nums[i]
        sum_of_sub_arrays.append(temp_sum)
        nums = nums[1:]
    return max(sum_of_sub_arrays)
