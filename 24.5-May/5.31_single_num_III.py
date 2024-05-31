"""
    260. Single Number III
    https://leetcode.com/problems/single-number-iii/

    Given an integer array nums, in which exactly two elements appear only once and all the other elements
    appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

    You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

"""

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for n in nums:
            if n in ans:
                ans.remove(n)
            else:
                ans.add(n)
        return list(ans)

        # ? ---------------------------------------------

        # xor = 0
        # for num in nums:
        #     xor ^= num

        # mask = 1
        # while xor & mask == 0:
        #     mask <<= 1

        # a = b = 0
        # #? a, b = 0, 0
        # for num in nums:
        #     if num & mask:
        #         a ^= num
        #     else:
        #         b ^= num

        # return [a, b]
