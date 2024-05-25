"""
    402. Remove K Digits
    https://leetcode.com/problems/remove-k-digits/

    Given string num representing a non-negative integer num, and an integer k,
        return the smallest possible integer after removing k digits from num.

"""


def removeKdigits(num, k):
    if len(num) == k:
        return "0"

    stack = []

    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # If k is still greater than 0, remove remaining digits from the end
    while k > 0:
        stack.pop()
        k -= 1

    # Remove leading zeros
    while stack and stack[0] == "0":
        stack.pop(0)

    # If stack is empty, return "0"
    if not stack:
        return "0"

    return "".join(stack)

    # --------------------------------------------------------------------------------

    # stack = []
    # for digit in num:
    #     while k and stack and stack[-1] > digit:
    #         stack.pop()
    #         k -= 1
    #     stack.append(digit)
    # return "".join(stack[: -k or None]).lstrip("0") or "0"
