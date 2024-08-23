"""
    592. Fraction Addition and Subtraction
    https://leetcode.com/problems/fraction-addition-and-subtraction/

    Given a string expression representing an expression of fraction addition and subtraction,
    return the calculation result in string format.

    The final result should be an irreducible fraction. If your final result is an integer,
    change it to the format of a fraction that has a denominator 1.
    So in this case, 2 should be converted to 2/1.

"""


class Solution:
    def fractionAddition(self, expression):
        num = 0
        denom = 1

        i = 0
        while i < len(expression):
            curr_num = 0
            curr_denom = 0

            is_negative = False

            # check for sign
            if expression[i] == "-" or expression[i] == "+":
                if expression[i] == "-":
                    is_negative = True
                # move to next character
                i += 1

            # build numerator
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                curr_num = curr_num * 10 + val
                i += 1

            if is_negative:
                curr_num *= -1

            # skip divisor
            i += 1

            # build denominator
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                curr_denom = curr_denom * 10 + val
                i += 1

            # add fractions together using common denominator
            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

        gcd = abs(self._find_gcd(num, denom))

        # reduce fractions
        num //= gcd
        denom //= gcd

        return f"{num}/{denom}"

    def _find_gcd(self, a, b):
        if a == 0:
            return b
        return self._find_gcd(b % a, a)


#! Approach 1: Manual Parsing + Common Denominator
class Solution:
    def fractionAddition(self, expression):
        num = 0
        denom = 1

        i = 0
        while i < len(expression):
            curr_num = 0
            curr_denom = 0

            is_negative = False

            # check for sign
            if expression[i] == "-" or expression[i] == "+":
                if expression[i] == "-":
                    is_negative = True
                # move to next character
                i += 1

            # build numerator
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                curr_num = curr_num * 10 + val
                i += 1

            if is_negative:
                curr_num *= -1

            # skip divisor
            i += 1

            # build denominator
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                curr_denom = curr_denom * 10 + val
                i += 1

            # add fractions together using common denominator
            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

        gcd = abs(self._find_gcd(num, denom))

        # reduce fractions
        num //= gcd
        denom //= gcd

        return f"{num}/{denom}"

    def _find_gcd(self, a, b):
        if a == 0:
            return b
        return self._find_gcd(b % a, a)


#! Approach 2 - Parsing with Regular Expressions
import re


class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        denom = 1

        # separate expression into signed numbers
        nums = re.split("/|(?=[-+])", expression)
        nums = list(filter(None, nums))

        for i in range(0, len(nums), 2):
            curr_num = int(nums[i])
            curr_denom = int(nums[i + 1])

            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

        gcd = abs(self._find_gcd(num, denom))

        num //= gcd
        denom //= gcd

        return str(num) + "/" + str(denom)

    def _find_gcd(self, a: int, b: int) -> int:
        if a == 0:
            return b
        return self._find_gcd(b % a, a)
