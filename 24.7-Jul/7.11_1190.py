"""
    1190. Reverse Substrings Between Each Pair of Parentheses
    https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

    You are given a string s that consists of lower case English letters and brackets.

    Reverse the strings in each pair of matching parentheses, starting from the innermost one.

    Your result should not contain any brackets.

"""


def reverseParentheses(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    for i in s:
        if i == ")":
            temp = ""
            while stack[-1] != "(":
                temp += stack.pop()
            stack.pop()
            for j in temp:
                stack.append(j)
        else:
            stack.append(i)
    return "".join(stack)

    #! ------------------------------
    # sub = list(s)
    # i = len(sub) - 1
    # while "(" in sub:
    #     if sub[i] == "(":
    #         for j in range(i, len(sub)):
    #             if sub[j] == ")":
    #                 sub[i + 1 : j] = sub[i + 1 : j][::-1]
    #                 sub.pop(j)
    #                 sub.pop(i)
    #                 break
    #     i -= 1
    # return "".join(sub)


#!Approach 1: Straightforward Way
class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_parentheses_indices = deque()
        result = []

        for current_char in s:
            if current_char == "(":
                # Store the current length as the start index
                # for future reversal
                open_parentheses_indices.append(len(result))
            elif current_char == ")":
                start = open_parentheses_indices.pop()
                # Reverse the substring between the matching parentheses
                result[start:] = result[start:][::-1]
            else:
                # Append non-parenthesis characters to the processed list
                result.append(current_char)
        return "".join(result)


#! Approach 2: Wormhole Teleportation technique
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices = []
        pair = [0] * n

        # First pass: Pair up parentheses
        for i in range(n):
            if s[i] == "(":
                open_parentheses_indices.append(i)
            if s[i] == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i

        # Second pass: Build the result string
        result = []
        curr_index = 0
        direction = 1

        while curr_index < n:
            if s[curr_index] == "(" or s[curr_index] == ")":
                curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            curr_index += direction

        return "".join(result)
