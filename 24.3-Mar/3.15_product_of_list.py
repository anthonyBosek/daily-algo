"""
    238. Product of Array Except Self
    https://leetcode.com/problems/product-of-array-except-self/

    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1]*len(nums)
        # for i in range(1,len(nums)):
        #     res[i] = res[i-1] * nums[i-1]
        # post = 1
        # for i in range(len(nums)-1,-1,-1):
        #     res[i] *= post
        #     post *= nums[i]
        # return res

        # ---------------------------------------------------

        prefix, postfix = 1, 1
        res = [0] * len(nums)
        for i in range(len(nums)):

            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

        # ---------------------------------------------------

        # n = len(nums)
        # left = [0] * n
        # right = [0] * n
        # left[0] = 1
        # right[n-1] = 1
        # for i in range(1, n):
        #     left[i] = left[i-1] * nums[i-1]
        # for i in range(n-2, -1, -1):
        #     right[i] = right[i+1] * nums[i+1]
        # for i in range(n):
        #     nums[i] = left[i] * right[i]
        # return nums
