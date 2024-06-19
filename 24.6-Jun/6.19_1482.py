"""
    1482. Minimum Number of Days to Make m Bouquets
    https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

    You are given an integer array bloomDay, an integer m and an integer k.

    You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

    The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used
    in exactly one bouquet.

    Return the minimum number of days you need to wait to be able to make m bouquets from the garden.
    If it is impossible to make m bouquets return -1.

"""


# Option 1: Binary Search
class Solution:
    def get_num_of_bouquets(self, bloomDay, mid, k):
        num_of_bouquets = 0
        count = 0

        for day in bloomDay:
            # If the flower is bloomed, add to the set. Else reset the count.
            if day <= mid:
                count += 1
            else:
                count = 0

            if count == k:
                num_of_bouquets += 1
                count = 0

        return num_of_bouquets

    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        start = 0
        end = max(bloomDay)
        minDays = -1

        while start <= end:
            mid = (start + end) // 2

            if self.get_num_of_bouquets(bloomDay, mid, k) >= m:
                minDays = mid
                end = mid - 1
            else:
                start = mid + 1

        return minDays


#! ------------------------------------------------------------------------------------------------------------------
# Option 2: Binary Search
class Solution:
    def minDays(self, day, m, k):
        """
        :type day: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        def fn(day, i, m, k):
            count = 0
            countB = 0
            for value in day:
                if value <= i:
                    count += 1
                else:
                    if count >= k:
                        countB += count // k
                    count = 0
            countB += count // k
            return countB >= m

        n = len(day)
        l = min(day)
        h = max(day)
        while l <= h:
            mid = (l + h) // 2
            if fn(day, mid, m, k):
                h = mid - 1
            else:
                l = mid + 1
        if n < m * k:
            return -1
        return l


#! ------------------------------------------------------------------------------------------------------------------
# Option 3: Binary Search
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def isValid(x):
            total = 0
            currcount = 0
            for b in bloomDay:
                if x >= b:
                    currcount += 1
                else:
                    total += currcount // k
                    if total >= m:
                        return True
                    currcount = 0
            total += currcount // k
            if total >= m:
                return True

        if m * k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if isValid(mid):
                right = mid
            else:
                left = mid + 1
        return left


# TODO: Binary Search
# * The solution is to use binary search to find the minimum number of days.
# * The minimum number of days will be between the minimum and maximum days in the bloomDay array.
# * We will use the binary search to find the minimum number of days.
# * We will check if we can make m bouquets with k flowers each using the mid number of days.
# * If we can make m bouquets, we will check for the minimum number of days between the minimum and mid.
# * If we cannot make m bouquets, we will check for the minimum number of days between mid and maximum.
# * We will return the minimum number of days when the binary search is complete.
# * If the number of flowers is less than m*k, we will return -1 as it is impossible to make m bouquets.
