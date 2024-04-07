"""
    678. Valid Parenthesis String
    https://leetcode.com/problems/valid-parenthesis-string/

    Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

    The following rules define a valid string:

    - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    - Any right parenthesis ')' must have a corresponding left parenthesis '('.
    - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

"""


def checkValidString(s):
    """
    :type s: str
    :rtype: bool
    """
    # The idea is to keep track of the minimum and maximum number of open left brackets
    # that must be present in the string to make it valid.
    # If the maximum number of open left brackets falls below 0, then the string is invalid.
    # If the minimum number of open left brackets is not 0, then the string is invalid.
    # The minimum and maximum number of open left brackets are updated as follows:
    # - If we encounter a left bracket, then the minimum and maximum number of open left brackets are incremented by 1.
    # - If we encounter a right bracket, then the minimum and maximum number of open left brackets are decremented by 1.
    # - If we encounter a star, then the minimum number of open left brackets is decremented by 1,
    #   and the maximum number of open left brackets is incremented by 1.
    # If the maximum number of open left brackets falls below 0, then the string is invalid.
    # If the minimum number of open left brackets is not 0, then the string is invalid.
    # If the string is valid, then the minimum number of open left brackets will be 0.

    min_open = 0
    max_open = 0

    for c in s:
        if c == "(":
            min_open += 1
            max_open += 1
        elif c == ")":
            min_open = max(min_open - 1, 0)
            max_open -= 1
        else:
            min_open = max(min_open - 1, 0)
            max_open += 1

        if max_open < 0:
            return False

    return min_open == 0

    # -------------------------------------------------

    # stack = []
    # star = []
    # for idx, char in enumerate(s):
    #     if char == '(':
    #         stack.append(idx)
    #     elif char == ')':
    #         if stack:
    #             stack.pop()
    #         elif star:
    #             star.pop()
    #         else:
    #             return False
    #     else:
    #         star.append(idx)
    # while stack and star:
    #     if stack[-1] > star[-1]:
    #         return False

    #     stack.pop()
    #     star.pop()

    # return len(stack) == 0

    # -------------------------------------------------
    # --- best solution ---

    # leftMin, leftMax = 0, 0

    # for char in s:
    #     if char == "(":
    #         leftMin, leftMax = leftMin + 1, leftMax + 1
    #     elif char == ")":
    #         leftMin, leftMax = leftMin - 1, leftMax - 1
    #     else:
    #         leftMin, leftMax = leftMin - 1, leftMax + 1
    #     if leftMax < 0:
    #         return False
    #     if leftMin < 0:
    #         leftMin = 0
    # return leftMin == 0
