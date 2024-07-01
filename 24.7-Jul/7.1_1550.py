"""
    1550. Three Consecutive Odds
    https://leetcode.com/problems/three-consecutive-odds/

    Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

"""


def threeConsecutiveOdds(arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    #! my solution
    cnt = 0
    for i in arr:
        if i % 2 != 0:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            return True

    return False

    #! copilot solution
    # for i in range(len(arr) - 2):
    #     if arr[i] % 2 != 0 and arr[i + 1] % 2 != 0 and arr[i + 2] % 2 != 0:
    #         return True
    # return False

    #! another solution
    # i = 0
    # for x in arr:
    #     if x & 1:
    #         i += 1
    #     else:
    #         i = 0
    #     if i > 2:
    #         return True
    #     print(i)
    # return False
