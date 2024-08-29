"""
    947. Most Stones Removed with Same Row or Column
    https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

    On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

    A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

    Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the
    largest possible number of stones that can be removed.

"""

from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(i, j)

        return n - len({find(x) for x in parent})


#! Approach 1: Depth First Search
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)

        # Adjacency list to store graph connections
        adjacency_list = [[] for _ in range(n)]

        # Build the graph: Connect stones that share the same row or column
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)

        num_of_connected_components = 0
        visited = [False] * n

        # DFS to visit all stones in a connected component
        def _depth_first_search(stone):
            visited[stone] = True
            for neighbor in adjacency_list[stone]:
                if not visited[neighbor]:
                    _depth_first_search(neighbor)

        # Traverse all stones using DFS to count connected components
        for i in range(n):
            if not visited[i]:
                _depth_first_search(i)
                num_of_connected_components += 1

        # Maximum stones that can be removed is total stones minus number of connected components
        return n - num_of_connected_components


#! Approach 2: Disjoint Set Union
class Solution:
    def removeStones(self, stones):
        n = len(stones)
        uf = self.UnionFind(n)

        # Populate uf by connecting stones that share the same row or column
        for i in range(n):
            for j in range(i + 1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf._union(i, j)

        return n - uf.count

    # Union-Find data structure for tracking connected components
    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n  # Initialize all nodes as their own parent
            self.count = n  # Initially, each stone is its own connected component

        # Find the root of a node with path compression
        def _find(self, node):
            if self.parent[node] == -1:
                return node
            self.parent[node] = self._find(self.parent[node])
            return self.parent[node]

        # Union two nodes, reducing the number of connected components
        def _union(self, n1, n2):
            root1 = self._find(n1)
            root2 = self._find(n2)

            if root1 == root2:
                return  # If they are already in the same component, do nothing

            # Merge the components and reduce the count of connected components
            self.count -= 1
            self.parent[root1] = root2


#! Approach 3: Disjoint Set Union (Optimized)
class Solution:
    def removeStones(self, stones):
        uf = self.UnionFind(
            20002
        )  # Initialize UnionFind with a large enough range to handle coordinates

        # Union stones that share the same row or column
        for x, y in stones:
            uf._union_nodes(
                x, y + 10001
            )  # Offset y-coordinates to avoid conflict with x-coordinates

        return len(stones) - uf.component_count

    # Union-Find data structure for tracking connected components
    class UnionFind:
        def __init__(self, n):
            self.parent = [-1] * n  # Initialize all nodes as their own parent
            self.component_count = 0  # Initialize the count of connected components
            self.unique_nodes = set()  # Initialize the set to track unique nodes

        # Find the root of a node with path compression
        def _find(self, node):
            # If node is not marked, increase the component count
            if node not in self.unique_nodes:
                self.component_count += 1
                self.unique_nodes.add(node)

            if self.parent[node] == -1:
                return node
            self.parent[node] = self._find(self.parent[node])
            return self.parent[node]

        # Union two nodes, reducing the number of connected components
        def _union_nodes(self, node1, node2):
            root1 = self._find(node1)
            root2 = self._find(node2)

            if root1 == root2:
                return  # If they are already in the same component, do nothing

            # Merge the components and reduce the component count
            self.parent[root1] = root2
            self.component_count -= 1
