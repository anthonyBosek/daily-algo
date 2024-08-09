"""
    840. Magic Squares In Grid
    https://leetcode.com/problems/magic-squares-in-grid/

    A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

    Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

    Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.

"""

from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagicSquare(grid, i, j):
            if grid[i + 1][j + 1] != 5:
                return False
            s = "".join(
                str(grid[i + x // 3][j + x % 3]) for x in [0, 1, 2, 5, 8, 7, 6, 3]
            )
            return s in "43816729" * 2 or s in "43816729"[::-1] * 2

        return sum(
            isMagicSquare(grid, i, j)
            for i in range(len(grid) - 2)
            for j in range(len(grid[0]) - 2)
        )


#! Approach 1: Manual Scan
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            for col in range(n - 2):
                if self._isMagicSquare(grid, row, col):
                    ans += 1
        return ans

    def _isMagicSquare(self, grid, row, col):
        seen = [False] * 10
        for i in range(3):
            for j in range(3):
                num = grid[row + i][col + j]
                if num < 1 or num > 9:
                    return False
                if seen[num]:
                    return False
                seen[num] = True

        # Check if diagonal sums are the same
        diagonal1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
        diagonal2 = grid[row + 2][col] + grid[row + 1][col + 1] + grid[row][col + 2]

        if diagonal1 != diagonal2:
            return False

        # Check if all row sums are the same as the diagonal sums
        row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
        row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
        row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]

        if not (row1 == diagonal1 and row2 == diagonal1 and row3 == diagonal1):
            return False

        # Check if all column sums are the same as the diagonal sums
        col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
        col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
        col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]

        if not (col1 == diagonal1 and col2 == diagonal1 and col3 == diagonal1):
            return False

        return True


#! Approach 2: Check Unique Properties of Magic Square
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ans = 0
        m = len(grid)
        n = len(grid[0])
        for row in range(m - 2):
            for col in range(n - 2):
                if self._isMagicSquare(grid, row, col):
                    ans += 1
        return ans

    def _isMagicSquare(self, grid, row, col):
        # The sequences are each repeated twice to account for
        # the different possible starting points of the sequence
        # in the magic square
        sequence = "2943816729438167"
        sequenceReversed = "7618349276183492"

        border = []
        # Flattened indices for bordering elements of 3x3 grid
        borderIndices = [0, 1, 2, 5, 8, 7, 6, 3]
        for i in borderIndices:
            num = grid[row + i // 3][col + (i % 3)]
            border.append(str(num))

        borderConverted = "".join(border)

        # Make sure the sequence starts at one of the corners
        return (
            grid[row][col] % 2 == 0
            and (
                sequence.find(borderConverted) != -1
                or sequenceReversed.find(borderConverted) != -1
            )
            and grid[row + 1][col + 1] == 5
        )
