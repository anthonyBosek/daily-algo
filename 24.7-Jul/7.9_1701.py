"""
    1701. Average Waiting Time
    https://leetcode.com/problems/average-waiting-time/

    There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

        - arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
        - timei is the time needed to prepare the order of the ith customer.

    When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle.
    The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time.
    The chef prepares food for customers in the order they were given in the input.

    Return the average waiting time of all customers. Solutions within 10^-5 from the actual answer are considered accepted.

"""

from typing import List
from sys import maxsize


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        wait = 0
        e = -maxsize
        for val in customers:
            arrive, time = val
            if arrive < e:  # no one shows up at -9gazillion
                # so we use this to determine if this is their first time or not
                wait += e - arrive + time
                e += time
            else:
                wait += time
                e = arrive + time
        return wait / n


#! -----------------------------------------------------------------------


#! Approach: Simulation
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        next_idle_time = 0
        net_wait_time = 0

        for customer in customers:
            # The next idle time for the chef is given by the time of delivery
            # of current customer's order.
            next_idle_time = max(customer[0], next_idle_time) + customer[1]

            # The wait time for the current customer is the difference between
            # his delivery time and arrival time.
            net_wait_time += next_idle_time - customer[0]

        # Divide by total customers to get average.
        average_wait_time = net_wait_time / len(customers)
        return average_wait_time
