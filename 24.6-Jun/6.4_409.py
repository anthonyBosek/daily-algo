"""
    409. Longest Palindrome
    https://leetcode.com/problems/longest-palindrome/

    Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

    Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

"""

from collections import Counter


def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    # ans = 0
    # count = Counter(s)
    # for c in count.values():
    #     ans += c if c % 2 == 0 else c - 1
    # has = any(c % 2 == 1 for c in count.values())
    # return ans + has

    #! ----------------------------------------------------

    # pair_counter = 0
    # chars = set()

    # for ch in s:
    #     if ch in chars:
    #         chars.remove(ch)
    #         pair_counter += 1

    #     else:
    #         chars.add(ch)

    # return pair_counter * 2 + (1 if len(chars) > 0 else 0)

    #! ----------------------------------------------------

    count = Counter(s)
    res = 0
    odd = 0
    for i in count:
        if count[i] % 2 == 0:
            res += count[i]
        else:
            res += count[i] - 1
            odd = 1
    return res + odd
