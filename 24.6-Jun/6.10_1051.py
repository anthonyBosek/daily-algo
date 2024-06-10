"""
    1051. Height Checker
    https://leetcode.com/problems/height-checker/

    A school is trying to take an annual photo of all the students. The students are asked to stand in a
    single file line in non-decreasing order by height. Let this ordering be represented by the integer
    array expected where expected[i] is the expected height of the ith student in line.

    You are given an integer array heights representing the current order that the students are standing in.
    Each heights[i] is the height of the ith student in line (0-indexed).

    Return the number of indices where heights[i] != expected[i].

"""

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return sum(1 for i in range(len(heights)) if heights[i] != expected[i])

        #! ---------------------------------------------------------------

        # c = heights[:]
        # d = 0
        # c.sort()
        # for i in range(len(c)):
        #     if heights[i] != c[i]:
        #         d += 1
        # return d

        #! ---------------------------------------------------------------

        # #? Function to perform bubble sort on the input array.
        # def bubble_sort():
        #     n = len(sorted_heights)
        #     #? Loop through the array for bubble sort passes.
        #     for i in range(n - 1):
        #         #? Inner loop to compare and swap elements.
        #         for j in range(n - i - 1):
        #             #? Compare and swap if elements are in the wrong order.
        #             if sorted_heights[j] > sorted_heights[j + 1]:
        #                 sorted_heights[j], sorted_heights[j + 1] = (
        #                     sorted_heights[j + 1],
        #                     sorted_heights[j],
        #                 )

        # #? Sort the array using bubble sort.
        # sorted_heights = heights[:]
        # bubble_sort()

        # count = 0
        # #? Loop through the original and sorted arrays.
        # for i in range(len(sorted_heights)):
        #     #? Increment count if elements at the same index differ.
        #     if heights[i] != sorted_heights[i]:
        #         count += 1
        # #? Return the total count of differing elements.
        # return count
