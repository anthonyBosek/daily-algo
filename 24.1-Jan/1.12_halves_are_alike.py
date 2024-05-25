"""
    1704. Determine if String Halves Are Alike
    https://leetcode.com/problems/determine-if-string-halves-are-alike/

    You are given a string s of even length. Split this string into two halves of equal lengths,
        and let a be the first half and b be the second half.
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # other solution
        vowels = set("aeiouAEIOU")
        l = len(s)
        count = 0
        for i in range(l):
            if s[i] in vowels:
                if i < l // 2:
                    count += 1
                else:
                    count -= 1
        return count == 0

        # my solution
        # l = s.lower()
        # vwls = set('aeiou')
        # h = len(l) // 2
        # x = l[h:]
        # y = l[:h]
        # x_cnt = 0
        # y_cnt = 0
        # for i in range(h):
        #     if x[i] in vwls:
        #         x_cnt += 1
        #     if y[i] in vwls:
        #         y_cnt += 1

        # return x_cnt == y_cnt

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
