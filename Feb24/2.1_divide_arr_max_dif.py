"""
    2966. Divide Array Into Arrays With Max Difference
    https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

    You are given an integer array nums of size n and a positive integer k.

    Divide the array into one or more arrays of size 3 satisfying the following conditions:
     - Each element of nums should be in exactly one array.
     - The difference between any two elements in one array is less than or equal to k.

    Return a 2D array containing all the arrays. If it is impossible to satisfy the conditions,
        return an empty array. And if there are multiple answers, return any of them.
        
"""


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        while nums:
            res.append([nums.pop(0)])
            for i in range(len(nums)):
                if nums[i] - res[-1][-1] <= k:
                    res[-1].append(nums.pop(i))
                    break
            else:
                return []
        return res

        # size = len(nums)
        # if size % 3 != 0:
        #     return []

        # nums.sort()

        # result = []
        # group_index = 0
        # for i in range(0, size, 3):
        #     if i + 2 < size and nums[i + 2] - nums[i] <= k:
        #         result.append([nums[i], nums[i + 1], nums[i + 2]])
        #         group_index += 1
        #     else:
        #         return []
        # return result

        # ------------------------------

        # nums.sort()
        # res = []
        # while nums:
        #     res.append(nums[:3])
        #     nums = nums[3:]
        # return res

        # ------------------------------

        # nums.sort()
        # n = len(nums)
        # res = []
        # i = 0
        # while i < n:
        #     res.append(nums[i : i + 3])
        #     i += 3
        # return res

        # ------------------------------

        # nums.sort()
        # res = []
        # while nums:
        #     res.append([nums.pop(0)])
        #     for i in range(len(nums)):
        #         if nums[i] - res[-1][-1] <= k:
        #             res[-1].append(nums.pop(i))
        #             break
        #     else:
        #         return []
        # return res
