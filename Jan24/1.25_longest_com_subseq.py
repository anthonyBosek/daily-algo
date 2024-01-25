"""
    1143. Longest Common Subsequence
    https://leetcode.com/problems/longest-common-subsequence/

    Given two strings text1 and text2, return the length of their longest common subsequence.
    If there is no common subsequence, return 0.

    A subsequence of a string is a new string generated from the original string with some characters
    (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

    A common subsequence of two strings is a subsequence that is common to both strings.

"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Time Complexity: O(m*n)
        Space Complexity: O(m*n)
        """
        m = len(text1)
        n = len(text2)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        return dp[m][n]

    # -----------------------------------------------------------------------------------------------

    # """
    #     Time Complexity: O(m*n)
    #     Space Complexity: O(m*n)
    # """
    # m = len(text1)
    # n = len(text2)

    # dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # for i in range(1, m+1):
    #     for j in range(1, n+1):

    #         if text1[i-1] == text2[j-1]:
    #             # if same, add 1 to the diagonal value
    #             dp[i][j] = 1 + dp[i-1][j-1]
    #         else:
    #             # if not same, take max of left and top value
    #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # return dp[m][n]
