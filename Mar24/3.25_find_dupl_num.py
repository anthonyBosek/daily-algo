"""
    287. Find the Duplicate Number
    https://leetcode.com/problems/find-the-duplicate-number/

    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.

"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            if num in (num_set):
                return num
            else:
                num_set.add(num)

        # --------------------------------------------

        # # Floyd's Tortoise and Hare (Cycle Detection)
        # # Time complexity: O(n)
        # # Space complexity: O(1)
        # slow = nums[0]
        # fast = nums[0]

        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]

        #     if slow == fast:
        #         break

        # slow = nums[0]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]

        # return slow
