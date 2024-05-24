"""
    2444. Count Subarrays With Fixed Bounds
    https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

    You are given an integer array nums and two integers minK and maxK.

    A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

    • The minimum value in the subarray is equal to minK.
    • The maximum value in the subarray is equal to maxK.

    Return the number of fixed-bound subarrays.

    A subarray is a contiguous part of an array.

"""


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        min_index, max_index, bad_index = -1, -1, -1
        for i, v in enumerate(nums):
            if v < minK or v > maxK:
                min_index, max_index, bad_index = -1, -1, i
            if v == minK:
                min_index = i
            if v == maxK:
                max_index = i

            if min_index > -1 and max_index > -1:
                res += min(min_index, max_index) - bad_index
        return res

        # -----------------------------------------------------------------

        # miLastIdx = mxLastIdx = -1
        # wall = -1
        # res = 0
        # for i,x in enumerate(nums):
        #     if x>maxK or x<minK:
        #         miLastIdx = mxLastIdx = -1
        #         wall = i
        #         continue
        #     if x==minK:
        #         miLastIdx = i
        #     if x==maxK:
        #         mxLastIdx = i
        #     if miLastIdx>-1 and mxLastIdx>-1:
        #         b = min(miLastIdx, mxLastIdx)
        #         res += b-wall #b-wall is all the possible starting indices of a subarray that ends at current index i
        # return res

        # -----------------------------------------------------------------

        # res = 0
        # bad_idx = left_idx = right_idx = -1

        # for i, num in enumerate(nums) :
        #     if not minK <= num <= maxK:
        #         bad_idx = i

        #     if num == minK:
        #         left_idx = i

        #     if num == maxK:
        #         right_idx = i

        #     res += max(0, min(left_idx, right_idx) - bad_idx)

        # return res
