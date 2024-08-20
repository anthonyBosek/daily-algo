"""
    1140. Stone Game II
    https://leetcode.com/problems/stone-game-ii/

    Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row,
    and each pile has a positive integer number of stones piles[i].
    The objective of the game is to end with the most stones. 

    Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

    On each player's turn, that player can take all the stones in the first X remaining piles,
    where 1 <= X <= 2M.  Then, we set M = max(M, X).

    The game continues until all the stones have been taken.

    Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

"""

from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        suffix = [0] * n
        suffix[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        def dfs(i, m):
            if i == n:
                return 0
            if 2 * m >= n - i:
                return suffix[i]
            if dp[i][m]:
                return dp[i][m]
            res = 0
            for x in range(1, 2 * m + 1):
                res = max(res, suffix[i] - dfs(i + x, max(m, x)))
            dp[i][m] = res
            return res

        return dfs(0, 1)


#! Approach 1: Dynamic Programming (Memoization)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Initialize the memoization table
        memo = [[0] * len(piles) for _ in range(len(piles))]
        # Initialize the suffixSum array
        suffix_sum = piles[:]

        # Compute the suffix sums
        for i in range(len(suffix_sum) - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        # Call the recursive function to find the maximum stones Alex can collect
        return self.max_stones(suffix_sum, 1, 0, memo)

    def max_stones(
        self,
        suffix_sum: List[int],
        max_till_now: int,
        curr_index: int,
        memo: List[List[int]],
    ) -> int:
        # If the current index plus twice the maxTillNow exceeds the array size, take all remaining stones
        if curr_index + 2 * max_till_now >= len(suffix_sum):
            return suffix_sum[curr_index]

        # Return the memoized result if it exists
        if memo[curr_index][max_till_now] > 0:
            return memo[curr_index][max_till_now]

        # Initialize the result to a very large number (infinity)
        res = float("inf")

        # Iterate through possible moves and calculate the minimum result for the opponent
        for i in range(1, 2 * max_till_now + 1):
            res = min(
                res,
                self.max_stones(
                    suffix_sum,
                    max(i, max_till_now),
                    curr_index + i,
                    memo,
                ),
            )

        # Memoize the result as the current suffix sum minus the opponent's best outcome
        memo[curr_index][max_till_now] = suffix_sum[curr_index] - res
        return memo[curr_index][max_till_now]


#! Approach 2: Dynamic Programming (Tabulation)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

        # Store suffix sum for all possible suffix
        suffix_sum = [0 for _ in range(length + 1)]
        for i in range(length - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Initialize the dp array.
        for i in range(length + 1):
            dp[i][length] = suffix_sum[i]

        # Start from the last index to store the future state first.
        for index in range(length - 1, -1, -1):
            for max_till_now in range(length - 1, 0, -1):
                for X in range(1, min(2 * max_till_now, length - index) + 1):
                    dp[index][max_till_now] = max(
                        dp[index][max_till_now],
                        suffix_sum[index] - dp[index + X][max(max_till_now, X)],
                    )
        return dp[0][1]
