"""
    1863. Sum of All Subset XOR Totals
    https://leetcode.com/problems/sum-of-all-subset-xor-totals/

    The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

        - For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.

    Given an array nums, return the sum of all XOR totals for every subset of nums. 

    Note: Subsets with the same elements should be counted multiple times.

    An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.

"""

from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        pass
        # res = 0
        # for num in nums:
        #     res |= num
        # return res * (1 << (len(nums) - 1))

        # ------------------------------------------------------------------------

        # def dfs(i: int, xors: int) -> int:
        #     if i == len(nums):
        #         return xors
        #     x = dfs(i + 1, xors)
        #     y = dfs(i + 1, nums[i] ^ xors)
        #     return x + y

        # return dfs(0, 0)

        # ------------------------------------------------------------------------

        # def backtrack(start, subset_xor):
        #     nonlocal total_xor
        #     total_xor += subset_xor
        #     for i in range(start, len(nums)):
        #         backtrack(i + 1, subset_xor ^ nums[i])

        # total_xor = 0
        # backtrack(0, 0)
        # return total_xor

        # ------------------------------------------------------------------------

        # def xor_sum(nums, i, xor):
        #     if i == len(nums):
        #         return xor
        #     return xor_sum(nums, i + 1, xor) + xor_sum(nums, i + 1, xor ^ nums[i])

        # return xor_sum(nums, 0, 0)
