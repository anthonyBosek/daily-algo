"""
    2958. Length of Longest Subarray With at Most K Frequency
    https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency

    You are given an integer array nums and an integer k.

    The frequency of an element x is the number of times it occurs in an array.

    An array is called good if the frequency of each element in this array is less than or equal to k.

    Return the length of the longest good subarray of nums.

    A subarray is a contiguous non-empty sequence of elements within an array.

"""


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        max = 0
        for right in range(len(nums)):
            valright = nums[right]
            if valright in freq:
                freq[valright] += 1
            else:
                freq[valright] = 1
            while freq[valright] > k and left <= right:
                valleft = nums[left]
                freq[valleft] -= 1
                left += 1
            length = right - left + 1
            if length > max:
                max = length
        return max

        # ------------------------------------------------------

        # ans = 0
        # mp = {}
        # l = 0
        # n = len(nums)
        # for r in range(n):
        #     mp[nums[r]] = mp.get(nums[r], 0) + 1
        #     if mp[nums[r]] > k:
        #         while nums[l] != nums[r]:
        #             mp[nums[l]] -= 1
        #             l += 1
        #         mp[nums[l]] -= 1
        #         l += 1
        #     ans = max(ans, r - l + 1)
        # return ans
