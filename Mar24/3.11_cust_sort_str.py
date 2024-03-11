"""
    791. Custom Sort String
    https://leetcode.com/problems/custom-sort-string/

    You are given two strings order and s. All the characters of order are unique
        and were sorted in some custom order previously.

    Permute the characters of s so that they match the order that order was sorted.
        More specifically, if a character x occurs before a character y in order,
        then x should occur before y in the permuted string.

    Return any permutation of s that satisfies this property.

"""

# def customSortString(order, s):

from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)

        res = ""
        for c in order:
            if c in counter:
                newStr = counter[c] * c
                res += newStr
                del counter[c]

        for k, v in counter.items():
            newStr = k * v
            res += newStr

        return res

        # ---------------------------------------------------------------

        # # Create a dictionary to store the count of each character in s
        # count = {}
        # for c in s:
        #     if c in count:
        #         count[c] += 1
        #     else:
        #         count[c] = 1

        # # Create a string to store the result
        # result = ""

        # # Iterate through the characters in order
        # for c in order:
        #     if c in count:
        #         result += c * count[c]
        #         count.pop(c)

        # # Add the remaining characters in s to the result
        # for c in count:
        #     result += c * count[c]

        # return result
