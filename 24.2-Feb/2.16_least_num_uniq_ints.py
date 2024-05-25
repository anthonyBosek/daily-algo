"""
    1481. Least Number of Unique Integers after K Removals
    https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals

    Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

"""

from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = Counter(arr)
        counts = sorted(dic.values())

        res = 0

        for i, c in enumerate(counts):
            if k >= c:
                k -= c
            else:
                res = len(counts[i:])
                break

        return res

        # ------------------------------------------------------------

        # mp = collections.Counter(arr)
        # v = list(mp.values())
        # cnt = 0
        # v.sort()
        # for i in range(len(v)):
        #     if k > v[i]:
        #         k -= v[i]
        #         v[i] = 0
        #     else:
        #         v[i] -= k
        #         k = 0
        #     if v[i] != 0:
        #         cnt += 1
        # return cnt
