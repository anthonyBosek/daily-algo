"""
    2073. Time Needed to Buy Tickets
    https://leetcode.com/problems/time-needed-to-buy-tickets/

    There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the
        (n - 1)th person is at the back of the line.

    You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person
        would like to buy is tickets[i].

    Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go back
        to the end of the line (which happens instantaneously) in order to buy more tickets. If a person does not
        have any tickets left to buy, the person will leave the line.

    Return the time taken for the person at position k (0-indexed) to finish buying tickets.

"""


def timeRequiredToBuy(tickets, k):
    counter = 0

    counter = tickets[k]
    for z in range(len(tickets)):
        if z == k:
            continue
        res = tickets[z] - tickets[k]
        if res >= 0:
            counter += tickets[k]
        else:
            counter += tickets[z]

    for s in range(k + 1, len(tickets)):
        if tickets[s] >= tickets[k]:
            counter -= 1

    return counter

    # -----------------------------------------------

    # time = 0

    # for x in range(len(tickets)):
    #     if tickets[x] >= tickets[k]:
    #         time += tickets[k]
    #     elif tickets[x] < tickets[k]:
    #         time += tickets[x]

    #     if x > k and tickets[x] >= tickets[k]:
    #         time -= 1

    # return time

    # ----------------------------------------------

    # time = 0
    # while tickets[k] > 0:
    #     for i in range(len(tickets)):
    #         if tickets[i] > 0:
    #             tickets[i] -= 1
    #             time += 1
    #             if i == k and tickets[i] == 0:
    #                 return time
    # return time
