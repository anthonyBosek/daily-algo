"""
    2392. Build a Matrix With Conditions
    https://leetcode.com/problems/build-a-matrix-with-conditions/

    You are given a positive integer k. You are also given:

        • a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
        • a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].

    The two arrays contain integers from 1 to k.

    You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

    The matrix should also satisfy the following conditions:

        • The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
        • The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.

    Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.

"""

from typing import List


class Solution:
    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        pass


#! Approach 1: Depth-First Search
class Solution:
    def buildMatrix(
        self,
        k: int,
        rowConditions: List[List[int]],
        colConditions: List[List[int]],
    ) -> List[List[int]]:
        # Store the topologically sorted sequences.
        order_rows = self.__topoSort(rowConditions, k)
        order_columns = self.__topoSort(colConditions, k)

        # If no topological sort exists, return empty array.
        if not order_rows or not order_columns:
            return []
        matrix = [[0] * k for _ in range(k)]
        pos_row = {num: i for i, num in enumerate(order_rows)}
        pos_col = {num: i for i, num in enumerate(order_columns)}

        for num in range(1, k + 1):
            if num in pos_row and num in pos_col:
                matrix[pos_row[num]][pos_col[num]] = num
        return matrix

    def __topoSort(self, edges: List[List[int]], n: int) -> List[int]:
        adj = defaultdict(list)
        order = []
        visited = [0] * (n + 1)
        has_cycle = [False]

        # Build adjacency list
        for x, y in edges:
            adj[x].append(y)
        # Perform DFS for each node
        for i in range(1, n + 1):
            if visited[i] == 0:
                self.__dfs(i, adj, visited, order, has_cycle)
                # Return empty if cycle detected
                if has_cycle[0]:
                    return []
        # Reverse to get the correct order
        order.reverse()
        return order

    def __dfs(
        self,
        node: int,
        adj: defaultdict,
        visited: List[int],
        order: List[int],
        has_cycle: List[bool],
    ):
        # Mark node as visiting
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                self.__dfs(neighbor, adj, visited, order, has_cycle)
                # Early exit if a cycle is detected
                if has_cycle[0]:
                    return
            elif visited[neighbor] == 1:
                # Cycle detected
                has_cycle[0] = True
                return
        # Mark node as visited
        visited[node] = 2
        # Add node to the order
        order.append(node)


#! Approach 2: Kahn's Algorithm
from collections import deque, defaultdict


class Solution:
    def buildMatrix(
        self,
        k: int,
        row_conditions: List[List[int]],
        col_conditions: List[List[int]],
    ) -> List[List[int]]:
        order_rows = self.__topo_sort(row_conditions, k)
        order_columns = self.__topo_sort(col_conditions, k)
        if not order_rows or not order_columns:
            return []
        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            for j in range(k):
                if order_rows[i] == order_columns[j]:
                    matrix[i][j] = order_rows[i]
        return matrix

    def __topo_sort(self, edges, n):
        adj = [[] for _ in range(n + 1)]
        deg = [0] * (n + 1)
        order = []
        for x in edges:
            adj[x[0]].append(x[1])
            deg[x[1]] += 1
        q = deque()
        for i in range(1, n + 1):
            if deg[i] == 0:
                q.append(i)
        while q:
            f = q.popleft()
            order.append(f)
            n -= 1
            for v in adj[f]:
                deg[v] -= 1
                if deg[v] == 0:
                    q.append(v)
        if n != 0:
            return []
        return order
