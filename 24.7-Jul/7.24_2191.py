"""
    2191. Sort the Jumbled Numbers
    https://leetcode.com/problems/sort-the-jumbled-numbers/

    You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system.
    mapping[i] = j means digit i should be mapped to digit j in this system.

    The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer
    with mapping[i] for all 0 <= i <= 9.

    You are also given another integer array nums.
    
    Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

    Notes:

        - Elements with the same mapped values should appear in the same relative order as in the input.
        - The elements of nums should only be sorted based on their mapped values and not be replaced by them.

"""

from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # return sorted(
        #     nums,
        #     key=lambda n: int("".join(map(lambda d: str(mapping[int(d)]), str(n)))),
        # )
        # #!
        trans_rule = str.maketrans({str(i): str(x) for i, x in enumerate(mapping)})
        return sorted(nums, key=lambda x: int(str(x).translate(trans_rule)))


#! Approach 1: Conversion using strings and Sorting
class Solution:
    def sortJumbled(self, mapping, nums):
        store_pairs = []

        for i in range(len(nums)):
            # Convert current value to string
            number = str(nums[i])
            formed = ""
            for j in range(len(number)):
                formed = formed + str(mapping[int(number[j])])
            # Store the mapped value.
            mapped_value = int(formed)
            # Push a pair consisting of mapped value and original value's index.
            store_pairs.append((mapped_value, i))

        # Sort the array in non-decreasing order by the first value (default).
        store_pairs.sort()
        answer = []
        for pair in store_pairs:
            answer.append(nums[pair[1]])
        return answer


#! Approach 2: Conversion without using strings and Sorting
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        store_pairs = []

        for i in range(len(nums)):
            mapped_value = 0
            temp = nums[i]

            # Start making changes from the units place.
            place = 1
            # If the value initially is 0, return mapping[0] and index.
            if temp == 0:
                store_pairs.append((mapping[0], i))
                continue
            # Repeat the process for units, tenths, hundredths.. places.
            while temp != 0:
                mapped_value = place * mapping[temp % 10] + mapped_value
                place *= 10
                temp //= 10
            store_pairs.append((mapped_value, i))

        # Sort the array in non-decreasing order by the first value (default).
        store_pairs.sort()
        answer = [nums[pair[1]] for pair in store_pairs]

        return answer
