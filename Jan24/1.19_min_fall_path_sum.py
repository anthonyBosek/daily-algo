"""
    931. Minimum Falling Path Sum
    https://leetcode.com/problems/minimum-falling-path-sum/

    Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

    A falling path starts at any element in the first row and chooses the element in the next row that is
        either directly below or diagonally left/right. Specifically, the next element from position
        (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

"""


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        """
        T(n) = O(n^2) -- traversed all elements in matrix
        S(n) = O(1) -- no extra space used
        """
        if not matrix:
            return 0
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                if j == 0:
                    matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j + 1])
                elif j == n - 1:
                    matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j - 1])
                else:
                    matrix[i][j] += min(
                        matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i - 1][j + 1]
                    )
        return min(matrix[-1])

        # -----------------------------------------------------------------------------

        # n = len(matrix)
        # m = len(matrix[0])
        # dp = [[0] * m for _ in range(n)]

        # for j in range(m):
        #     dp[0][j] = matrix[0][j]

        # for i in range(1, n):
        #     for j in range(m):
        #         ld = rd = float('inf')
        #         up = matrix[i][j] + dp[i - 1][j]

        #         if j - 1 >= 0:
        #             ld = matrix[i][j] + dp[i - 1][j - 1]
        #         if j + 1 < m:
        #             rd = matrix[i][j] + dp[i - 1][j + 1]

        #         dp[i][j] = min(up, min(ld, rd))

        # mini = dp[n - 1][0]
        # for j in range(1, m):
        #     mini = min(mini, dp[n - 1][j])
        # return mini
