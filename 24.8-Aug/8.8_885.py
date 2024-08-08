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
        path = [[rStart, cStart]]
        steps = 1
        r, c = rStart, cStart
        while len(path) < rows * cols:
            for _ in range(steps):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    path.append([r, c])
            for _ in range(steps):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    path.append([r, c])
            steps += 1
            for _ in range(steps):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    path.append([r, c])
            for _ in range(steps):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    path.append([r, c])
            steps += 1
        return path


#! Approach 1: Simulation
class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        # Store all possible directions in an array.
        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        traversed = []

        # Initial step size is 1, value of d represents the current direction.
        step = 1
        direction = 0
        while len(traversed) < rows * cols:
            # direction = 0 -> East, direction = 1 -> South
            # direction = 2 -> West, direction = 3 -> North
            for _ in range(2):
                for _ in range(step):
                    # Validate the current position
                    if rStart >= 0 and rStart < rows and cStart >= 0 and cStart < cols:
                        traversed.append([rStart, cStart])
                    # Make changes to the current position.
                    rStart += dir[direction][0]
                    cStart += dir[direction][1]

                direction = (direction + 1) % 4
            step += 1
        return traversed


#! Another Approach
class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        output = [[rStart, cStart]]
        r = rStart
        c = cStart
        total = rows * cols
        i = 1
        count = 1
        while True:
            # dn = ['e','s','w','n']
            # move to east
            for _ in range(i):
                c += 1
                if r >= 0 and r < rows and c >= 0 and c < cols:
                    output.append([r, c])
                    count += 1
            if count == total:
                break

            # move to south
            for _ in range(i):
                r += 1
                if r >= 0 and r < rows and c >= 0 and c < cols:
                    output.append([r, c])
                    count += 1
            if count == total:
                break

            # move to west
            for _ in range(i + 1):
                c -= 1
                if r >= 0 and r < rows and c >= 0 and c < cols:
                    output.append([r, c])
                    count += 1
            if count == total:
                break

            # move to north
            for _ in range(i + 1):
                r -= 1
                if r >= 0 and r < rows and c >= 0 and c < cols:
                    output.append([r, c])
                    count += 1
            if count == total:
                break

            i += 2
        return output
