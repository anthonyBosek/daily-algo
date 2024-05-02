"""
    2441. Largest Positive Integer That Exists With Its Negative
    https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

    Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.

    Return the positive integer k. If there is no such integer, return -1.

"""


def findMaxK(nums):
    # numsSet = set(nums)
    # pos = []
    # for x in numsSet:
    #     if -x in numsSet:
    #         pos.append(x)
    # return max(pos, default=-1)

    # ---------------------------------------

    # nums.sort()
    # l,r = 0, len(nums) - 1

    # while l < r and nums[l] < 0:
    #     if abs(nums[l]) == nums[r]:
    #         return nums[r]
    #     elif abs(nums[l]) >= nums[r]:
    #         l+=1
    #     else:
    #         r -= 1

    # return -1

    # ---------------------------------------

    # nums = set(nums)
    # maxK = -1
    # for num in nums:
    #     if -num in nums:
    #         maxK = max(maxK, num)
    # return maxK

    # ---------------------------------------

    # nums.sort()
    # for i in range(len(nums)-1, -1, -1):
    #     if -nums[i] in nums:
    #         return nums[i]
    # return -1

    pass
