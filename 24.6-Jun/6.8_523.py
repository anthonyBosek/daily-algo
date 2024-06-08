"""
    523. Continuous Subarray Sum
    https://leetcode.com/problems/continuous-subarray-sum/

    Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

    A good subarray is a subarray where:

        • its length is at least two, and
        • the sum of the elements of the subarray is a multiple of k.

    Note that:

        • A subarray is a contiguous part of the array.
        • An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

"""

from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_cache = {0: -1}
        remainder = 0
        for i in range(len(nums)):
            remainder += nums[i]
            remainder %= k
            if remainder not in remainder_cache:
                remainder_cache[remainder] = i
            elif i - remainder_cache[remainder] >= 2:
                return True
        return False

        # ----------------------------------------------------------

        # sum_map = {0: -1}
        # sum = 0
        # for i in range(len(nums)):
        #     sum += nums[i]
        #     if k != 0:
        #         sum = sum % k
        #     if sum in sum_map:
        #         if i - sum_map[sum] > 1:
        #             return True
        #     else:
        #         sum_map[sum] = i
        # return False
