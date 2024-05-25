"""
    58. Length of Last Word
    https://leetcode.com/problems/length-of-last-word/

    Given a string s consisting of words and spaces, return the length of the last word in the string.

    A word is a maximal substring consisting of non-space characters only.

"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if res > 0:
                    break
            else:
                res += 1

        return res

        # -------------------------------------

        # return len(s.strip().split()[-1])
