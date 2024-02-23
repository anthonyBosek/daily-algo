"""
    787. Cheapest Flights Within K Stops
    https://leetcode.com/problems/cheapest-flights-within-k-stops/

    There are n cities connected by some number of flights. You are given an array flights where
        flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

    You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops.
        If there is no such route, return -1.

"""

from collections import defaultdict
from queue import Queue


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj = defaultdict(list)
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        dist = [float("inf")] * n
        dist[src] = 0

        q = Queue()
        q.put((src, 0))
        stops = 0

        while not q.empty() and stops <= k:
            sz = q.qsize()
            for _ in range(sz):
                node, distance = q.get()

                if node not in adj:
                    continue

                for neighbour, price in adj[node]:
                    if price + distance >= dist[neighbour]:
                        continue
                    dist[neighbour] = price + distance
                    q.put((neighbour, dist[neighbour]))

            stops += 1

        return dist[dst] if dist[dst] != float("inf") else -1

        # -------------------------------------------------------------

        # graph = defaultdict(list)
        # for u, v, w in flights:
        #     graph[u].append((v, w))

        # # Create a min heap
        # heap = [(0, src, k + 1)]

        # while heap:
        #     price, node, stops = heapq.heappop(heap)
        #     if node == dst:
        #         return price
        #     if stops > 0:
        #         for nei, w in graph[node]:
        #             heapq.heappush(heap, (price + w, nei, stops - 1))
        # return -1
