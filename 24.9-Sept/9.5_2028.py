"""
    2028. Find Missing Observations
    https://leetcode.com/problems/find-missing-observations/

    You have observations of n + m 6-sided dice rolls with each face numbered from 1 to 6. n of the
    observations went missing, and you only have the observations of m rolls. Fortunately, you have
    also calculated the average value of the n + m rolls.

    You are given an integer array rolls of length m where rolls[i] is the value of the ith observation.
    You are also given the two integers mean and n.

    Return an array of length n containing the missing observations such that the average value of the n + m
    rolls is exactly mean. If there are multiple valid answers, return any of them. If no such array exists,
    return an empty array.

    The average value of a set of k numbers is the sum of the numbers divided by k.

    Note that mean is an integer, so the sum of the n + m rolls should be divisible by n + m.

"""


class Solution:
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m = len(rolls)
        total = mean * (n + m) - sum(rolls)
        if total < n or total > 6 * n:
            return []
        res = [total // n] * n
        for i in range(total % n):
            res[i] += 1
        return res
        #
        # m = len(rolls)
        # total = mean * (n + m) - sum(rolls)
        # if total < n or total > 6 * n:
        #     return []
        # q, r = divmod(total, n)
        # return [q + (i < r) for i in range(n)]


#! Approach: Math
class Solution:
    def missingRolls(self, rolls, mean, n):
        # Find the sum of the rolls.
        sum_rolls = sum(rolls)
        # Find the remaining sum.
        remaining_sum = mean * (n + len(rolls)) - sum_rolls
        # Check if sum is valid or not.
        if remaining_sum > 6 * n or remaining_sum < n:
            return []
        distribute_mean = remaining_sum // n
        mod = remaining_sum % n
        # Distribute the remaining mod elements in n_elements list.
        n_elements = [distribute_mean] * n
        for i in range(mod):
            n_elements[i] += 1
        return n_elements
