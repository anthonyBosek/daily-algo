"""
    1289. Minimum Falling Path Sum II
    https://leetcode.com/problems/minimum-falling-path-sum-ii/

    Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

    A falling path with non-zero shifts is a choice of exactly one element from each row of grid such
        that no two elements chosen in adjacent rows are in the same column.

"""

from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        DP = grid[0]

        for i in range(1, N):
            indx1 = DP.index(min(DP))
            indx2 = DP.index(min(DP[:indx1] + DP[indx1 + 1 :]))
            for j in range(N):
                if j != indx1:
                    grid[i][j] += DP[indx1]
                else:
                    grid[i][j] += DP[indx2]
            DP = grid[i]

        return min(DP)

        # -----------------------------------------------------------------------

        # n = len(grid)
        # dp = [[0] * n for _ in range(n)]
        # dp[0] = grid[0]

        # for i in range(1, n):
        #     min1 = min(dp[i - 1])
        #     min1_idx = dp[i - 1].index(min1)
        #     min2 = min(dp[i - 1][:min1_idx] + dp[i - 1][min1_idx + 1 :])
        #     for j in range(n):
        #         dp[i][j] = grid[i][j] + (min1 if j != min1_idx else min2)

        # return min(dp[-1])

        # -----------------------------------------------------------------------

        # n = len(grid)
        # dp = [[0] * n for _ in range(n)]
        # for i in range(n):
        #     dp[0][i] = grid[0][i]

        # for i in range(1, n):
        #     for j in range(n):
        #         dp[i][j] = grid[i][j] + min(dp[i - 1][:j] + dp[i - 1][j + 1 :])

        # return min(dp[-1])
