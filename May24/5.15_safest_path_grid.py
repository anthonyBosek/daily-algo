"""
    2812. Find the Safest Path in a Grid
    https://leetcode.com/problems/find-the-safest-path-in-a-grid/

    You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

        • A cell containing a thief if grid[r][c] = 1
        • An empty cell if grid[r][c] = 0

    You are initially positioned at cell (0, 0). In one move, you can move to any
        adjacent cell in the grid, including cells containing thieves.

    The safeness factor of a path on the grid is defined as the minimum manhattan
        distance from any cell in the path to any thief in the grid.

    Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

    An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1),
        (r + 1, c) and (r - 1, c) if it exists.

    The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|,
        where |val| denotes the absolute value of val.

"""

from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        pass
