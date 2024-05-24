"""
    861. Score After Flipping Matrix
    https://leetcode.com/problems/score-after-flipping-matrix/

    You are given an m x n binary matrix grid.

    A move consists of choosing any row or column and toggling each value in that row or column
        (i.e., changing all 0's to 1's, and all 1's to 0's).

    Every row of the matrix is interpreted as a binary number, and the score of the matrix is
        the sum of these numbers.

    Return the highest possible score after making any number of moves (including zero moves).

"""

from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # Set score to summation of first column
        score = (1 << (n - 1)) * m

        # Loop over all other columns
        for j in range(1, n):
            count_same_bits = 0
            for i in range(m):
                # Count elements matching first in row
                if grid[i][j] == grid[i][0]:
                    count_same_bits += 1

            # Calculate score based on the number of same bits in a column
            count_same_bits = max(count_same_bits, m - count_same_bits)
            # Calculate the score contribution for the current column
            column_score = (1 << (n - j - 1)) * count_same_bits
            # Add contribution to score
            score += column_score

        return score

        # -----------------------------------------------------------

        # m = len(grid)
        # n = len(grid[0])

        # for i in range(m):
        #     if grid[i][0] == 0:  # Toggle the entire row if it starts with 0.
        #         grid[i] = [1 - x for x in grid[i]]

        # for j in range(1, n):  # Start from the second column as the first column is already toggled.
        #     count_1 = sum(grid[i][j] for i in range(m))
        #     if count_1 < m - count_1:  # Toggle the entire column if there are more zeros than ones.
        #         for i in range(m):
        #             grid[i][j] = 1 - grid[i][j]

        # Sum = 0
        # for row in grid:
        #     Bin = ''.join(map(str, row))
        #     dec = int(Bin, 2)
        #     Sum += dec
        # return Sum

        # -----------------------------------------------------------

        # rows,cols = len(grid),len(grid[0])
        # for r in range(rows):
        #     if grid[r][0] == 0:
        #         for c in range(cols):
        #             if grid[r][c] == 0:
        #                 grid[r][c] = 1
        #             else:
        #                 grid[r][c] = 0

        # counts = collections.defaultdict(int)
        # for c in range(1,cols):
        #     for r in range(rows):
        #         if grid[r][c] == 0:
        #             counts[c] += 1

        # res = rows * (2**(cols-1))
        # for c in range(1,cols):
        #     res += max(counts[c],rows - counts[c])*2**(cols - c - 1)

        # return res

        # -----------------------------------------------------------

        # m, n = len(grid), len(grid[0])
        # for i in range(m):
        #     if grid[i][0] == 0:
        #         for j in range(n):
        #             grid[i][j] = 1 - grid[i][j]

        # for j in range(1, n):
        #     count = sum(grid[i][j] for i in range(m))
        #     if count < m - count:
        #         for i in range(m):
        #             grid[i][j] = 1 - grid[i][j]

        # return sum(int("".join(map(str, row)), 2) for row in grid)
