"""
    1137. N-th Tribonacci Number
    https://leetcode.com/problems/n-th-tribonacci-number/

    The Tribonacci sequence Tn is defined as follows:
    
    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

    Given n, return the value of Tn.

"""


class Solution:
    def tribonacci(self, n: int) -> int:
        # if n <= 1:
        #     return n
        # if n == 2:
        #     return 1
        # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        # ------------------------------

        l1 = [0, 1, 1]

        if len(l1) <= n:
            while len(l1) <= n:
                l1.append(l1[-1] + l1[-2] + l1[-3])

        return l1[n]

        # ------------------------------

        # if n < 3:
        #     return 1 if n else 0
        # a, b, c = 0, 1, 1
        # for _ in range(n - 2):
        #     a, b, c = b, c, a+b+c
        # return c

        # ------------------------------

        # if n == 0:
        #     return 0
        # if n == 1 or n == 2:
        #     return 1
        # a, b, c = 0, 1, 1
        # for _ in range(3, n+1):
        #     a, b, c = b, c, a+b+c
        # return c
