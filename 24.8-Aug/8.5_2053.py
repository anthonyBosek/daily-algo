"""
    2053. Kth Distinct String in an Array
    https://leetcode.com/problems/kth-distinct-string-in-an-array/

    A distinct string is a string that is present only once in an array.

    Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
    If there are fewer than k distinct strings, return an empty string "".

    Note that the strings are considered in the order in which they appear in the array.

"""

from collections import Counter


#! --- My Solution ---
def kthDistinct(arr, k):
    """
    :type arr: List[str]
    :type k: int
    :rtype: str
    """
    c = Counter(arr)
    a = 1
    for key, val in c.items():
        if val == 1:
            if a == k:
                return key
            else:
                a += 1
    return ""


#! Approach: Hash Map
class Solution:
    def kthDistinct(self, arr, k):
        frequency_map = {}

        # First pass: Populate the frequency map
        for s in arr:
            frequency_map[s] = frequency_map.get(s, 0) + 1

        # Second pass: Find the k-th distinct string
        for s in arr:
            # Check if the current string is distinct
            if frequency_map[s] == 1:
                k -= 1
            # When k reaches 0, we have found the k-th distinct string
            if k == 0:
                return s

        return ""
