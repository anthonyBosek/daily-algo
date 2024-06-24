"""
    995. Minimum Number of K Consecutive Bit Flips
    https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

    You are given a binary array nums and an integer k.

    A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0
    in the subarray to 1, and every 1 in the subarray to 0.

    Return the minimum number of k-bit flips required so that there is no 0 in the array.
    If it is not possible, return -1.

    A subarray is a contiguous part of an array.

"""

from typing import List


#! Approach 1: Using an Auxiliary Array
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # Keeps track of flipped states
        flipped = [False] * len(nums)

        # Tracks valid flips within the past window
        validFlipsFromPastWindow = 0

        # Counts total flips needed
        flipCount = 0

        for i in range(len(nums)):
            if i >= k:
                # Decrease count of valid flips from the past window if needed
                if flipped[i - k]:
                    validFlipsFromPastWindow -= 1

            # Check if current bit needs to be flipped
            if validFlipsFromPastWindow % 2 == nums[i]:
                # If flipping the window extends beyond the array length,
                # return -1
                if i + k > len(nums):
                    return -1

                # Increment the count of valid flips and
                # mark current as flipped
                validFlipsFromPastWindow += 1
                flipped[i] = True
                flipCount += 1

        return flipCount


#! Approach 2: Using a Deque
from collections import deque


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)  # Length of the input list
        flip_queue = deque()  # Queue to keep track of flips
        flipped = 0  # Current flip state
        result = 0  # Total number of flips

        for i, num in enumerate(nums):

            # Remove the effect of the oldest flip if it's out of the current window
            if i >= k:
                flipped ^= flip_queue[0]

            # If the current bit is 0 (i.e., it needs to be flipped)
            if flipped == nums[i]:

                # If we cannot flip a subarray starting at index i
                if i + k > n:
                    return -1

                # Add a flip at this position
                flip_queue.append(1)
                flipped ^= 1  # Toggle the flipped state
                result += 1  # Increment the flip count
            else:
                flip_queue.append(0)
            # Remove the oldest flip effect if the queue is longer than k

            if len(flip_queue) > k:
                flip_queue.popleft()
        return result


#! Approach 3: In Constant Space
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        current_flips = 0  # Tracks the current number of flips
        total_flips = 0  # Tracks the total number of flips

        for i in range(len(nums)):
            # If the window slides out of the range and the leftmost element is
            #  marked as flipped (2), decrement current_flips
            if i >= k and nums[i - k] == 2:
                current_flips -= 1

            # Check if the current bit needs to be flipped
            if (current_flips % 2) == nums[i]:
                # If flipping would exceed array bounds, return -1
                if i + k > len(nums):
                    return -1
                # Mark the current bit as flipped
                nums[i] = 2
                current_flips += 1
                total_flips += 1

        return total_flips


#! fastest on leetcode
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        ans = 0
        flippedTime = 0

        for i, num in enumerate(nums):
            if i >= k and nums[i - k] == 2:
                flippedTime -= 1
            if flippedTime % 2 == num:
                if i + k > len(nums):
                    return -1
                ans += 1
                flippedTime += 1
                nums[i] = 2

        return ans
