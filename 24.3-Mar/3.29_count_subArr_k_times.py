"""
    2962. Count Subarrays Where Max Element Appears at Least K Times
    https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times

    You are given an integer array nums and a positive integer k.

    Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

    A subarray is a contiguous sequence of elements within an array.

"""


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ma = nums[0]
        ps = [0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] > ma:
                ma = nums[i]
                ps = [i]
            elif nums[i] == ma:
                ps.append(i)
        if len(ps) < k:
            return 0
        ans = 0
        idx = -1
        for l in range(len(ps) - k + 1):
            ans += (n - ps[l + k - 1]) * (ps[l] - idx)
            idx = ps[l]
        return ans

        # ---------------------------------------------------

        # mx, ans, l, r, n = max(nums), 0, 0, 0, len(nums)
        # while r < n:
        #     k -= nums[r] == mx
        #     r += 1
        #     while k == 0:
        #         k += nums[l] == mx
        #         l += 1
        #     ans += l
        # return ans
