"""
    1937. Maximum Number of Points with Cost
    https://leetcode.com/problems/maximum-number-of-points-with-cost/

    You are given an m x n integer matrix points (0-indexed). Starting with 0 points,
    you want to maximize the number of points you can get from the matrix.

    To gain points, you must pick one cell in each row. Picking the cell at coordinates
    (r, c) will add points[r][c] to your score.

    However, you will lose points if you pick a cell too far from the cell that you picked
    in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1),
    picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

    Return the maximum number of points you can achieve.

"""

from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        dp = points[0]
        for i in range(1, m):
            left = [0] * n
            right = [0] * n
            left[0] = dp[0]
            right[-1] = dp[-1]
            for j in range(1, n):
                left[j] = max(left[j - 1] - 1, dp[j])
            for j in range(n - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, dp[j])
            for j in range(n):
                dp[j] = points[i][j] + max(left[j], right[j])
        return max(dp)


#! Approach 1: Dynamic Programming
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        previous_row = points[0]

        for row in range(1, rows):
            left_max = [0] * cols
            right_max = [0] * cols
            current_row = [0] * cols

            # Calculate left-to-right maximum
            left_max[0] = previous_row[0]
            for col in range(1, cols):
                left_max[col] = max(left_max[col - 1] - 1, previous_row[col])

            # Calculate right-to-left maximum
            right_max[-1] = previous_row[-1]
            for col in range(cols - 2, -1, -1):
                right_max[col] = max(right_max[col + 1] - 1, previous_row[col])

            # Calculate the current row's maximum points
            for col in range(cols):
                current_row[col] = points[row][col] + max(left_max[col], right_max[col])

            # Update previous_row for the next iteration
            previous_row = current_row

        # Find the maximum value in the last processed row
        return max(previous_row)


#! Approach 2: Dynamic Programming (Optimized)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        cols = len(points[0])
        current_row = [0] * cols
        previous_row = [0] * cols

        for row in points:
            # running_max holds the maximum value generated in the previous iteration of each loop
            running_max = 0

            # Left to right pass
            for col in range(cols):
                running_max = max(running_max - 1, previous_row[col])
                current_row[col] = running_max

            running_max = 0
            # Right to left pass
            for col in range(cols - 1, -1, -1):
                running_max = max(running_max - 1, previous_row[col])
                current_row[col] = max(current_row[col], running_max) + row[col]

            # Update previous_row for next iteration
            previous_row = current_row.copy()

        # Find maximum points in the last row
        return max(previous_row)


#! Fast
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = [0] * n
        for i in range(m):
            newDp = [0] * n
            for j in range(n):
                point = points[i][j]
                if i > 0:
                    point += dp[j]
                if j > 0:
                    if point > newDp[j - 1] - 1:
                        k = j
                        while k >= 0 and newDp[k] < point:
                            newDp[k] = point
                            k -= 1
                            point -= 1
                    else:
                        newDp[j] = newDp[j - 1] - 1
                else:
                    newDp[j] = point
            dp = newDp
        return max(dp)
