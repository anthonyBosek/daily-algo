"""
    2192. All Ancestors of a Node in a Directed Acyclic Graph
    https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

    You are given a positive integer n representing the number of nodes of a Directed Acyclic Graph (DAG).
    The nodes are numbered from 0 to n - 1 (inclusive).

    You are also given a 2D integer array edges, where edges[i] = [fromi, toi] denotes that there is a
    unidirectional edge from fromi to toi in the graph.

    Return a list answer, where answer[i] is the list of ancestors of the ith node, sorted in ascending order.

    A node u is an ancestor of another node v if u can reach v via a set of edges.

"""

from typing import List
from collections import deque, defaultdict


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestors = [set() for _ in range(n)]
        incoming = [0] * (n)

        for start, end in edges:
            graph[start].append(end)
            ancestors[end].add(start)
            incoming[end] += 1

        q = deque()
        for node in range(n):
            if not incoming[node]:
                q.append(node)

        while q:
            node = q.popleft()
            for adjacent_node in graph[node]:
                ancestors[adjacent_node].update(ancestors[node])
                incoming[adjacent_node] -= 1
                if not incoming[adjacent_node]:
                    q.append(adjacent_node)

        result = []
        for node in range(n):
            result.append(sorted(ancestors[node]))
        return result


#! Approach 1: Depth First Search (Reversed Graph)
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize adjacency list for the graph
        adjacency_list = [[] for _ in range(n)]

        # Populate the adjacency list with reversed edges
        for edge in edges:
            from_node, to_node = edge
            adjacency_list[to_node].append(from_node)

        ancestors_list = []

        # For each node, find all its ancestors (children in reversed graph)
        for i in range(n):
            ancestors = []
            visited = set()
            self.find_children(i, adjacency_list, visited)
            # Add visited nodes to the current nodes' ancestor list
            for node in range(n):
                if node == i:
                    continue
                if node in visited:
                    ancestors.append(node)
            ancestors_list.append(ancestors)

        return ancestors_list

    # Helper method to perform DFS and find all children of a given node
    def find_children(self, current_node, adjacency_list, visited_nodes):
        # Mark current node as visited
        visited_nodes.add(current_node)

        # Recursively traverse all neighbors
        for neighbour in adjacency_list[current_node]:
            if neighbour not in visited_nodes:
                self.find_children(neighbour, adjacency_list, visited_nodes)


#! Approach 2: Depth First Search (Optimized)
class Solution:
    def getAncestors(self, n, edges):
        # Initialize adjacency list for each node and ancestors list
        adjacency_list = [[] for _ in range(n)]
        ancestors = [[] for _ in range(n)]

        # Populate the adjacency list with edges
        for edge in edges:
            from_node = edge[0]
            to_node = edge[1]
            adjacency_list[from_node].append(to_node)

        # Perform DFS for each node to find all its ancestors
        for i in range(n):
            self.find_ancestors_DFS(i, adjacency_list, i, ancestors)

        return ancestors

    # Helper method to perform DFS and find ancestors
    def find_ancestors_DFS(self, ancestor, adjacency_list, current_node, ancestors):
        for child_node in adjacency_list[current_node]:
            # Check if the ancestor is already added to avoid duplicates
            if not ancestors[child_node] or ancestors[child_node][-1] != ancestor:
                ancestors[child_node].append(ancestor)
                self.find_ancestors_DFS(ancestor, adjacency_list, child_node, ancestors)


#! Approach 3: Topological Sort (BFS)
class Solution:
    def getAncestors(self, n, edges):
        # Create adjacency list
        adjacency_list = [[] for _ in range(n)]

        # Fill the adjacency list and indegree array based on the edges
        indegree = [0 for _ in range(n)]
        for edge in edges:
            from_node = edge[0]
            to = edge[1]
            adjacency_list[from_node].append(to)
            indegree[to] += 1

        # Queue for nodes with no incoming edges (starting points for topological sort)
        nodes_with_zero_indegree = [i for i in range(n) if indegree[i] == 0]

        # List to store the topological order of nodes
        topological_order = []
        while nodes_with_zero_indegree:
            current_node = nodes_with_zero_indegree.pop(0)
            topological_order.append(current_node)

            # Reduce indegree of neighboring nodes and add them to the queue
            # if they have no more incoming edges
            for neighbor in adjacency_list[current_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    nodes_with_zero_indegree.append(neighbor)

        # Initialize the result list and set list for storing ancestors
        ancestors_list = [[] for _ in range(n)]
        ancestors_set_list = [set() for _ in range(n)]

        # Fill the set list with ancestors using the topological order
        for node in topological_order:
            for neighbor in adjacency_list[node]:
                # Add immediate parent, and other ancestors.
                ancestors_set_list[neighbor].add(node)
                ancestors_set_list[neighbor].update(ancestors_set_list[node])

        # Convert sets to lists and sort them
        for i in range(n):
            ancestors_list[i].extend(ancestors_set_list[i])
            ancestors_list[i].sort()

        return ancestors_list
