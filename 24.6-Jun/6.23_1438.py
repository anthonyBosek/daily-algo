"""
    1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
    https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

    Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that
    the absolute difference between any two elements of this subarray is less than or equal to limit.

"""

from typing import List
from heapq import heappush, heappop
from sortedcontainers import SortedDict
from collections import deque


#! Approach 1: Two Heaps
class Solution:
    def longestSubarray(self, nums, limit):
        max_heap = []
        min_heap = []

        left = 0
        max_length = 0

        for right in range(len(nums)):
            heappush(max_heap, (-nums[right], right))
            heappush(min_heap, (nums[right], right))

            # Check if the absolute difference between the maximum and minimum values in the current window exceeds the limit
            while -max_heap[0][0] - min_heap[0][0] > limit:
                # Move the left pointer to the right until the condition is satisfied.
                # This ensures we remove the element causing the violation
                left = min(max_heap[0][1], min_heap[0][1]) + 1

                # Remove elements from the heaps that are outside the current window
                while max_heap[0][1] < left:
                    heappop(max_heap)
                while min_heap[0][1] < left:
                    heappop(min_heap)

            # Update max_length with the length of the current valid window
            max_length = max(max_length, right - left + 1)

        return max_length


#! Approach 2: Multiset
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # SortedDict to maintain the elements within the current window
        window = SortedDict()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] in window:
                window[nums[right]] += 1
            else:
                window[nums[right]] = 1

            # Check if the absolute difference between the maximum and minimum values in the current window exceed the limit
            while window.peekitem(-1)[0] - window.peekitem(0)[0] > limit:
                # Remove the element at the left pointer from the SortedDict
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    window.pop(nums[left])
                # Move the left pointer to the right to exclude the element causing the violation
                left += 1

            # Update maxLength with the length of the current valid window
            max_length = max(max_length, right - left + 1)

        return max_length


#! Approach 3: Two Deques
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Maintain the max_deque in decreasing order
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            # Maintain the min_deque in increasing order
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            # Check if the current window exceeds the limit
            while max_deque[0] - min_deque[0] > limit:
                # Remove the elements that are out of the current window
                if max_deque[0] == nums[left]:
                    max_deque.popleft()
                if min_deque[0] == nums[left]:
                    min_deque.popleft()
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
