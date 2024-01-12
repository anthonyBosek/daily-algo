"""
    1704. Determine if String Halves Are Alike
    https://leetcode.com/problems/determine-if-string-halves-are-alike/

    You are given a string s of even length. Split this string into two halves of equal lengths,
        and let a be the first half and b be the second half.
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        pass

        # copilot solution
        # vowels = set("aeiouAEIOU")
        # a = s[: len(s) // 2]
        # b = s[len(s) // 2 :]
        # a_count = 0
        # b_count = 0
        # for i in range(len(a)):
        #     if a[i] in vowels:
        #         a_count += 1
        #     if b[i] in vowels:
        #         b_count += 1
        # return a_count == b_count
