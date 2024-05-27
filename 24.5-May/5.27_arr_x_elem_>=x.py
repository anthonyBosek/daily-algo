"""
    1608. Special Array With X Elements Greater Than or Equal X
    https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

    You are given an array nums of non-negative integers. nums is considered special if there exists
    a number x such that there are exactly x numbers in nums that are greater than or equal to x.

    Notice that x does not have to be an element in nums.

    Return x if the array is special, otherwise, return -1. It can be proven that if nums is special,
    the value for x is unique.

"""

from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # nums.sort()
        # n = len(nums)

        # for x in range(1, n + 1):
        #     count = 0
        #     for num in nums:
        #         if num >= x:
        #             count += 1
        #     if count == x:
        #         return x
        # return -1

        # ? ----------------------------------------------------------------------

        # N = len(nums)

        # freq = [0] * (N + 1)
        # for num in nums:
        #     freq[min(N, num)] += 1

        # num_greater_than_or_equal = 0
        # for i in range(N, 0, -1):
        #     num_greater_than_or_equal += freq[i]
        #     if i == num_greater_than_or_equal:
        #         return i

        # return -1

        # ? ----------------------------------------------------------------------

        nums.sort(reverse=True)
        for i in range(len(nums)):
            if nums[i] >= i + 1 and (i == len(nums) - 1 or nums[i + 1] < i + 1):
                return i + 1
        return -1
