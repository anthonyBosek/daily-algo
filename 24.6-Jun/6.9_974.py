"""
    974. Subarray Sums Divisible by K
    https://leetcode.com/problems/subarray-sums-divisible-by-k/

    Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

    A subarray is a contiguous part of an array.
    
"""

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mod = [0] * k
        mod[0] = 1
        running_mod = 0
        for num in nums:
            running_mod = (num + running_mod) % k
            mod[running_mod] += 1

        return sum([n * (n - 1) // 2 for n in mod])

        # -----------------------------------------------------

        # count = 0
        # prefix_sum = 0
        # remainder_count = {0: 1}
        # for num in nums:
        #     prefix_sum += num
        #     remainder = prefix_sum % k
        #     count += remainder_count.get(remainder, 0)
        #     remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        # return count
