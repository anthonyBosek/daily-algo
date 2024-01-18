"""
    70. Climbing Stairs
    https://leetcode.com/problems/climbing-stairs/

    You are climbing a stair case. It takes n steps to reach to the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?

"""


class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        if 0 < n < 3:
            return n

        # Recursive - Top Dowm (memoization)
        if n not in memo:
            memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)
        return memo[n]

        # Iterative - Bottom Up (tabulation)
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        # Super Fancy
        # one, two = 1, 1
        # for i in range(n-1):
        #     temp = one
        #     one = one + two
        #     two = temp
        # return one
