"""
    131. Palindrome Partitioning
    https://leetcode.com/problems/palindrome-partitioning/

    Given a string s, partition s such that every substring of the partition is a palindrome.
    
    Return all possible palindrome partitioning of s.

"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[0].append([])

        for i in range(n + 1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    for prev in dp[j]:
                        dp[i].append(prev + [s[j:i]])
        return dp[n]

    # ? --------------------------------------------------
    #
    # --- option 1 ---
    #
    #     result = []
    #     self.dfs(s, [], result)
    #     return result

    # def dfs(self, s, path, result):
    #     if not s:
    #         result.append(path)
    #         return
    #     for i in range(1, len(s) + 1):
    #         if self.is_palindrome(s[:i]):
    #             self.dfs(s[i:], path + [s[:i]], result)

    # def is_palindrome(self, s):
    #     return s == s[::-1]
