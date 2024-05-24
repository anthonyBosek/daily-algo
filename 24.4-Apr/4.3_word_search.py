"""
    79. Word Search
    https://leetcode.com/problems/word-search/

    Given an m x n grid of characters board and a string word, return true if word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
        or vertically neighboring. The same letter cell may not be used more than once.

"""

from collections import Counter


def exist(board, word):
    # ------ leaderboard ------
    R = len(board)
    C = len(board[0])

    if len(word) > R * C:
        return False

    count = Counter(sum(board, []))

    for c, countWord in Counter(word).items():
        if count[c] < countWord:
            return False

    if count[word[0]] > count[word[-1]]:
        word = word[::-1]

    seen = set()

    def dfs(r, c, i):
        if i == len(word):
            return True
        if (
            r < 0
            or c < 0
            or r >= R
            or c >= C
            or word[i] != board[r][c]
            or (r, c) in seen
        ):
            return False

        seen.add((r, c))
        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )
        seen.remove((r, c))  # backtracking

        return res

    for i in range(R):
        for j in range(C):
            if dfs(i, j, 0):
                return True
    return False

    # -----------------------------------------------------------------------------------------------------
    # -------- copilot ----------

    # def dfs(i, j, k):
    #     if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
    #         return False
    #     if k == len(word) - 1:
    #         return True
    #     tmp, board[i][j] = board[i][j], '/'
    #     res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
    #     board[i][j] = tmp
    #     return res

    # for i in range(len(board)):
    #     for j in range(len(board[0])):
    #         if dfs(i, j, 0):
    #             return True
    # return False
