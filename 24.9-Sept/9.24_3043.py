"""
    3043. Find the Length of the Longest Common Prefix
    https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

    You are given two arrays with positive integers arr1 and arr2.

    A prefix of a positive integer is an integer formed by one or more of its digits,
    starting from its leftmost digit. For example, 123 is a prefix of the integer 12345,
    while 234 is not.

    A common prefix of two integers a and b is an integer c, such that c is a prefix of both a and b.
    For example, 5655359 and 56554 have a common prefix 565 while 1223 and 43456 do not have a common prefix.

    You need to find the length of the longest common prefix between all pairs of integers (x, y)
    such that x belongs to arr1 and y belongs to arr2.

    Return the length of the longest common prefix among all pairs. If no common prefix exists among them, return 0.

"""

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()
        for elem in arr2:
            while elem > 0:
                prefixes.add(elem)
                elem //= 10

        result = 0
        for elem in arr1:
            while elem > result:
                if elem in prefixes:
                    result = max(result, elem)
                    break
                else:
                    elem //= 10

        if result == 0:
            return 0
        return len(str(result))


#! Approach 1: Using Hash Table
class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        arr1_prefixes = set()  # Set to store all prefixes from arr1

        # Step 1: Build all possible prefixes from arr1
        for val in arr1:
            while val not in arr1_prefixes and val > 0:
                # Insert current value as a prefix
                arr1_prefixes.add(val)
                # Generate the next shorter prefix by removing the last digit
                val //= 10

        longest_prefix = 0

        # Step 2: Check each number in arr2 for the longest matching prefix
        for val in arr2:
            while val not in arr1_prefixes and val > 0:
                # Reduce val by removing the last digit if not found in the prefix set
                val //= 10
            if val > 0:
                # Length of the matched prefix using log10 to determine the number of digits
                longest_prefix = max(longest_prefix, len(str(val)))

        return longest_prefix


#! Approach 2: Trie
class TrieNode:
    def __init__(self):
        # Each node has up to 10 possible children (digits 0-9)
        self.children = [None] * 10


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a number into the Trie by treating it as a string of digits
    def insert(self, num):
        node = self.root
        num_str = str(num)
        for digit in num_str:
            idx = int(digit)
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]

    # Find the longest common prefix for a number in arr2 with the Trie
    def find_longest_prefix(self, num):
        node = self.root
        num_str = str(num)
        len = 0

        for digit in num_str:
            idx = int(digit)
            if node.children[idx]:
                # Increase length if the current digit matches
                len += 1
                node = node.children[idx]
            else:
                # Stop if no match for the current digit
                break
        return len


class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        trie = Trie()

        # Step 1: Insert all numbers from arr1 into the Trie
        for num in arr1:
            trie.insert(num)

        longest_prefix = 0

        # Step 2: Find the longest prefix match for each number in arr2
        for num in arr2:
            len = trie.find_longest_prefix(num)
            longest_prefix = max(longest_prefix, len)

        return longest_prefix
