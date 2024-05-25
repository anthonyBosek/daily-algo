"""
    1249. Minimum Remove to Make Valid Parentheses
    https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

    Given a string s of '(' , ')' and lowercase English characters.

    Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
        parentheses string is valid and return any valid string.

    Formally, a parentheses string is valid if and only if:
        - It is the empty string, contains only lowercase characters, or
        - It can be written as AB (A concatenated with B), where A and B are valid strings, or
        - It can be written as (A), where A is a valid string.

"""

from typing import List


def minRemoveToMakeValid(s):
    stack: List[int] = []
    result: List[str] = []
    for c in s:
        if c == "(":
            stack.append(len(result))
            result.append(c)
        elif c == ")":
            if stack:
                stack.pop()
                result.append(c)
        else:
            result.append(c)

    for i in stack:
        result[i] = ""

    return "".join(result)

    # ---------------------------------------------------------

    # stack = []
    # s = list(s)
    # for i, c in enumerate(s):
    #     if c == '(':
    #         stack.append(i)
    #     elif c == ')':
    #         if stack:
    #             stack.pop()
    #         else:
    #             s[i] = ''
    # for i in stack:
    #     s[i] = ''
    # return ''.join(s)
