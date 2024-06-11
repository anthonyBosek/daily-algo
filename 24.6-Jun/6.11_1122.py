"""
    1122. Relative Sort Array
    https://leetcode.com/problems/relative-sort-array/

    Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

    Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
    Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

"""

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map = {}
        for i in range(len(arr2)):
            hash_map[arr2[i]] = i

        for i in range(len(arr1)):
            if arr1[i] not in hash_map:
                hash_map[arr1[i]] = 1000 + arr1[i]
        arr1.sort(key=lambda x: hash_map[x])
        return arr1

        #! --------------------------------------------------------------------

        # count_map = {}
        # remaining = []
        # result = []
        # #? Initialize count map with relative order elements
        # for value in arr2:
        #     count_map[value] = 0
        # #? Count occurrences of elements in target array
        # for value in arr1:
        #     if value in count_map:
        #         count_map[value] += 1
        #     else:
        #         remaining.append(value)
        # #? Sort the remaining elements
        # remaining.sort()
        # #? Add elements as per relative order
        # for value in arr2:
        #     for _ in range(count_map[value]):
        #         result.append(value)
        # #? Add remaining elements
        # result.extend(remaining)
        # return result

        #! --------------------------------------------------------------------

        # arr1.sort(key=lambda x: (0, arr2.index(x)) if x in arr2 else (1, x))
        # return arr1
