"""
    1404. Number of Steps to Reduce a Number in Binary Representation to One
    https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/

    Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

        • If the current number is even, you have to divide it by 2.

        • If the current number is odd, you have to add 1 to it.

    It is guaranteed that you can always reach one for all test cases.

"""


class Solution:
    def numSteps(self, s: str) -> int:
        return len(s) + s.rstrip("0").count("0") + 2 * (s.count("1") != 1) - 1

        # -----------------------------------

        # n = int(s, 2)
        # a = 0
        # while n > 1:
        #     if n & 1:
        #         n += 1
        #     else:
        #         n //= 2
        #     a += 1
        # return a

        # -----------------------------------

        # n = int(s, 2)
        # steps = 0
        # while n != 1:
        #     if n % 2 == 0:
        #         n //= 2
        #     else:
        #         n += 1
        #     steps += 1
        # return steps
