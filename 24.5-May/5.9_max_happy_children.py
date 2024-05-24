"""
    3075. Maximize Happiness of Selected Children
    https://leetcode.com/problems/maximize-happiness-of-selected-children/

    You are given an array happiness of length n, and a positive integer k.

    There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select
        k children from these n children in k turns.

    In each turn, when you select a child, the happiness value of all the children that have not been selected till now
        decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

    Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

"""

from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sort_happy = sorted(happiness)
        happiness = 0
        for i in range(k):
            val = sort_happy.pop() - i
            if val <= 0:
                return happiness
            happiness += val
        return happiness

        # -------------------------------------------------------------

        # happiness.sort(reverse=True)
        # i = 0
        # res = 0

        # while k > 0:
        #     happiness[i] = max(happiness[i] - i, 0)
        #     res += happiness[i]
        #     i += 1
        #     k -= 1

        # return res
