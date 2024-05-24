"""
    310. Minimum Height Trees
    https://leetcode.com/problems/minimum-height-trees/

    A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words,
    any connected graph without simple cycles is a tree.

    Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates
    that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree
    as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees,
    those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

    Return a list of all MHTs' root labels. You can return the answer in any order.

    The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

"""

from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        The idea is to remove the leaf nodes layer by layer until we are left with 1 or 2 nodes.
        These nodes are the roots of the minimum height trees.

        The leaf nodes are the nodes with degree 1. So, we start with the leaf nodes and remove them from the graph.
        After removing the leaf nodes, some more nodes become leaf nodes. We continue this process until we are left
        with 1 or 2 nodes.

        The nodes left at the end are the roots of the minimum height trees.

        Time complexity: O(n), where n is the number of nodes in the graph.
        Space complexity: O(n), where n is the number of nodes in the graph.
        """

        if n == 1:
            return [0]

        # Create an adjacency list
        adj_list = [set() for _ in range(n)]
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)

        # Find the leaf nodes
        leaves = [i for i in range(n) if len(adj_list[i]) == 1]

        # Remove the leaf nodes layer by layer
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return leaves

        # -----------------------------------------------------------------------------------------------

        # if n == 1: return [0]

        # adj = [set() for _ in range(n)]
        # for u, v in edges:
        #     adj[u].add(v)
        #     adj[v].add(u)

        # leaves = [i for i in range(n) if len(adj[i]) == 1]

        # while n > 2:
        #     n -= len(leaves)
        #     new_leaves = []
        #     for leaf in leaves:
        #         neighbor = adj[leaf].pop()
        #         adj[neighbor].remove(leaf)
        #         if len(adj[neighbor]) == 1:
        #             new_leaves.append(neighbor)
        #     leaves = new_leaves

        # return leaves
