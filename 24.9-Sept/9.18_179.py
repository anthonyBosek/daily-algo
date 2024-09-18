"""
    179. Largest Number
    https://leetcode.com/problems/largest-number/

    Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

    Since the result may be very large, you will need to return a string instead of an integer.
    
"""


def largestNumber(nums):
    # Convert numbers to strings for comparison
    nums = list(map(str, nums))

    # Sort numbers based on custom comparison
    nums.sort(key=lambda x: x * 10, reverse=True)

    # Join sorted numbers into a single string
    result = "".join(nums)

    # Handle the case where the result is all zeros
    return result if result[0] != "0" else "0"


#! Approach 1: Using Built-in Function
def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    # Convert each integer to a string
    num_strings = [str(num) for num in nums]

    # Sort strings based on concatenated values
    num_strings.sort(key=lambda a: a * 10, reverse=True)

    # Handle the case where the largest number is zero
    if num_strings[0] == "0":
        return "0"

    # Concatenate sorted strings to form the largest number
    return "".join(num_strings)


#! Approach 2: Quick Sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Sort the numbers using Quick Sort
        self._quick_sort(nums, 0, len(nums) - 1)
        # Concatenate sorted numbers to form the largest number
        largest_num = "".join(map(str, nums))
        # Handle the case where the largest number is zero
        return "0" if largest_num[0] == "0" else largest_num

    def _quick_sort(self, nums: List[int], left: int, right: int) -> None:
        # Base case: if the range has one or no elements, it is already sorted
        if left >= right:
            return

        # Partition the array and get the pivot index
        pivot_index = self._partition(nums, left, right)

        # Recursively sort the sub-arrays
        self._quick_sort(nums, left, pivot_index - 1)
        self._quick_sort(nums, pivot_index + 1, right)

    def _partition(self, nums: List[int], left: int, right: int) -> int:
        pivot = nums[right]
        low_index = left

        # Rearrange elements so that those greater than the pivot are on the left
        for i in range(left, right):
            if self._compare(nums[i], pivot):
                nums[i], nums[low_index] = nums[low_index], nums[i]
                low_index += 1

        # Place the pivot in its correct position
        nums[low_index], nums[right] = nums[right], nums[low_index]
        return low_index

    def _compare(self, first_num: int, second_num: int) -> bool:
        # Compare concatenated strings to decide the order
        return str(first_num) + str(second_num) > str(second_num) + str(first_num)


#! Approach 3: Merge Sort
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Sort the numbers using Merge Sort
        sorted_nums = self._merge_sort(nums, 0, len(nums) - 1)
        # Concatenate sorted numbers to form the largest number
        largest_num = "".join(map(str, sorted_nums))
        # Handle the case where the largest number is zero
        return "0" if largest_num[0] == "0" else largest_num

    def _merge_sort(self, nums: List[int], left: int, right: int) -> List[int]:
        # Base case: a single element is already sorted
        if left >= right:
            return [nums[left]]
        mid = left + (right - left) // 2

        # Recursively sort the left and right halves
        left_half = self._merge_sort(nums, left, mid)
        right_half = self._merge_sort(nums, mid + 1, right)

        # Merge the sorted halves
        return self._merge(left_half, right_half)

    def _merge(self, left_half: List[int], right_half: List[int]) -> List[int]:
        sorted_nums = []
        left_index, right_index = 0, 0

        # Merge the two halves based on custom comparison
        while left_index < len(left_half) and right_index < len(right_half):
            if self._compare(left_half[left_index], right_half[right_index]):
                sorted_nums.append(left_half[left_index])
                left_index += 1
            else:
                sorted_nums.append(right_half[right_index])
                right_index += 1

        # Append remaining elements from left half
        sorted_nums.extend(left_half[left_index:])

        # Append remaining elements from right half
        sorted_nums.extend(right_half[right_index:])
        return sorted_nums

    def _compare(self, first_num: int, second_num: int) -> bool:
        # Compare concatenated strings to decide the order
        return str(first_num) + str(second_num) > str(second_num) + str(first_num)


#! Approach 4: HeapSort
from typing import List
import heapq


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Edge case: if all numbers are zero, return "0"
        if not any(nums):
            return "0"

        # Custom comparison function for heapq (simulating the comparator in Java)
        class LargerStrComparator(str):
            def __lt__(self, other):
                # Custom comparison: return True if self+other > other+self
                return self + other > other + self

        # Priority queue (min-heap), but we push elements using a custom comparator
        heap = []
        for num in nums:
            heapq.heappush(heap, LargerStrComparator(str(num)))

        # Build the result string by popping from the heap
        result = []
        while heap:
            result.append(heapq.heappop(heap))

        # Concatenate and return the result
        largest_num = "".join(result)

        # Handle case where all elements are "0"
        return "0" if largest_num[0] == "0" else largest_num


#! Approach 5: TimSort
class Solution:
    RUN = 32

    def largestNumber(self, nums: List[int]) -> str:
        # Sort the numbers using custom Tim Sort
        self.tim_sort(nums)
        # Concatenate sorted numbers to form the largest number
        largest_num = "".join(map(str, nums))
        # Handle the case where the largest number is zero
        return "0" if largest_num[0] == "0" else largest_num

    def insertion_sort(self, nums: List[int], left: int, right: int):
        for i in range(left + 1, right + 1):
            temp = nums[i]
            j = i - 1
            while j >= left and self.compare(temp, nums[j]):
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp

    def merge(self, nums: List[int], left: int, mid: int, right: int):
        left_arr = nums[left : mid + 1]
        right_arr = nums[mid + 1 : right + 1]

        i, j, k = 0, 0, left
        while i < len(left_arr) and j < len(right_arr):
            if self.compare(left_arr[i], right_arr[j]):
                nums[k] = left_arr[i]
                i += 1
            else:
                nums[k] = right_arr[j]
                j += 1
            k += 1
        nums[k : right + 1] = left_arr[i:] + right_arr[j:]

    def tim_sort(self, nums: List[int]):
        n = len(nums)
        # Sort small runs with insertion sort
        for i in range(0, n, self.RUN):
            self.insertion_sort(nums, i, min(i + self.RUN - 1, n - 1))
        # Merge sorted runs
        size = self.RUN
        while size < n:
            for left in range(0, n, 2 * size):
                mid = left + size - 1
                right = min(left + 2 * size - 1, n - 1)
                if mid < right:
                    self.merge(nums, left, mid, right)
            size *= 2

    def compare(self, first_num: int, second_num: int) -> bool:
        return str(first_num) + str(second_num) > str(second_num) + str(first_num)


#! Approach 6
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def mergeSortReverse(l, r):
            if l >= r:
                return

            m = (l + r) // 2
            mergeSortReverse(l, m)
            mergeSortReverse(m + 1, r)
            mergeReverse(l, r, m)
            return

        def mergeReverse(l, r, m):
            left = nums[l : m + 1]
            right = nums[m + 1 : r + 1]
            i, j, k = 0, 0, l

            while i < len(left) and j < len(right):

                if compare(left[i], right[j]):
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                k += 1
                j += 1

            return

        def compare(num1, num2):
            return str(num1) + str(num2) >= str(num2) + str(num1)

        nums.sort(key=lambda x: str(x) * 10, reverse=True)
        if nums[0] == 0:
            return "0"

        return "".join([str(i) for i in nums])
