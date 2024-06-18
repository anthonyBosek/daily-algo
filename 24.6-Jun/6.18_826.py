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
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        ans = i = best = 0
        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans

        #! --------------------------------------------------------------
        # #? Approach 1: Using Binary Search
        # job_profile = [(0, 0)]
        # for i in range(len(difficulty)):
        #     job_profile.append((difficulty[i], profit[i]))
        # #? Sort by difficulty values in increasing order.

        # job_profile.sort()
        # for i in range(len(job_profile) - 1):
        #     job_profile[i + 1] = (
        #         job_profile[i + 1][0],
        #         max(job_profile[i][1], job_profile[i + 1][1]),
        #     )
        # net_profit = 0
        # for i in range(len(worker)):
        #     ability = worker[i]

        #     #? Find the job with just smaller or equal difficulty than ability.

        #     l, r = 0, len(job_profile) - 1
        #     job_profit = 0
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if job_profile[mid][0] <= ability:
        #             job_profit = max(job_profit, job_profile[mid][1])
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     #? Increment profit of current worker to total profit.

        #     net_profit += job_profit
        # return net_profit

        #! --------------------------------------------------------------
        # #? Approach 2: Using Two Pointers
        # #? Combine difficulty and profit into a list of tuples and sort them by difficulty
        # jobs = sorted(zip(difficulty, profit))

        # #? Sort worker abilities
        # worker.sort()

        # max_profit = 0
        # best = 0
        # i = 0
        # n = len(jobs)

        # for ability in worker:
        #     #? Increase the best profit up to the current worker's ability
        #     while i < n and jobs[i][0] <= ability:
        #         best = max(best, jobs[i][1])
        #         i += 1
        #     #? Add the best profit the current worker can get
        #     max_profit += best

        # return max_profit
