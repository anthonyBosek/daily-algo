"""
    857. Minimum Cost to Hire K Workers
    https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

    There are n workers. You are given two integer arrays quality and wage where quality[i]
        is the quality of the ith worker and wage[i] is the minimum wage expectation for
        the ith worker.

    We want to hire exactly k workers to form a paid group. To hire a group of k workers,
        we must pay them according to the following rules:

            1. Every worker in the paid group must be paid at least their minimum wage expectation.

            2. In the group, each worker's pay must be directly proportional to their quality.
                This means if a worker’s quality is double that of another worker in the group,
                then they must be paid twice as much as the other worker.

    Given the integer k, return the least amount of money needed to form a paid group satisfying the
        above conditions. Answers within 10-5 of the actual answer will be accepted.

"""

# from typing import List
from heapq import heapify, heapreplace


# class Solution:
#     def mincostToHireWorkers(
#         self, quality: List[int], wage: List[int], k: int
#     ) -> float:
#         # pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])
#         # h = [-q for q, _ in pairs[:k]]
#         # heapify(h)
#         # sum_q = -sum(h)
#         # ans = sum_q * pairs[k - 1][1] / pairs[k - 1][0]
#         # for q, w in pairs[k:]:
#         #     if q < -h[0]:
#         #         sum_q += heapreplace(h, -q) + q
#         #         ans = min(ans, sum_q * w / q)
#         # return ans

#         # ----------------------------------------------------------------

#         # ratio = sorted([(w / q, q) for w, q in zip(wage, quality)])
#         # max_heap = []
#         # quality_sum = 0
#         # max_ratio = 0.0

#         # for i in range(k):
#         #     max_ratio = max(max_ratio, ratio[i][0])
#         #     quality_sum += ratio[i][1]
#         #     heapq.heappush(max_heap, -ratio[i][1])

#         # res = max_ratio * quality_sum

#         # for i in range(k, len(quality)):
#         #     max_ratio = max(max_ratio, ratio[i][0])
#         #     quality_sum += ratio[i][1] + heapq.heappop(max_heap)
#         #     heapq.heappush(max_heap, -ratio[i][1])
#         #     res = min(res, max_ratio * quality_sum)

#         # return res

#         # ----------------------------------------------------------------

#         pass


class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        qw = sorted(zip(quality, wage), key=lambda p: p[1] / float(p[0]))
        h = [-q for q, _ in qw[:k]]
        heapify(h)
        sum_q = -sum(h)
        ans = sum_q * qw[k - 1][1] / float(qw[k - 1][0])
        for q, w in qw[k:]:
            if q < -h[0]:
                sum_q += heapreplace(h, -q) + q
                ans = min(ans, sum_q * w / float(q))
        return ans
