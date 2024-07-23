"""
    1636. Sort Array by Increasing Frequency
    https://leetcode.com/problems/sort-array-by-increasing-frequency/

    Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
    
    If multiple values have the same frequency, sort them in decreasing order.

    Return the sorted array.

"""

from collections import Counter


def frequencySort(n):
    c = Counter(n)
    return sorted(n, key=lambda x: (c[x], -x))

    #!

    # # Step 1: Count the frequency of each number
    # freq_dict = {}
    # for num in nums:
    #     freq_dict[num] = freq_dict.get(num, 0) + 1

    # # Step 2: Sort the numbers by frequency first, and by number value if frequencies are the same
    # sorted_nums = sorted(nums, key=lambda x: (freq_dict[x], -x))

    # return sorted_nums


#! Approach: Customized Sorting
# The lambda function lambda x: (freq[x], -x) is used as the key parameter in the sorted function call.
# 1. lambda x: creates an anonymous function with x as its parameter.
# 2. (freq[x], -x) is the tuple that the lambda function returns.
# 3. freq[x] is used to get the frequency of x from the freq dictionary as the main sorting criterion.
# 4. -x ensures that values are sorted in descending order when their frequencies are the same.
