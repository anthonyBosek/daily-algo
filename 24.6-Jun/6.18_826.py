"""
    826. Most Profit Assigning Work
    https://leetcode.com/problems/most-profit-assigning-work/

    You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

        • difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
        • worker[j] is the ability of jth worker (i.e., the jth worker can only complete a
            job with difficulty at most worker[j]).

    Every worker can be assigned at most one job, but one job can be completed multiple times.

        • For example, if three workers attempt the same job that pays $1, then the total profit
            will be $3. If a worker cannot complete any job, their profit is $0.

    Return the maximum profit we can achieve after assigning the workers to the jobs.

"""

from typing import List


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        pass
