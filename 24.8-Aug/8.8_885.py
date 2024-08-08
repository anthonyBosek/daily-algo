"""
    885. Spiral Matrix III
    https://leetcode.com/problems/spiral-matrix-iii/

    You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner
    is at the first row and column in the grid, and the southeast corner is at the last row and column.

    You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move
    outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.).
    Eventually, we reach all rows * cols spaces of the grid.

    Return an array of coordinates representing the positions of the grid in the order you visited them.

"""

from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        pass
