"""
    78. Subsets
    https://leetcode.com/problems/subsets/

    Given an integer array nums of unique elements, return all possible subsets (the power set).

    The solution set must not contain duplicate subsets. Return the solution in any order.

"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for binary in range(2**n, 2 ** (n + 1)):
            char = str(bin(binary))[3:]
            local_res = []
            for index, ch in enumerate(char):
                if ch == "1":
                    local_res.append(nums[index])
            res.append(local_res)
        return res

        # ? -----------------------------------------------------------

        # res = []
        # subset = []

        # def returnsub(i):
        #     if len(nums) == i:
        #         res.append(subset[:])
        #         return
        #     subset.append(nums[i])
        #     returnsub(i + 1)
        #     subset.pop()
        #     returnsub(i + 1)

        # returnsub(0)
        # return res

        # ? -----------------------------------------------------------

        # result = []
        # self.backtrack(nums, [], result, 0)
        # return result

    # def backtrack(self, nums, path, result, start):
    #     result.append(path)
    #     for i in range(start, len(nums)):
    #         self.backtrack(nums, path + [nums[i]], result, i + 1)
