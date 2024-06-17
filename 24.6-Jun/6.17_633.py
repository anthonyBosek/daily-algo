"""
    633. Sum of Square Numbers
    https://leetcode.com/problems/sum-of-square-numbers/

    Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.

"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # #? --- Option 1 ---
        i = 2
        while i * i <= c:
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c //= i
                if count % 2 and i % 4 == 3:
                    return False
            i += 1
        return c % 4 != 3
        #! -----------------------------------
        # #? --- Option 2 ---
        # i, j = 0, int(math.sqrt(c))
        # while i <= j:
        #     sum1 = i * i + j * j
        #     if sum1 == c:
        #         return True
        #     elif sum1 > c:
        #         j -= 1
        #     else:
        #         i += 1
        # return False
        #
        # #? --- same but different ---
        # m = int(math.sqrt(c))
        # l, r = 0, m
        # while l <= r:
        #     s = l * l + r * r
        #     if s == c:
        #         return True
        #     elif s < c:
        #         l += 1
        #     else:
        #         r -= 1
        # return False
        #! -----------------------------------
        # #? --- Option 3 ---
        # if c == 0:
        #     return True

        # for i in range(1, int(c**0.5) + 1):
        #     if (c - i**2) ** 0.5 % 1 == 0:
        #         return True

        # return False
