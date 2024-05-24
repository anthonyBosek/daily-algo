"""
    1544. Make The String Great
    https://leetcode.com/problems/make-the-string-great/

    Given a string s of lower and upper case English letters.

    A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

        - 0 <= i <= s.length - 2

        - s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.

    To make the string good, you can choose two adjacent characters that make the string bad and remove them.
        You can keep doing this until the string becomes good.

    Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

"""

from collections import deque


def makeGood(self, s: str) -> str:
    # n = len(s)
    # s = deque(s)
    # stk = []
    # while s:
    #     stk.append(s.popleft())
    #     if len(stk) >= 2 and (
    #         stk[-1] != stk[-2] and stk[-1].lower() == stk[-2].lower()
    #     ):
    #         stk[:] = stk[:-2]

    # return "".join(stk)

    # --------------------------------------------------

    stack = []
    for c in s:
        if stack and abs(ord(stack[-1]) - ord(c)) == 32:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
