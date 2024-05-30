"""
    1442. Count Triplets That Can Form Two Arrays of Equal XOR
    https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

    Given an array of integers arr.

    We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

    Let's define a and b as follows:

        • a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
        • b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]

    Note that ^ denotes the bitwise-xor operation.

    Return the number of triplets (i, j and k) Where a == b.

"""

from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for i in range(n):
            xor = arr[i]
            for k in range(i + 1, n):
                xor ^= arr[k]
                if xor == 0:
                    res += k - i
        return res

    # ---------------------------------------------

    # def countTriplets(self, arr: List[int]) -> int:
    #     pre = []
    #     p = 0
    #     res = 0
    #     n = len(arr)

    #     for i in arr:
    #         p ^= i
    #         pre.append(p)

    #     for i in range(n):
    #         for k in range(i + 1, n):
    #             # print(i, k, pre[k] - (pre[i - 1] if i > 0 else 0))
    #             if pre[k] - (pre[i - 1] if i > 0 else 0) == 0:
    #                 res += k - i

    #     return res
