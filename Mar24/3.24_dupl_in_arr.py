"""
    442. Find All Duplicates in an Array
    https://leetcode.com/problems/find-all-duplicates-in-an-array/

    Given an integer array nums of length n where all the integers of nums are in the range [1, n] and
        each integer appears once or twice, return an array of all the integers that appears twice.

    You must write an algorithm that runs in O(n) time and uses only constant extra space.

"""


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # count = Counter(nums)
        # ls=[]
        # for i , j in count.items():
        #     if j >= 2:
        #         ls.append(i)
        # return ls

        # ----------------------------------------------------

        seen, duplicates = set(), []

        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)

        return duplicates

        # ----------------------------------------------------

        # res = []
        # for i in range(len(nums)):
        #     index = abs(nums[i]) - 1
        #     if nums[index] < 0:
        #         res.append(index + 1)
        #     nums[index] = -nums[index]
        # return res
