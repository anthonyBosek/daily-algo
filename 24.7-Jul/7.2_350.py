"""
    350. Intersection of Two Arrays II
    https://leetcode.com/problems/intersection-of-two-arrays-ii/

    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must appear as many times as it shows in both arrays
    and you may return the result in any order.

"""


def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    dict1 = {}
    dict2 = {}
    for num in nums1:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1
    for num in nums2:
        if num in dict2:
            dict2[num] += 1
        else:
            dict2[num] = 1
    result = []
    for key in dict1:
        if key in dict2:
            result += [key] * min(dict1[key], dict2[key])
    return result

    #! --- mine ---
    # result = []
    # for n in nums1:
    #     if n in nums2:
    #         nums2.remove(n)
    #         result.append(n)

    # return result

    #! ----------------------------------------------------------------------------
    # intersection = []
    # nums1.sort()
    # nums2.sort()
    # i = 0
    # for num in nums1:
    #     if i >= len(nums2):
    #         break
    #     while i < len(nums2) - 1 and nums2[i] < num:
    #         i += 1
    #     if nums2[i] == num:
    #         i += 1
    #         intersection.append(num)

    # return intersection

    #! ----------------------------------------------------------------------------
    # # Create a hashtable
    # table = {}
    # for number in nums1:
    #     table[number] = table.get(number, 0) + 1
    # # Instantiate an empty list for result
    # res = []
    # for num in nums2:
    #     if num in table:
    #         if table[num] > 0:
    #             res.append(num)
    #             table[num] = table[num] - 1
    # return res

    #! ----------------------------------------------------------------------------
    # # Count the occurrences of each number in nums1
    # count = Counter(nums1)

    # ans = []

    # # Check each number in nums2
    # for num in nums2:
    #     if count[num] > 0:
    #         ans.append(num)
    #         count[num] -= 1

    # return ans
