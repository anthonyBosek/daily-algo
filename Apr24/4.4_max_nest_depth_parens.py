"""
    1614. Maximum Nesting Depth of the Parentheses
    https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

    A string is a valid parentheses string (denoted VPS) if it meets one of the following:
        - It is an empty string "", or a single character not equal to "(" or ")",
        - It can be written as AB (A concatenated with B), where A and B are VPS's, or
        - It can be written as (A), where A is a VPS.

    We can similarly define the nesting depth depth(S) of any VPS S as follows:
        - depth("") = 0
        - depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
        - depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
        - depth("(" + A + ")") = 1 + depth(A), where A is a VPS.

"""


class Solution:
    def maxDepth(self, s: str) -> int:
        pass
