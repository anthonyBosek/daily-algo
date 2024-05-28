"""
    1208. Get Equal Substrings Within Budget
    https://leetcode.com/problems/get-equal-substrings-within-budget/

    You are given two strings s and t of the same length and an integer maxCost.

    You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]|
    (i.e., the absolute difference between the ASCII values of the characters).

    Return the maximum length of a substring of s that can be changed to be the same as the corresponding
    substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be
    changed to its corresponding substring from t, return 0.

"""

from collections import deque


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost_q = deque(maxlen=len(s))
        result = 0
        for c1, c2 in zip(s, t):
            c = abs(ord(c1) - ord(c2))
            maxCost -= c
            cost_q.append(c)
            while maxCost < 0:
                maxCost += cost_q.popleft()
            if len(cost_q) > result:
                result = len(cost_q)
        return result

        # --------------------------------------------------------

        # cost = lambda i: abs(ord(s[i]) - ord(t[i]))

        # i = 0
        # for j in range(len(s)):
        #     maxCost -= cost(j)
        #     if maxCost < 0:
        #         maxCost += cost(i)
        #         i += 1

        # return j - i + 1

        # --------------------------------------------------------

        # n = len(s)
        # cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        # i = 0
        # j = 0
        # max_len = 0
        # while j < n:
        #     maxCost -= cost[j]
        #     while maxCost < 0:
        #         maxCost += cost[i]
        #         i += 1
        #     max_len = max(max_len, j - i + 1)
        #     j += 1
        # return max_len
