"""
    647. Palindromic Substrings
    https://leetcode.com/problems/palindromic-substrings/

    Given a string s, return the number of palindromic substrings in it.

    A string is a palindrome when it reads the same backward as forward.

    A substring is a contiguous sequence of characters within the string.

"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            count += self.count_palindromic(s, i, i)
            count += self.count_palindromic(s, i, i + 1)
        return count

    def count_palindromic(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            count += 1
        return count


# ------------------------------------------------------------
# Solution 2
# def countSubstrings(self, s: str) -> int:
#     ans, n, i = 0, len(s), 0
#     while (i < n):
#         j, k = i - 1, i
#         while k < n - 1 and s[k] == s[k+1]: k += 1
#         ans += (k - j) * (k - j + 1) // 2
#         i, k = k + 1, k + 1
#         while ~j and k < n and s[k] == s[j]:
#             j, k, ans = j - 1, k + 1, ans + 1
#     return ans
