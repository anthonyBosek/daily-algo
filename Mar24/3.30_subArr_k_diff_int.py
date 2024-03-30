"""
    992. Subarrays with K Different Integers
    https://leetcode.com/problems/subarrays-with-k-different-integers/

    Given an integer array nums and an integer k, return the number of good subarrays of nums.

    A good array is an array where the number of different integers in that array is exactly k.

    • For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

    A subarray is a contiguous part of an array.

"""


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt, res, l, m = [0] * (len(nums) + 1), 0, 0, 0
        for n in nums:
            cnt[n] += 1
            if cnt[n] == 1:
                k -= 1
                if k < 0:
                    cnt[nums[m]] = 0
                    m += 1
                    l = m
            if k <= 0:
                while cnt[nums[m]] > 1:
                    cnt[nums[m]] -= 1
                    m += 1
                res += m - l + 1
        return res

    #     # -----------------------------------------------------------

    #     return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    # def atMostK(self, nums, k):
    #     count = 0
    #     left = 0
    #     freq = {}
    #     for right in range(len(nums)):
    #         if nums[right] not in freq or freq[nums[right]] == 0:
    #             k -= 1
    #         freq[nums[right]] = freq.get(nums[right], 0) + 1
    #         while k < 0:
    #             freq[nums[left]] -= 1
    #             if freq[nums[left]] == 0:
    #                 k += 1
    #             left += 1
    #         count += right - left + 1
    #     return count
