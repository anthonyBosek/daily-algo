"""
    624. Maximum Distance in Arrays
    https://leetcode.com/problems/maximum-distance-in-arrays/

    You are given m arrays, where each array is sorted in ascending order.

    You can pick up two integers from two different arrays (each array picks one) and calculate the distance.
    We define the distance between two integers a and b to be their absolute difference |a - b|.

    Return the maximum distance.

"""


def maxDistance(arrays):
    """
    :type arrays: List[List[int]]
    :rtype: int
    """
    min_val = arrays[0][0]
    max_val = arrays[0][-1]
    max_diff = 0
    for i in range(1, len(arrays)):
        max_diff = max(
            max_diff, abs(arrays[i][-1] - min_val), abs(max_val - arrays[i][0])
        )
        min_val = min(min_val, arrays[i][0])
        max_val = max(max_val, arrays[i][-1])
    return max_diff


#! Fast
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mn1, mn2 = float("inf"), float("inf")
        mx1, mx2 = float("-inf"), float("-inf")
        for i in arrays:
            mn, mx = i[0], i[-1]
            if mn < mn1:
                mn2, mn1 = mn1, mn
            elif mn < mn2:
                mn2 = mn
            if mx > mx1:
                mx2, mx1 = mx1, mx
            elif mx > mx2:
                mx2 = mx
        if mx1 == mx2 or mn1 == mn2:
            return mx1 - mn1
        for i in arrays:
            if (i[0], i[-1]) == (mn1, mx1):
                return max(abs(mx2 - mn1), abs(mx1 - mn2))
        return mx1 - mn1


#! Best Memory Option 1
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_distance = 0

        while len(arrays) >= 2:
            first = arrays.pop()
            second = arrays.pop()
            # print(arrays, first, second)

            # if abs(first[0] - second[-1]) >= abs(first[-1] - second[0]):
            max_distance = max(max_distance, abs(first[0] - second[-1]))
            # arrays.append(sorted([first[0], second[-1]]))
            # else:
            max_distance = max(max_distance, abs(first[-1] - second[0]))
            # arrays.append(sorted([first[-1], second[0]]))

            arrays.append([min(first[0], second[0]), max(first[-1], second[-1])])

        return max_distance


#! Best Memory Option 2
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_distance = 0

        while len(arrays) >= 2:
            first = arrays.pop()
            second = arrays.pop()
            # print(arrays, first, second)

            # if abs(first[0] - second[-1]) >= abs(first[-1] - second[0]):
            max_distance = max(max_distance, abs(first[0] - second[-1]))
            # arrays.append(sorted([first[0], second[-1]]))
            # else:
            max_distance = max(max_distance, abs(first[-1] - second[0]))
            # arrays.append(sorted([first[-1], second[0]]))

            arrays.append([min(first[0], second[0]), max(first[-1], second[-1])])

        return max_distance
