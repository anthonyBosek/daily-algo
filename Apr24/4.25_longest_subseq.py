"""
    2370. Longest Ideal Subsequence
    https://leetcode.com/problems/longest-ideal-subsequence/

    You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

        - t is a subsequence of the string s.
        - The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.

    Return the length of the longest ideal string.

    A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

    Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

"""

from typing import List


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # dp[i] := the longest subsequence that ends in ('a' + i)
        dp = [0] * 26

        for c in s:
            i = ord(c) - ord("a")
            dp[i] = 1 + self._getMaxReachable(dp, i, k)

        return max(dp)

    def _getMaxReachable(self, dp: List[int], i: int, k: int) -> int:
        first = max(0, i - k)
        last = min(25, i + k)
        maxReachable = 0
        for j in range(first, last + 1):
            maxReachable = max(maxReachable, dp[j])
        return maxReachable

    # ---------------------------------------------------------------------

    # l = [0] * 128
    # for c in s:
    #     i = ord(c)
    #     l[i] = max(l[i - k : i + k + 1]) + 1
    # return max(l)
