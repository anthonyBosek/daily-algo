"""
    1248. Count Number of Nice Subarrays
    https://leetcode.com/problems/count-number-of-nice-subarrays/

    Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

    Return the number of nice sub-arrays.

"""


def numberOfSubarrays(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # #? Approach 1: Hashing
    curr_sum = 0
    subarrays = 0
    prefix_sum = {curr_sum: 1}

    for i in range(len(nums)):
        curr_sum += nums[i] % 2
        # ? Find subarrays with sum k ending at i
        if curr_sum - k in prefix_sum:
            subarrays = subarrays + prefix_sum[curr_sum - k]
        # ? Increment the current prefix sum in hashmap
        prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

    return subarrays

    #! ------------------------------------------------------------------------
    # #? Approach 2: Sliding Window using Queue
    # odd_indices = deque()
    # subarrays = 0
    # last_popped = -1
    # initial_gap = -1

    # for i in range(len(nums)):
    #     #? If element is odd, append its index to the deque.
    #     if nums[i] % 2 == 1:
    #         odd_indices.append(i)
    #     #? If the number of odd numbers exceeds k, remove the first odd index.
    #     if len(odd_indices) > k:
    #         last_popped = odd_indices.popleft()
    #     #? If there are exactly k odd numbers, add the number of even numbers
    #     #? in the beginning of the subarray to the result.
    #     if len(odd_indices) == k:
    #         initial_gap = odd_indices[0] - last_popped
    #         subarrays += initial_gap

    # return subarrays

    #! ------------------------------------------------------------------------
    # #? Approach 3: Sliding Window (Space Optimisation of queue-based approach)
    # Runtime 557ms Memory 23.45MB --> **BEST**
    # subarrays = 0
    # initial_gap = 0
    # qsize = 0
    # start = 0
    # for end in range(len(nums)):
    #     #? If current element is odd, increment qsize by 1.
    #     if nums[end] % 2 == 1:
    #         qsize += 1
    #     if qsize == k:
    #         initial_gap = 0
    #         #? Calculate the number of even elements in the beginning of
    #         #? subarray.
    #         while qsize == k:
    #             qsize -= nums[start] % 2
    #             initial_gap += 1
    #             start += 1
    #     subarrays += initial_gap
    # return subarrays


#! ------------------------------------------------------------------------
# #? Approach 4: Sliding Window (subarray sum at most k)

# from typing import List


# class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         return self.atMost(nums, k) - self.atMost(nums, k - 1)

#     def atMost(self, nums: List[int], k: int) -> int:
#         window_size, subarrays, start = 0, 0, 0
#         for end in range(len(nums)):
#             window_size += nums[end] % 2
#             #? Find the first index start where the window has exactly k odd elements.
#             while window_size > k:
#                 window_size -= nums[start] % 2
#                 start += 1
#             #? Increment number of subarrays with end - start + 1.
#             subarrays += end - start + 1
#         return subarrays
