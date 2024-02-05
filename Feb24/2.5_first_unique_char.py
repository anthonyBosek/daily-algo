"""
    387. First Unique Character in a String
    https://leetcode.com/problems/first-unique-character-in-a-string/

    Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a Counter object to store the frequency of each character
        freq = Counter(s)

        # Iterate through the string and check the frequency of each character
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        return -1

        # -----------------------------------------------------

        # n = len(s)

        # # Iterate through each character in the string
        # for i in range(n):
        #     count = 0

        #     # Check for duplicates before the current index
        #     for k in range(0, i):
        #         if s[i] == s[k]:
        #             count = 1
        #             break

        #     # If no duplicates before, check after the current index
        #     if count == 0:
        #         for j in range(i + 1, n):
        #             if s[i] == s[j]:
        #                 count = 1
        #                 break

        #     # If no duplicates found, return the current index
        #     if count == 0:
        #         return i

        # # If no unique character is found, return -1
        # return -1

        # -----------------------------------------------------

        # # Create a dictionary to store the frequency of each character
        # freq = {}
        # for char in s:
        #     if char in freq:
        #         freq[char] += 1
        #     else:
        #         freq[char] = 1

        # # Iterate through the string and check the frequency of each character
        # for i in range(len(s)):
        #     if freq[s[i]] == 1:
        #         return i
        # return -1
