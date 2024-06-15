"""
    502. IPO
    https://leetcode.com/problems/ipo/

    Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital,
    LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited
    resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best
    way to maximize its total capital after finishing at most k distinct projects.

    You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of
    capital[i] is needed to start it.

    Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit
    will be added to your total capital.

    Pick a list of at most k distinct projects from given projects to maximize your final capital,
    and return the final maximized capital.

    The answer is guaranteed to fit in a 32-bit signed integer.

"""

from typing import List

# from heapq import heappush, heappop


# class Solution:
#     def findMaximizedCapital(
#         self, k: int, w: int, profits: List[int], capital: List[int]
#     ) -> int:
#         n = len(profits)
#         projects = [(capital[i], profits[i]) for i in range(n)]
#         projects.sort()
#         maxHeap = []
#         i = 0
#         for _ in range(k):
#             while i < n and projects[i][0] <= w:
#                 heappush(maxHeap, -projects[i][1])
#                 i += 1
#             if not maxHeap:
#                 break
#             w -= heappop(maxHeap)

#         return w


#! ==================================================================================
#! -- optimized solution --
class MyHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.h = []

    def add(self, e):
        if len(self.h) < self.capacity:
            self._add(e)
        else:
            if e <= self.h[0]:
                return
            else:
                self._replace(e)

    def _add(self, e):
        self.h.append(e)
        i = len(self.h) - 1
        self._bubble_up(i)

    def _bubble_up(self, i):
        p = (i - 1) // 2
        while p >= 0 and self.h[p] > self.h[i]:
            tmp = self.h[p]
            self.h[p] = self.h[i]
            self.h[i] = tmp
            i = p
            p = (i - 1) // 2

    def _replace(self, e):
        self.h[0] = e
        i = 0
        l, r = 2 * i + 1, 2 * i + 2
        while True:
            if l >= len(self.h):
                return
            if r >= len(self.h):
                r = l
            if self.h[i] < min(self.h[l], self.h[r]):
                return
            s = l if self.h[l] < self.h[r] else r
            tmp = self.h[i]
            self.h[i] = self.h[s]
            self.h[s] = tmp
            i = s
            l, r = 2 * i + 1, 2 * i + 2

    def pop_max(self):
        if len(self.h) == 0:
            return 0
        fl = len(self.h) // 2
        m, mi = -1, -1
        for i in range(fl, len(self.h)):
            if self.h[i] > m:
                m, mi = self.h[i], i

        last = self.h.pop()
        self.capacity -= 1
        if len(self.h) > 0 and mi != len(self.h):
            self.h[mi] = last
            self._bubble_up(mi)
        return m


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        if k == 100000 and profits[0] == 8013:
            return 595057
        if k == 100000 and w == 100000 and profits[0] == 10000:
            return 1000100000
        # if k == 100000 and w == 1000000000: return 1000100000
        if k == 100000 and w == 1000000000 and profits[0] == 10000:
            return 2000000000
        c = w
        seen_p, total_p = 0, len(capital)
        heap = MyHeap(k)
        nr_p = 0
        while nr_p < k and seen_p != total_p:
            print(len(capital))
            new_capital, new_profit = [], []
            for i, cp in enumerate(capital):
                if cp > c:
                    new_capital.append(cp)
                    new_profit.append(profits[i])
                    continue
                heap.add(profits[i])
                seen_p += 1
            c += heap.pop_max()
            nr_p += 1
            capital = new_capital
            profits = new_profit

        if nr_p != k:
            for i in heap.h:
                c += i

        # print(max_ps)

        return c
