"""
    368. Largest Divisible Subset
    https://leetcode.com/problems/largest-divisible-subset/

    Given a set of distinct positive integers nums, return the largest subset answer such that every pair
        (answer[i], answer[j]) of elements in this subset satisfies:

        • answer[i] % answer[j] == 0, or
        • answer[j] % answer[i] == 0

    If there are multiple solutions, return any of them.

"""


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_len, max_idx = 1, 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > max_len:
                        max_len = dp[i]
                        max_idx = i

        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = prev[max_idx]

        return res

        # -------------------------------------------------------------------

        # if len(nums) == 0:
        #     return []

        # nums.sort()
        # dp = [1] * len(nums)
        # prev = [-1] * len(nums)
        # max_index = 0

        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[i] % nums[j] == 0:
        #             if dp[i] < dp[j] + 1:
        #                 dp[i] = dp[j] + 1
        #                 prev[i] = j
        #     if dp[i] > dp[max_index]:
        #         max_index = i

        # result = []
        # while max_index != -1:
        #     result.append(nums[max_index])
        #     max_index = prev[max_index]

        # return result

        # -------------------------------------------------------------------

        # nums.sort()
        # n = len(nums)
        # dp = [1] * n
        # prev = [-1] * n
        # max_len = 0
        # max_idx = -1

        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] % nums[j] == 0:
        #             if dp[i] < dp[j] + 1:
        #                 dp[i] = dp[j] + 1
        #                 prev[i] = j
        #     if dp[i] > max_len:
        #         max_len = dp[i]
        #         max_idx = i

        # res = []
        # while max_idx != -1:
        #     res.append(nums[max_idx])
        #     max_idx = prev[max_idx]

        # return res
