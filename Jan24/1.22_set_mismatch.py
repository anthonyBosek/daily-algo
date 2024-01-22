""""
    645. Set Mismatch
    https://leetcode.com/problems/set-mismatch/

    You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
    one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

    You are given an integer array nums representing the data status of this set after the error.

    Find the number that occurs twice and the number that is missing and return them in the form of an array.

"""


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 1. set
        # 2. sum
        # 3. math

        # 1. set
        # Time: O(n)
        # Space: O(n)
        # nums_set = set()
        # for num in nums:
        #     if num not in nums_set:
        #         nums_set.add(num)
        #     else:
        #         return [num, (set(range(1, len(nums) + 1)) - nums_set).pop()]

        # 2. sum
        # Time: O(n)
        # Space: O(1)
        # n = len(nums)
        # return [sum(nums) - sum(set(nums)), n * (n + 1) // 2 - sum(set(nums))]

        # 3. math
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        nums_sum = sum(nums)
        nums_sum_set = sum(set(nums))
        return [nums_sum - nums_sum_set, n * (n + 1) // 2 - nums_sum_set]
