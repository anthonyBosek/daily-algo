"""
    169. Majority Element
    https://leetcode.com/problems/majority-element/

    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Using Boyer-Moore Voting Algorithm
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate

        # ---------------------------------------------

        # Using Counter
        # from collections import Counter
        # count = Counter(nums)
        # return max(count.keys(), key=count.get)

        # ---------------------------------------------

        # Using Sorting
        # nums.sort()
        # return nums[len(nums)//2]

        # ---------------------------------------------
        # Using Set
        # return max(set(nums), key=nums.count)

        # ---------------------------------------------

        # Using Dictionary
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        # return max(count.keys(), key=count.get)
