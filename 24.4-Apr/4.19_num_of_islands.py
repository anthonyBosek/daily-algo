"""
    200. Number of Islands
    https://leetcode.com/problems/number-of-islands/

    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
    
    You may assume all four edges of the grid are all surrounded by water.

"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        number_of_islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    number_of_islands += 1

        return number_of_islands

        # -------------------------------------------------------------------------------------

        # def dfs(grid, i, j):
        #     if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
        #         return
        #     grid[i][j] = "0"
        #     dfs(grid, i + 1, j)
        #     dfs(grid, i - 1, j)
        #     dfs(grid, i, j + 1)
        #     dfs(grid, i, j - 1)

        # count = 0
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if grid[i][j] == "1":
        #             count += 1
        #             dfs(grid, i, j)
        # return count
