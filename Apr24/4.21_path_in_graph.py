"""
    1971. Find if Path Exists in Graph
    https://leetcode.com/problems/find-if-path-exists-in-graph/

    There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
    The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
    Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

    You want to determine if there is a valid path that exists from vertex source to vertex destination.

    Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

"""

from typing import List
from collections import deque
from heapq import heappush


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        if source == destination:
            return True
        if [source, destination] in edges:
            return True

        outedges = [list() for _ in range(n)]
        for s, e in edges:
            heappush(outedges[s], e)
            heappush(outedges[e], s)
        del edges

        stack = deque([source])
        visited = {source}
        while stack:
            node = stack.pop()
            visited.add(node)
            if node == destination:
                return True
            for dest in outedges[node]:
                if dest not in visited:
                    stack.append(dest)

        return False

        # -------------------------------------------------

        # graph = {i: [] for i in range(n)}
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)

        # visited = set()
        # stack = [source]

        # while stack:
        #     node = stack.pop()
        #     if node == destination:
        #         return True
        #     if node in visited:
        #         continue
        #     visited.add(node)
        #     stack.extend(graph[node])

        # return False
