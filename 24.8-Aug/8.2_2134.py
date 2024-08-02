"""
    2134. Minimum Swaps to Group All 1's Together II
    https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

    A swap is defined as taking two distinct positions in an array and swapping the values in them.

    A circular array is defined as an array where we consider the first element and the last element to be adjacent.

    Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the
    array together at any location.

"""


def minSwaps(n):
    k = sum(n)
    ones = sum(n[-k:])
    max_fill = ones
    for i in range(len(n)):
        ones += n[i] - n[i - k]
        if ones > max_fill:
            max_fill = ones
    return k - max_fill


#! Approach 1: Using Suffix Sum
from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        op1 = self.min_swaps_helper(nums, 0)  # Grouping all 0s together
        op2 = self.min_swaps_helper(nums, 1)  # Grouping all 1s together
        return min(op1, op2)

    def min_swaps_helper(self, data: List[int], val: int) -> int:
        length = len(data)
        right_suffix_sum = [0] * (length + 1)

        # Construct the suffix sum array for counting opposite values
        # (val ^ 1)
        for i in range(length - 1, -1, -1):
            right_suffix_sum[i] = right_suffix_sum[i + 1]
            if data[i] == (val ^ 1):
                right_suffix_sum[i] += 1

        # Total zeros in the array if `val` is 1 (or vice versa)
        total_swaps_needed = right_suffix_sum[0]
        # Track current number of required swaps in the current segment
        current_swap_count = 0
        minimum_swaps = (
            total_swaps_needed - right_suffix_sum[length - total_swaps_needed]
        )

        # Iterate to find the minimum swaps by sliding
        # the potential block of grouped `val`
        for i in range(total_swaps_needed):
            if data[i] == (val ^ 1):
                current_swap_count += 1
            remaining = total_swaps_needed - i - 1
            required_swaps = ((i + 1) - current_swap_count) + (
                remaining - right_suffix_sum[length - remaining]
            )
            minimum_swaps = min(minimum_swaps, required_swaps)
        return minimum_swaps


#! Approach 2: Using Sliding Window
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Calculate the minimum swaps needed to group all 1s or all 0s together
        op1 = self.min_swaps_helper(nums, 0)  # Grouping all 0s together
        op2 = self.min_swaps_helper(nums, 1)  # Grouping all 1s together
        return min(op1, op2)

    def min_swaps_helper(self, data: List[int], val: int) -> int:
        length = len(data)
        total_val_count = 0

        # Count the total number of `val` in the array
        for i in range(length - 1, -1, -1):
            if data[i] == val:
                total_val_count += 1

        # If there is no `val` or the array is full of `val`, no swaps are needed
        if total_val_count == 0 or total_val_count == length:
            return 0

        start = 0
        end = 0
        max_val_in_window = 0
        current_val_in_window = 0

        # Initial window setup: count the number of `val` in the first window of size `total_val_count`
        while end < total_val_count:
            if data[end] == val:
                current_val_in_window += 1
            end += 1
        max_val_in_window = max(max_val_in_window, current_val_in_window)

        # Slide the window across the array to find the maximum number of `val` in any window
        while end < length:
            if data[start] == val:
                current_val_in_window -= 1
            start += 1
            if data[end] == val:
                current_val_in_window += 1
            end += 1
            max_val_in_window = max(max_val_in_window, current_val_in_window)

        # Minimum swaps are the total `val` minus the maximum found in any window
        return total_val_count - max_val_in_window


#! Approach 3: Cleaner and More Intuitive Sliding Window
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Initialize minimum swaps to a large value
        minimum_swaps = float("inf")

        # Calculate the total number of 1s in the array
        total_ones = sum(nums)

        # Initialize the count of 1s in the current window
        ones_count = nums[0]
        end = 0

        # Slide the window across the array
        for start in range(len(nums)):
            # Adjust ones_count by removing the element that
            # is sliding out of the window
            if start != 0:
                ones_count -= nums[start - 1]

            # Expand the window to the right until it reaches the desired size
            while end - start + 1 < total_ones:
                end += 1
                ones_count += nums[end % len(nums)]

            # Update the minimum number of swaps needed
            minimum_swaps = min(minimum_swaps, total_ones - ones_count)

        return minimum_swaps
