"""
    1509. Minimum Difference Between Largest and Smallest Value in Three Moves
    https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

    You are given an integer array nums.

    In one move, you can choose one element of nums and change it to any value.

    Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

"""


def minDifference(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) <= 4:
        return 0

    nums.sort()
    n = len(nums)
    return min(
        nums[n - 4] - nums[0],
        nums[n - 3] - nums[1],
        nums[n - 2] - nums[2],
        nums[n - 1] - nums[3],
    )


# #! Approach 1: Sort + Greedy Deletion

# from typing import List


# class Solution:
#     def minDifference(self, nums: List[int]) -> int:
#         nums_size = len(nums)

#         # If the array has 4 or fewer elements, return 0
#         if nums_size <= 4:
#             return 0

#         nums.sort()

#         min_diff = float("inf")

#         # Four scenarios to compute the minimum difference
#         for left in range(4):
#             right = nums_size - 4 + left
#             min_diff = min(min_diff, nums[right] - nums[left])

#         return min_diff


# #! Approach 2: Partial Sort + Greedy Deletion

# from typing import List
# from heapq import nsmallest, nlargest


# class Solution:
#     def minDifference(self, nums: List[int]) -> int:
#         nums_size = len(nums)
#         if nums_size <= 4:
#             return 0

#         # Find the four smallest elements
#         smallest_four = sorted(nsmallest(4, nums))

#         # Find the four largest elements
#         largest_four = sorted(nlargest(4, nums))

#         min_diff = float("inf")
#         # Four scenarios to compute the minimum difference
#         for i in range(4):
#             min_diff = min(min_diff, largest_four[i] - smallest_four[i])

#         return min_diff
