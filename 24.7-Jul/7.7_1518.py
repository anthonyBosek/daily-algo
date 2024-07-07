"""
    1518. Water Bottles
    https://leetcode.com/problems/water-bottles/

    There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water
    bottles from the market with one full water bottle.

    The operation of drinking a full water bottle turns it into an empty bottle.

    Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

"""


def numWaterBottles(numBottles, numExchange):
    """
    :type numBottles: int
    :type numExchange: int
    :rtype: int
    """
    # total = numBottles
    # while numBottles >= numExchange:
    #     total += numBottles // numExchange
    #     numBottles = numBottles // numExchange + numBottles % numExchange
    # return total

    empty = 0
    drank = 0
    while numBottles:
        drank += 1
        empty += 1
        numBottles -= 1
        if empty == numExchange:
            empty -= numExchange
            numBottles += 1
    return drank


#! Approach 1: Simulation
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed_bottles = 0

        while numBottles >= numExchange:
            # Consume numExchange full bottles.
            consumed_bottles += numExchange
            numBottles -= numExchange

            # Exchange them for one full bottle.
            numBottles += 1

        # Consume the remaining numBottles (less than numExchange).
        return consumed_bottles + numBottles


#! Approach 2: Optimized Simulation
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        consumed_bottles = 0

        while numBottles >= numExchange:
            # Maximum number of times we can consume numExchange
            # number of bottles using numBottles.
            K = numBottles // numExchange

            consumed_bottles += numExchange * K
            numBottles -= numExchange * K

            numBottles += K

        return consumed_bottles + numBottles
