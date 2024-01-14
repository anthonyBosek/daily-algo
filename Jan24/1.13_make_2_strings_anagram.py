"""
    1347. Minimum Number of Steps to Make Two Strings Anagram
    https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

    Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.
    Return the minimum number of steps to make t an anagram of s.
    An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

"""


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # count_s = [0] * 26
        # count_t = [0] * 26

        # for char in s:
        #     count_s[ord(char) - ord("a")] += 1

        # for char in t:
        #     count_t[ord(char) - ord("a")] += 1

        # steps = 0
        # for i in range(26):
        #     steps += abs(count_s[i] - count_t[i])

        # return steps // 2

        smp = {}
        tmp = {}
        cnt = 0

        for a in s:
            smp[a] = smp.get(a, 0) + 1

        for a in t:
            tmp[a] = tmp.get(a, 0) + 1

        for key, value in smp.items():
            if key in tmp:
                if value == tmp[key]:
                    cnt += value
                else:
                    cnt += min(value, tmp[key])

        return len(s) - cnt
