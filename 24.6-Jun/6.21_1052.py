"""
    1052. Grumpy Bookstore Owner
    https://leetcode.com/problems/grumpy-bookstore-owner/

    There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers
    enter the store. You are given an integer array customers of length n where customers[i] is the number
    of the customer that enters the store at the start of the ith minute and all those customers leave
    after the end of that minute.

    On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1
    if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

    When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise,
    they are satisfied.

    The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes,
    but can only use it once.

    Return the maximum number of customers that can be satisfied throughout the day.

"""

from typing import List


class Solution:
    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        # runtime: 1597 ms
        # memory: 168.6 MB
        #
        n = len(customers)
        satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]
                customers[i] = 0

        max_satisfied = 0
        for i in range(n - minutes + 1):
            max_satisfied = max(max_satisfied, sum(customers[i : i + minutes]))

        return satisfied + max_satisfied

        #! ------------------------------------------------------------------------

        # runtime: 210 ms
        # memory: 19.2 MB
        #
        # n = len(customers)
        # unrealized_customers = 0

        # #? Calculate initial number of unrealized customers in first 'minutes' window
        # for i in range(minutes):
        #     unrealized_customers += customers[i] * grumpy[i]

        # max_unrealized_customers = unrealized_customers

        # #? Slide the 'minutes' window across the rest of the customers array
        # for i in range(minutes, n):
        #     # Add current minute's unsatisfied customers if the owner is grumpy
        #     # and remove the customers that are out of the current window
        #     unrealized_customers += customers[i] * grumpy[i]
        #     unrealized_customers -= customers[i - minutes] * grumpy[i - minutes]

        #     # Update the maximum unrealized customers
        #     max_unrealized_customers = max(
        #         max_unrealized_customers, unrealized_customers
        #     )

        # #? Start with maximum possible satisfied customers due to secret technique
        # total_customers = max_unrealized_customers

        # #? Add the satisfied customers during non-grumpy minutes
        # for i in range(n):
        #     total_customers += customers[i] * (1 - grumpy[i])

        # #? Return the maximum number of satisfied customers
        # return total_customers

        #! ------------------------------------------------------------------------
