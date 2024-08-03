"""
    1460. Make Two Arrays Equal by Reversing Subarrays
    https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

    You are given two integer arrays of equal length target and arr. In one step,
    you can select any non-empty subarray of arr and reverse it. You are allowed
    to make any number of steps.

    Return true if you can make arr equal to target or false otherwise.

"""

from collections import Counter


#! --- My Solution ---
def canBeEqual(target, arr):
    # return sorted(target) == sorted(arr)
    return Counter(target) == Counter(arr)


#! --- LeetCode Editorial Solutions ---
#! Approach 1: Sorting
def canBeEqual(target, arr):
    arr.sort()
    target.sort()
    for i in range(len(arr)):
        if arr[i] != target[i]:
            return False
    return True


#! Approach 2: Frequency Counting With 2 Dictionaries
def canBeEqual(target, arr):
    # Dictionary to maintain frequency count for arr
    arrFreq = {}
    for num in arr:
        if num not in arrFreq:
            arrFreq[num] = 1
        else:
            arrFreq[num] += 1

    # Dictionary to maintain frequency count for arr
    targetFreq = {}
    for num in target:
        if num not in targetFreq:
            targetFreq[num] = 1
        else:
            targetFreq[num] += 1

    # Number of distinct elements of the 2 arrays are not equal
    if len(arrFreq) != len(targetFreq):
        return False

    for key in arrFreq:
        # Frequency for num differs
        if arrFreq[key] != targetFreq.get(key, 0):
            return False

    return True


#! Approach 3: Frequency Counting With 1 Dictionary
def canBeEqual(target, arr):
    # Frequency count for arr
    arrFreq = {}
    for num in arr:
        arrFreq[num] = arrFreq.get(num, 0) + 1

    for num in target:
        # If num does not appear in target, then arrays are not equal
        if num not in arrFreq:
            return False

        # Decrement the frequency count for num and
        # remove key if the count goes to 0
        arrFreq[num] -= 1
        if arrFreq[num] == 0:
            del arrFreq[num]

    return len(arrFreq) == 0
