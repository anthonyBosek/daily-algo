"""
    2373. Largest Local Values in a Matrix
    https://leetcode.com/problems/largest-local-values-in-a-matrix/

    You are given an n x n integer matrix grid.

    Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

        • maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid
            centered around row i + 1 and column j + 1.

    In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

    Return the generated matrix.

"""


def largestLocal(grid):
    """
    :type grid: List[List[int]]
    :rtype: List[List[int]]
    """
    n = len(grid)
    ans = []
    for i in range(n - 2):
        res = []
        for j in range(n - 2):
            maximum = max(
                grid[i][j],
                grid[i][j + 1],
                grid[i][j + 2],
                grid[i + 1][j],
                grid[i + 1][j + 1],
                grid[i + 1][j + 2],
                grid[i + 2][j],
                grid[i + 2][j + 1],
                grid[i + 2][j + 2],
            )
            res.append(maximum)
        ans.append(res)
    return ans

    # -----------------------------------------------------------------

    # n = len(grid)
    # res = []
    # for i in range(1, n - 1):
    #     row = []
    #     for j in range(1, n - 1):
    #         sub = [
    #             grid[i - 1][j - 1],
    #             grid[i - 1][j],
    #             grid[i - 1][j + 1],
    #             grid[i][j - 1],
    #             grid[i][j],
    #             grid[i][j + 1],
    #             grid[i + 1][j - 1],
    #             grid[i + 1][j],
    #             grid[i + 1][j + 1],
    #         ]
    #         row.append(max(sub))
    #     res.append(row)
    # return res

    # -----------------------------------------------------------------

    # n = len(grid)
    # maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

    # for i in range(1, n - 1):
    #     for j in range(1, n - 1):
    #         maxLocal[i - 1][j - 1] = max(
    #             grid[i - 1][j - 1],
    #             grid[i - 1][j],
    #             grid[i - 1][j + 1],
    #             grid[i][j - 1],
    #             grid[i][j],
    #             grid[i][j + 1],
    #             grid[i + 1][j - 1],
    #             grid[i + 1][j],
    #             grid[i + 1][j + 1],
    #         )

    # return maxLocal
