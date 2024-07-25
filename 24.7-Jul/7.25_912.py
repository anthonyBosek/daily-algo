"""
    912. Sort an Array
    https://leetcode.com/problems/sort-an-array/

    Given an array of integers nums, sort the array in ascending order and return it.

    You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
    and with the smallest space complexity possible.

"""


#! Approach 1: Bucket Sort
def sortArray(nums):
    # return sorted(nums) #! This is not allowed.

    # Find the absolute maximum element to find max number of digits.
    max_element = max(map(abs, nums))

    max_digits = 0
    while max_element > 0:
        max_digits += 1
        max_element = max_element // 10

    place_value = 1

    # Bucket sort function for each place value digit.
    def bucket_sort():
        buckets = [[] for _ in range(10)]
        # Store the respective number based on it's digit.
        for val in nums:
            digit = abs(val) / place_value
            digit = int(digit % 10)
            buckets[digit].append(val)

        # Overwrite 'nums' in sorted order of current place digits.
        index = 0
        for digit in range(10):
            for val in buckets[digit]:
                nums[index] = val
                index += 1

    # Radix sort, least significant digit place to most significant.
    for _ in range(max_digits):
        bucket_sort()
        place_value *= 10

    # Seperate out negatives and reverse them.
    positives = [val for val in nums if val >= 0]
    negatives = [val for val in nums if val < 0]
    negatives.reverse()

    # Final 'arr' will be 'negative' elements, then 'positive' elements.
    return negatives + positives


# -----------------------------------------------------------------------


#! Approach 2: Merge Sort
def sortArray(nums):
    def mergeSort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            mergeSort(L)
            mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    mergeSort(nums)
    return nums
