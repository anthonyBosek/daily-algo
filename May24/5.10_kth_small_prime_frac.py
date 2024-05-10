"""
    786. K-th Smallest Prime Fraction
    https://leetcode.com/problems/k-th-smallest-prime-fraction/

    You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

    For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

    Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

"""


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        def con(value):
            nb_smallest_fraction = 0
            numer = arr[0]
            denom = arr[-1]

            slow = 0
            for fast in range(1, len(arr)):
                while slow < fast and arr[slow] / arr[fast] < value:
                    if arr[slow] / arr[fast] > numer / denom:
                        numer, denom = arr[slow], arr[fast]

                    slow += 1

                nb_smallest_fraction += slow

            return nb_smallest_fraction, numer, denom

        l = arr[0] / arr[-1]
        r = 1

        while l < r:
            m = (l + r) / 2

            count, numer, denom = con(m)

            if count == k:
                return [numer, denom]

            if count > k:
                r = m
            else:
                l = m

        # =========================================================================

        # left = 0
        # right = 1

        # while left < right:
        #     mid = (left + right) / 2
        #     count = 0
        #     max_fraction = [0, 1]

        #     for i in range(len(arr)):
        #         for j in range(i + 1, len(arr)):
        #             if arr[i] / arr[j] <= mid:
        #                 count += 1
        #                 if arr[i] / arr[j] > max_fraction[0] / max_fraction[1]:
        #                     max_fraction = [arr[i], arr[j]]

        #     if count == k:
        #         return max_fraction

        #     if count < k:
        #         left = mid
        #     else:
        #         right = mid

        # return max_fraction
