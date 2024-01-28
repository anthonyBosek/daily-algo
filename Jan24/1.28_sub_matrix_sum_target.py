"""
    1074. Number of Submatrices That Sum to Target
    https://leetcode.com/problems/number-of-submatrices-that-sum-to-target

    Given a matrix and a target, return the number of non-empty submatrices that sum to target.

    A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

    Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

"""


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

        # Compute the 2D prefix sum
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum[i][j] = (
                    matrix[i - 1][j - 1]
                    + prefix_sum[i - 1][j]
                    + prefix_sum[i][j - 1]
                    - prefix_sum[i - 1][j - 1]
                )

        count = 0

        # Iterate through all possible pairs of columns
        for col1 in range(1, cols + 1):
            for col2 in range(col1, cols + 1):
                # Use a hashmap to count the number of subarrays with a given sum
                prefix_sum_map = {0: 1}
                current_sum = 0
                for row in range(1, rows + 1):
                    current_sum = prefix_sum[row][col2] - prefix_sum[row][col1 - 1]
                    if current_sum - target in prefix_sum_map:
                        count += prefix_sum_map[current_sum - target]
                    if current_sum in prefix_sum_map:
                        prefix_sum_map[current_sum] += 1
                    else:
                        prefix_sum_map[current_sum] = 1

        return count

    # ------------------------------------------------------------------------------
    #     """
    #     Brute force: O(n^4)
    #     1. Calculate the sum of all submatrices
    #     2. Count the number of submatrices that sum to target
    #     """
    #     m, n = len(matrix), len(matrix[0])
    #     prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
    #     for i in range(m):
    #         for j in range(n):
    #             prefix_sum[i + 1][j + 1] = (
    #                 prefix_sum[i][j + 1]
    #                 + prefix_sum[i + 1][j]
    #                 - prefix_sum[i][j]
    #                 + matrix[i][j]
    #             )

    #     count = 0
    #     for i in range(m):
    #         for j in range(n):
    #             for k in range(i, m):
    #                 for l in range(j, n):
    #                     if (
    #                         prefix_sum[k + 1][l + 1]
    #                         - prefix_sum[i][l + 1]
    #                         - prefix_sum[k + 1][j]
    #                         + prefix_sum[i][j]
    #                         == target
    #                     ):
    #                         count += 1
    #     return count

    # def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    #     """
    #     Optimized brute force: O(n^3)
    #     1. Calculate the sum of all submatrices
    #     2. Count the number of submatrices that sum to target
    #     """
    #     m, n = len(matrix), len(matrix[0])
    #     prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
    #     for i in range(m):
    #         for j in range(n):
    #             prefix_sum[i + 1][j + 1] = (
    #                 prefix_sum[i][j + 1]
    #                 + prefix_sum[i + 1][j]
    #                 - prefix_sum[i][j]
    #                 + matrix[i][j]
    #             )

    #     count = 0
    #     for i in range(m):
    #         for j in range(i, m):
    #             for k in range(n):
    #                 for l in range(k, n):
    #                     if (
    #                         prefix_sum[j + 1][l + 1]
    #                         - prefix_sum[i][l + 1]
    #                         - prefix_sum[j + 1][k]
    #                         + prefix_sum[i][k]
    #                         == target
    #                     ):
    #                         count += 1
    #     return count

    # def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
    #     """
    #     Optimized brute force: O(n^3)
    #     1. Calculate the sum of all submatrices
    #     2. Count the number of submatrices that sum to target
    #     """
    #     m, n = len(matrix), len(matrix[0])
    #     prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
    #     for i in range(m):
    #         for j in range(n):
    #             prefix_sum[i + 1][j + 1] = (
    #                 prefix_sum[i][j + 1]
    #                 + prefix_sum[i + 1][j]
    #                 - prefix_sum[i][j]
    #                 + matrix[i][j]
    #             )

    #     count = 0
    #     for i in range(m):
    #         for j in range(i, m):
    #             dic = collections.defaultdict(int)
    #             for k in range(n):
    #                 cur = prefix_sum[j + 1][k + 1] - prefix_sum[i][k + 1]
    #                 if cur == target:
    #                     count += 1
    #                 count += dic[cur - target]
    #                 dic[cur] += 1
    #     return count
