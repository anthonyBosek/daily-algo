"""
    1463. Cherry Pickup II
    https://leetcode.com/problems/cherry-pickup-ii/

    You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

    You have two robots that can collect cherries for you:

        • Robot #1 is located at the top-left corner (0, 0), and
        • Robot #2 is located at the top-right corner (0, cols - 1).

    Return the maximum number of cherries collection using both robots by following the rules below:

    From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
        • When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
        • When both robots stay in the same cell, only one takes the cherries.
        • Both robots cannot move outside of the grid at any moment.
        • Both robots should reach the bottom row in grid.

"""


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        #     m, n = len(grid), len(grid[0])
        #     dp = [[[-1] * n for _ in range(n)] for _ in range(m)]
        #     return self.dfs(grid, 0, 0, n - 1, dp)

        # def dfs(self, grid, r, c1, c2, dp):
        #     if r == len(grid):
        #         return 0
        #     if dp[r][c1][c2] != -1:
        #         return dp[r][c1][c2]
        #     res = 0
        #     for i in range(-1, 2):
        #         for j in range(-1, 2):
        #             nc1, nc2 = c1 + i, c2 + j
        #             if 0 <= nc1 < len(grid[0]) and 0 <= nc2 < len(grid[0]):
        #                 res = max(res, self.dfs(grid, r + 1, nc1, nc2, dp))
        #     cherries = grid[r][c1] + (c1 != c2) * grid[r][c2]
        #     res += cherries
        #     dp[r][c1][c2] = res
        #     return res

        # -------------------------------------------------------------------

        m, n = len(grid), len(grid[0])
        if n == 2:
            return sum(sum(g) for g in grid)
        elif n == 3:
            return sum(sum(g) - min(g) for g in grid)

        prev, dirs = [[0] * n for _ in range(n)], {
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 0),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        }
        for i in range(m - 1, -1, -1):
            cur = [[0] * n for _ in range(n)]
            for j in range(min(i + 1, n)):
                for k in range(max(j, n - i - 1), n):
                    for dir in dirs:
                        s, t = j + dir[0], k + dir[1]
                        if 0 <= s <= t < n and cur[j][k] < prev[s][t]:
                            cur[j][k] = prev[s][t]
                    cur[j][k] += grid[i][j] + (0 if j == k else grid[i][k])
            prev = cur
        return prev[0][-1]
