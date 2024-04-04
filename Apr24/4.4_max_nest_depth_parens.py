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
        res = 0
        depth = 0
        for c in s:
            if c == "(":
                depth += 1
                res = max(res, depth)
            elif c == ")":
                depth -= 1
        return res

        # ------------------------------------------

        # count=0
        # max1 =0
        # for i in s:
        #     if i == '(':
        #         count+=1
        #         if count > max1:
        #             max1 = count
        #     if i == ')':
        #         count-=1
        # return max1

        # ------------------------------------------

        # max_depth = 0
        # depth = 0
        # for c in s:
        #     if c == '(':
        #         depth += 1
        #         max_depth = max(max_depth, depth)
        #     elif c == ')':
        #         depth -= 1
        # return max_depth
