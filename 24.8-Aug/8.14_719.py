"""
    719. Find K-th Smallest Pair Distance
    https://leetcode.com/problems/find-k-th-smallest-pair-distance/

    The distance of a pair of integers a and b is defined as the absolute difference between a and b.

    Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

"""

from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = low + (high - low) // 2
            count, left = 0, 0
            for right in range(n):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low


#! Approach 1: Bucket Sort !!!Time limit exceeded!!!
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        list_size = len(nums)

        # Find the maximum element in the list
        max_element = max(nums)

        # Initialize a bucket list to store counts of each distance
        distance_bucket = [0] * (max_element + 1)

        # Populate the bucket list with counts of each distance
        for i in range(list_size):
            for j in range(i + 1, list_size):
                # Compute the distance between nums[i] and nums[j]
                distance = abs(nums[i] - nums[j])

                # Increment the count for this distance in the bucket
                distance_bucket[distance] += 1

        # Find the k-th smallest distance
        for dist in range(max_element + 1):
            # Reduce k by the number of pairs with the current distance
            k -= distance_bucket[dist]

            # If k is less than or equal to 0, return the current distance
            if k <= 0:
                return dist

        return -1  # Return -1 if no distance found, should not reach here


#! Approach 2: Binary Search + Dynamic Programming (DP)
class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        array_size = len(nums)

        # Highest element in the sorted array
        max_element = nums[-1]

        # Maximum possible distance
        max_possible_distance = max_element * 2

        # Initialize arrays for prefix counts and value counts
        prefix_count = [0] * max_possible_distance
        value_count = [0] * (max_element + 1)

        # Populate prefix count and value count
        index = 0
        for value in range(max_possible_distance):
            while index < array_size and nums[index] <= value:
                index += 1
            prefix_count[value] = index
        for i in range(array_size):
            value_count[nums[i]] += 1

        # Binary search to find kth smallest distance
        left, right = 0, max_element
        while left < right:
            mid = (left + right) // 2

            # Count pairs with distance <= mid
            count = self._count_pairs(nums, prefix_count, value_count, mid)

            # Adjust binary search bounds based on count
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    def _count_pairs(self, nums, prefix_count, value_count, max_distance):
        count = 0
        array_size = len(nums)
        index = 0

        while index < array_size:
            current_value = nums[index]
            value_count_for_current = value_count[current_value]

            # Calculate pairs involving current value with distance <= max_distance
            pairs_with_larger_values = (
                prefix_count[min(current_value + max_distance, len(prefix_count) - 1)]
                - prefix_count[current_value]
            )
            pairs_with_same_values = (
                value_count_for_current * (value_count_for_current - 1) // 2
            )
            count += (
                pairs_with_larger_values * value_count_for_current
                + pairs_with_same_values
            )

            # Skip duplicate values
            while index + 1 < array_size and nums[index] == nums[index + 1]:
                index += 1
            index += 1

        return count


#! Approach 3: Binary Search + Sliding Window
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        array_size = len(nums)

        # Initialize binary search range
        low = 0
        high = nums[array_size - 1] - nums[0]

        while low < high:
            mid = (low + high) // 2

            # Count pairs with distance <= mid
            count = self._count_pairs_with_max_distance(nums, mid)

            # Adjust binary search bounds based on count
            if count < k:
                low = mid + 1
            else:
                high = mid

        return low

    # Count number of pairs with distance <= max_distance using a moving window
    def _count_pairs_with_max_distance(self, nums: List[int], max_distance: int) -> int:
        count = 0
        array_size = len(nums)
        left = 0

        for right in range(array_size):
            # Adjust the left pointer to maintain the window with distances <=
            # max_distance
            while nums[right] - nums[left] > max_distance:
                left += 1
            # Add the number of valid pairs ending at the current right index
            count += right - left
        return count
