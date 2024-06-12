"""
    75. Sort Colors
    https://leetcode.com/problems/sort-colors/

    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects
    of the same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.

"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Count the number of 0, 1, and 2
        count = [0, 0, 0]
        for num in nums:
            count[num] += 1

        # Update the array
        for i in range(len(nums)):
            if i < count[0]:
                nums[i] = 0
            elif i < count[0] + count[1]:
                nums[i] = 1
            else:
                nums[i] = 2

        #! --------------------------------------------------
        # #? 2nd Approach: Dutch National Flag Algorithm
        # #? https://en.wikipedia.org/wiki/Dutch_national_flag_problem
        # start, mid, end = 0, 0, len(nums) - 1
        # while mid <= end:
        #     if nums[mid] == 0:
        #         nums[start], nums[mid] = nums[mid], nums[start]
        #         mid += 1
        #         start += 1
        #     elif nums[mid] == 1:
        #         mid += 1
        #     elif nums[mid] == 2:
        #         nums[mid], nums[end] = nums[end], nums[mid]
        #         end -= 1
