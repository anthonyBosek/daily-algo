"""
    514. Freedom Trail
    https://leetcode.com/problems/freedom-trail/

    In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring",
    and use the dial to spell a specific keyword in order to open the door.

    Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword
    needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.

    Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key
    one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction
    and then by pressing the center button.

    At the stage of rotating the ring to spell the key character key[i]:

        1. You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is
        to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].

        2. If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also
        counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise,
        you've finished all the spelling.

"""

from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        rlen, klen, d = len(ring), len(key), defaultdict(list)
        dist = lambda x, y: min((x - y) % rlen, (y - x) % rlen)

        for i, ch in enumerate(ring):
            d[ch].append(i)
        # print(d)
        # defaultdict(<class 'list'>, {'g': [0, 6], 'o': [1], 'd': [2, 3], 'i': [4], 'n': [5]})

        @lru_cache(None)
        def dfs(curr=0, next=0):
            if next >= klen:
                return 0

            return min(dist(curr, k) + dfs(k, next + 1) for k in d[key[next]])

        return dfs() + klen

        # ----------------------------------------------------------------------------------------

        # n = len(ring)
        # matches = {}
        # for i in range(n):
        #     matches.setdefault(ring[i], []).append(i)

        # pos_cost = [(0, 0)]
        # for ch in key:
        #     pos_cost_curr = []
        #     for curr_pos in matches[ch]:
        #         curr_cost = float('inf')
        #         for pos, cost in pos_cost:
        #             clkwise_trans_cost = abs(pos - curr_pos)
        #             temp_cost = cost + min(clkwise_trans_cost, n - clkwise_trans_cost)
        #             curr_cost = min(curr_cost, temp_cost)
        #         pos_cost_curr.append((curr_pos, curr_cost))
        #     pos_cost = pos_cost_curr

        # min_cost = float('inf')
        # for pos, cost in pos_cost:
        #     min_cost = min(min_cost, cost)

        # return min_cost + len(key)

        # ----------------------------------------------------------------------------------------

        # ----- pass some, but not all test cases --------
        # def dp(i, j):
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     if i == len(key):
        #         return 0
        #     res = float('inf')
        #     for k in pos[key[i]]:
        #         diff = abs(j - k)
        #         res = min(res, diff + dp(i + 1, k))
        #     memo[(i, j)] = res
        #     return res

        # pos = {}
        # for i, c in enumerate(ring):
        #     if c not in pos:
        #         pos[c] = []
        #     pos[c].append(i)

        # memo = {}
        # return len(key) + dp(0, 0)
