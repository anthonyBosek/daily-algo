"""
    2486. Append Characters to String to Make Subsequence
    https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

    You are given two strings s and t consisting of only lowercase English letters.

    Return the minimum number of characters that need to be appended to the end
    of s so that t becomes a subsequence of s.

    A subsequence is a string that can be derived from another string by deleting
    some or no characters without changing the order of the remaining characters.

"""


def appendCharacters(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    it = iter(s)
    matching_count = sum(1 for char in t if char in it)
    return len(t) - matching_count

    #! -------------------------------------------------

    # i = 0
    # j = 0
    # n = len(s)
    # m = len(t)
    # while i < n and j < m:
    #     if s[i] == t[j]:
    #         j += 1
    #     i += 1
    # return m - j
