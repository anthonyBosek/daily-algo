"""
    1945. Sum of Digits of String After Convert
    https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

    You are given a string s consisting of lowercase English letters, and an integer k.

    First, convert s into an integer by replacing each letter with its position in the alphabet (i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26). Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k times in total.

    For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

        • Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
        • Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
        • Transform #2: 17 ➝ 1 + 7 ➝ 8

    Return the resulting integer after performing the operations described above.

"""


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = "".join([str(ord(c) - 96) for c in s])
        for _ in range(k):
            s = str(sum([int(c) for c in s]))
        return int(s)


#!Approach 1: String Concatenation to Summation
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert each character to its numerical value and build a string
        numeric_string = ""
        for ch in s:
            numeric_string += str(ord(ch) - ord("a") + 1)

        # Apply digit sum transformations k times
        while k > 0:
            digit_sum = 0
            for digit in numeric_string:
                digit_sum += int(digit)
            numeric_string = str(digit_sum)
            k -= 1

        # Convert the final string to integer and return
        return int(numeric_string)


#! Approach 2: Direct Integer Operation
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert the string to a number by summing digit values
        current_number = 0
        for ch in s:
            position = ord(ch) - ord("a") + 1
            while position > 0:
                current_number += position % 10
                position //= 10

        # Apply digit sum transformations k-1 times
        for i in range(1, k):
            digit_sum = 0
            while current_number > 0:
                digit_sum += current_number % 10
                current_number //= 10
            current_number = digit_sum

        return current_number
