"""
    525. Contiguous Array
    https://leetcode.com/problems/contiguous-array/

    Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curr_sum, curr_max, n = 0, 0, len(nums)
        dic = {0: -1}
        for i in range(n):
            num = nums[i]
            curr_sum += 1 - 2 * num
            if curr_sum not in dic:
                dic[curr_sum] = i
            else:
                curr_max = max(i - dic[curr_sum], curr_max)
        return curr_max

        # -----------------------------------------------------------------------------------------------------

        # count = 0
        # max_len = 0
        # count_map = {0: -1}
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         count -= 1
        #     else:
        #         count += 1
        #     if count in count_map:
        #         max_len = max(max_len, i - count_map[count])
        #     else:
        #         count_map[count] = i
        # return max_len

        # -----------------------------------------------------------------------------------------------------

        # Using hashmap to store the first index of a prefix sum
        # Initialize the hashmap with {0: -1} to handle the edge case
        # when the contiguous subarray with equal number of 0 and 1 starts from the beginning of the nums array
        # hashmap = {0: -1}
        # max_length = 0
        # count = 0
        # for i in range(len(nums)):
        #     # If the current element is 0, decrease the count by 1
        #     if nums[i] == 0:
        #         count -= 1
        #     # If the current element is 1, increase the count by 1
        #     else:
        #         count += 1
        #     # If the count is already in the hashmap, calculate the length of the current subarray
        #     # and update the max_length if the current subarray is longer
        #     if count in hashmap:
        #         max_length = max(max_length, i - hashmap[count])
        #     # If the count is not in the hashmap, add the count with its corresponding index
        #     else:
        #         hashmap[count] = i
        # return max_length
