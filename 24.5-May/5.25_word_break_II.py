"""
    140. Word Break II
    https://leetcode.com/problems/word-break-ii/

    Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence
        where each word is a valid dictionary word. Return all such possible sentences in any order.

    Note that the same word in the dictionary may be reused multiple times in the segmentation.

"""

from typing import List

# from collections import defaultdict
# from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        n = len(s)
        dp = [None] * (n + 1)
        dp[0] = [""]
        for i in range(1, n + 1):
            dp[i] = []
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    for sentence in dp[j]:
                        dp[i].append((sentence + " " + s[j:i]).strip())
        return dp[n]

        # ? ---------------------------------------------------------------

        # wordSet = set(wordDict)
        # # table to map a string to its corresponding words break
        # # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
        # memo = defaultdict(list)

        # # @lru_cache(maxsize=None)    # alternative memoization solution
        # def _wordBreak_topdown(s):
        #     """return list of word lists"""
        #     if not s:
        #         return [[]]  # list of empty list

        #     if s in memo:
        #         # returned the cached solution directly.
        #         return memo[s]

        #     for endIndex in range(1, len(s) + 1):
        #         word = s[:endIndex]
        #         if word in wordSet:
        #             # move forwards to break the postfix into words
        #             for subsentence in _wordBreak_topdown(s[endIndex:]):
        #                 memo[s].append([word] + subsentence)
        #     return memo[s]

        # # break the input string into lists of words list
        # _wordBreak_topdown(s)

        # # chain up the lists of words into sentences.
        # return [" ".join(words) for words in memo[s]]
