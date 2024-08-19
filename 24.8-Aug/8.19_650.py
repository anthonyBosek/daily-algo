"""
    650. 2 Keys Keyboard
    https://leetcode.com/problems/2-keys-keyboard/

    There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

        • Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
        • Paste: You can paste the characters which are copied last time.

    Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

"""


def minSteps(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 0

    for i in range(2, n + 1):
        if n % i == 0:
            return i + minSteps(n // i)

    # #! ---------------------------------------------
    # if n == 1:
    #     return 0
    # currLen = 1
    # currCopy = 1
    # currOperations = 1

    # while currLen < n:
    #     if n % currLen == 0 and currLen != currCopy:
    #         currCopy = currLen

    #     else:
    #         currLen += currCopy

    #     currOperations += 1

    # return currOperations


# #! Editorial
# class Solution:

#     def __init__(self):
#         self.n = 0

#     def _min_steps_helper(self, curr_len, paste_len):
#         # base case: reached n A's, don't need more operations
#         if curr_len == self.n:
#             return 0
#         # base case: exceeded n `A`s, not a valid sequence, so
#         # return max value
#         if curr_len > self.n:
#             return 1000

#         # copy all + paste
#         opt1 = 2 + self._min_steps_helper(curr_len * 2, curr_len)
#         # paste
#         opt2 = 1 + self._min_steps_helper(curr_len + paste_len, paste_len)

#         return min(opt1, opt2)

#     def minSteps(self, n: int) -> int:
#         if n == 1:
#             return 0
#         self.n = n
#         # first step is always a Copy All operation
#         return 1 + self._min_steps_helper(1, 1)
