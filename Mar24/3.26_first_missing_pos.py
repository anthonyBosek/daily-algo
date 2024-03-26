"""
    41. First Missing Positive
    https://leetcode.com/problems/first-missing-positive/

    Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

    You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                return i
        return i + 1

        # ----------------------------------------------------------

        # n = len(nums)
        # for i in range(n):
        #     while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        #         nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # for i in range(n):
        #     if nums[i] != i + 1:
        #         return i + 1

        # return n + 1
