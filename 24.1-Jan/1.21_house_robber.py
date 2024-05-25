"""
    198. House Robber
    https://leetcode.com/problems/house-robber/

    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed, the only constraint
    stopping you from robbing each of them is that adjacent houses have
    security system connected and it will automatically contact the police
    if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money
    of each house, determine the maximum amount of money you can rob tonight
    without alerting the police.

"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        # """
        #     Time Complexity: O(n)
        #     Space Complexity: O(1)
        # """
        # if not nums:
        #     return 0

        # prev1 = 0
        # prev2 = 0

        # for num in nums:
        #     temp = prev1
        #     prev1 = max(prev2 + num, prev1)
        #     prev2 = temp

        # return prev1

        # ---------------------------------------------------------

        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not nums:
            return 0

        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[-1]
