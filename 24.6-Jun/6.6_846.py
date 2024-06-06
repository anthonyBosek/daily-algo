"""
    846. Hand of Straights
    https://leetcode.com/problems/hand-of-straights/

    Alice has some number of cards and she wants to rearrange the cards into groups so
    that each group is of size groupSize, and consists of groupSize consecutive cards.

    Given an integer array hand where hand[i] is the value written on the ith card and
    an integer groupSize, return true if she can rearrange the cards, or false otherwise.

"""

from typing import List
from collections import defaultdict, deque
from heapq import heapify, heappop


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) % groupSize != 0:
        #     return False

        # hand.sort()
        # hand_dict = {}
        # for card in hand:
        #     hand_dict[card] = hand_dict.get(card, 0) + 1

        # for card in hand:
        #     if hand_dict[card] == 0:
        #         continue
        #     for i in range(groupSize):
        #         if hand_dict.get(card + i, 0) == 0:
        #             return False
        #         hand_dict[card + i] -= 1

        # return True

        # -------------------------------------------------------------

        # handCounter = defaultdict(int)
        # for val in hand:
        #     handCounter[val] += 1

        # allKeys = list(handCounter.keys())
        # heapify(allKeys)

        # while allKeys:
        #     cur = allKeys[0]

        #     for i in range(cur, cur + groupSize):
        #         if i not in handCounter:
        #             return False
        #         handCounter[i] -= 1
        #         if handCounter[i] == 0:
        #             if i != allKeys[0]:
        #                 return False
        #             heappop(allKeys)

        # return True

        # -------------------------------------------------------------

        hand.sort()
        dq = deque([])

        for card in hand:
            if len(dq) > 0:
                if dq[-1][1] == card - 1:
                    item = dq.pop()
                    item[0] += 1
                    item[1] = card
                elif dq[-1][1] == card:
                    item = [1, card]
                else:
                    return False
            else:
                item = [1, card]

            if item[0] < groupSize:
                dq.appendleft(item)

        return len(dq) == 0
