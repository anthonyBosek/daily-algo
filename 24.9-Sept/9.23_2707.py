"""
    2707. Extra Characters in a String
    https://leetcode.com/problems/extra-characters-in-a-string/

    You are given a 0-indexed string s and a dictionary of words dictionary.
    You have to break s into one or more non-overlapping substrings such that each substring
    is present in dictionary. There may be some extra characters in s which are not present
    in any of the substrings.

    Return the minimum number of extra characters left over if you break up s optimally.

"""


def minExtraChar(s, dictionary):
    """
    :type s: str
    :type dictionary: List[str]
    :rtype: int
    """
    n = len(s)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + 1
        for word in dictionary:
            if i >= len(word) and s[i - len(word) : i] == word:
                dp[i] = min(dp[i], dp[i - len(word)])
    return dp[n]

    # ? faster approach
    # tree = {}
    # for word in dictionary:
    #     curr = tree
    #     for c in word:
    #         curr = curr.setdefault(c, {})
    #     curr['*'] = word

    # dp = [0] * (len(s) + 1)
    # for i in range(len(s) - 1, -1, -1):
    #     dp[i] = dp[i + 1] + 1
    #     curr = tree
    #     j = i
    #     while j < len(s) and s[j] in curr:
    #         curr = curr[s[j]]
    #         if '*' in curr:
    #             dp[i] = min(dp[i], dp[j + 1])
    #         j += 1
    # return dp[0]


#! Approach 1: Top Down Dynamic Programming with Substring Method
from typing import List
from functools import cache


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, dictionary_set = len(s), set(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0
            # To count this character as a left over character
            # move to index 'start + 1'
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start : end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
            return ans

        return dp(0)


#! Approach 2: Bottom Up Dynamic Programming with Substring Method
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (len(s) + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start : end + 1]
                if curr in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]


#! Approach 3: Top Down Dynamic Programming with Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = self.buildTrie(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0
            # To count this character as a left over character
            # move to index 'start + 1'
            ans = dp(start + 1) + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    ans = min(ans, dp(end + 1))
            return ans

        return dp(0)

    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
        return root


#! Approach 4: Bottom Up Dynamic Programming with Trie
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = self.buildTrie(dictionary)
        dp = [0] * (n + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = dp[start + 1] + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]

    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
        return root
