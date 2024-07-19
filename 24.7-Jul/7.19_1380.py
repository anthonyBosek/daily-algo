"""
    1380. Lucky Numbers in a Matrix
    https://leetcode.com/problems/lucky-numbers-in-a-matrix/

    Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

    A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

"""


def luckyNumbers(matrix):
    row_min = [min(row) for row in matrix]
    col_max = [max(col) for col in zip(*matrix)]
    return list(set(row_min) & set(col_max))


#! Approach 1: Simulation
class Solution:
    def luckyNumbers(self, matrix):
        N = len(matrix)
        M = len(matrix[0])

        rowMin = []
        for i in range(N):
            rMin = float("inf")
            for j in range(M):
                rMin = min(rMin, matrix[i][j])
            rowMin.append(rMin)

        colMax = []
        for i in range(M):
            cMax = float("-inf")
            for j in range(N):
                cMax = max(cMax, matrix[j][i])
            colMax.append(cMax)

        luckyNumbers = []
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    luckyNumbers.append(matrix[i][j])

        return luckyNumbers


#! Approach 2: Greedy
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        N, M = len(matrix), len(matrix[0])

        r_min_max = float("-inf")
        for i in range(N):
            r_min = min(matrix[i])
            r_min_max = max(r_min_max, r_min)

        c_max_min = float("inf")
        for i in range(M):
            c_max = max(matrix[j][i] for j in range(N))
            c_max_min = min(c_max_min, c_max)

        if r_min_max == c_max_min:
            return [r_min_max]
        else:
            return []
