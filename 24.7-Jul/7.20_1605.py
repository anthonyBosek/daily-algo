"""
    1605. Find Valid Matrix Given Row and Column Sums
    https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

    You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements
    in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you
    do not know the elements of the matrix, but you do know the sums of each row and column.

    Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum
    and colSum requirements.

    Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix
    that fulfills the requirements exists.

"""

from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        # m, n = len(rowSum), len(colSum)
        # res = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         res[i][j] = min(rowSum[i], colSum[j])
        #         rowSum[i] -= res[i][j]
        #         colSum[j] -= res[i][j]
        # return res

        # --------------------------------------------------------------------------------

        col_sum = colSum
        row_sum = rowSum

        mat = [[0] * len(col_sum) for i in range(len(row_sum))]
        i = 0
        j = 0
        while i < len(row_sum) and j < len(col_sum):
            mat[i][j] = min(row_sum[i], col_sum[j])
            if row_sum[i] == col_sum[j]:
                i += 1
                j += 1
            elif row_sum[i] > col_sum[j]:
                row_sum[i] -= col_sum[j]
                j += 1
            else:
                col_sum[j] -= row_sum[i]
                i += 1

        return mat


#! Approach 1: Greedy
class Solution:
    def restoreMatrix(self, rowSum, colSum):
        N = len(rowSum)
        M = len(colSum)

        curr_row_sum = [0] * N
        curr_col_sum = [0] * M

        orig_matrix = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                orig_matrix[i][j] = min(
                    rowSum[i] - curr_row_sum[i], colSum[j] - curr_col_sum[j]
                )

                curr_row_sum[i] += orig_matrix[i][j]
                curr_col_sum[j] += orig_matrix[i][j]

        return orig_matrix


#! Approach 2: Space Optimized Greedy
class Solution:
    def restoreMatrix(self, rowSum, colSum):
        N = len(rowSum)
        M = len(colSum)

        orig_matrix = [[0] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                orig_matrix[i][j] = min(rowSum[i], colSum[j])

                rowSum[i] -= orig_matrix[i][j]
                colSum[j] -= orig_matrix[i][j]

        return orig_matrix


#! Approach 3: Time + Space Optimized Greedy
class Solution:
    def restoreMatrix(self, rowSum, colSum):
        N = len(rowSum)
        M = len(colSum)

        orig_matrix = [[0] * M for _ in range(N)]
        i, j = 0, 0

        while i < N and j < M:
            orig_matrix[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= orig_matrix[i][j]
            colSum[j] -= orig_matrix[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1

        return orig_matrix
