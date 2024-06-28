"""
    2285. Maximum Total Importance of Roads
    https://leetcode.com/problems/maximum-total-importance-of-roads/

    You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.

    You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional
    road connecting cities ai and bi.

    You need to assign each city with an integer value from 1 to n, where each value can only be used once. The
    importance of a road is then defined as the sum of the values of the two cities it connects.

    Return the maximum total importance of all roads possible after assigning the values optimally.

"""

from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n

        for edge in roads:
            degree[edge[0]] += 1
            degree[edge[1]] += 1

        degree.sort()

        value = 1
        total_importance = 0
        for d in degree:
            total_importance += value * d
            value += 1

        return total_importance

        #! ---------------------------------------------------
        # Arr = [0] * n  # i-th city has Arr[i] roads
        # for A, B in roads:
        #     Arr[A] += 1  # Each road increase the road count
        #     Arr[B] += 1
        # Arr.sort()  # Cities with most road should receive the most score
        # summ = 0
        # for i in range(len(Arr)):
        #     summ += Arr[i] * (i + 1)  # Multiply city roads with corresponding score

        # return summ
