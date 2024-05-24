"""
    231. Power of Two
    https://leetcode.com/problems/power-of-two/

    Given an integer n, return true if it is a power of two. Otherwise, return false.

    An integer n is a power of two, if there exists an integer x such that n == 2^x.
    
"""

from math import log


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return (n != 0) and (n & (n-1) == 0)

        # ------------------------------------

        # if n <= 0:
        #     return False
        # return n & (n - 1) == 0

        # ------------------------------------

        # for i in range(31):
        #     if 2 ** i == n:
        #         return True
        # return False

        # ------------------------------------

        if not n > 0:
            return False
        x = int(log(n, 2))
        return pow(2, x) == n
