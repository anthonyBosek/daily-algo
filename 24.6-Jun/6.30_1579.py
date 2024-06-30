"""
    1579. Remove Max Number of Edges to Keep Graph Fully Traversable
    https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

    Alice and Bob have an undirected graph of n nodes and three types of edges:

        • Type 1: Can be traversed by Alice only.
        • Type 2: Can be traversed by Bob only.
        • Type 3: Can be traversed by both Alice and Bob.

    Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi,
    find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by
    both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

    Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

"""

from typing import List


#! Approach 1 (Brute Force)
class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        def find(x, parent):
            if parent[x] != x:
                parent[x] = find(parent[x], parent)
            return parent[x]

        def union(x, y, parent):
            parent[find(x, parent)] = find(y, parent)

        dsu1 = list(range(n + 1))
        dsu2 = list(range(n + 1))
        count = 0
        edges.sort(key=lambda x: x[0], reverse=True)

        for edge in edges:
            if edge[0] == 3:
                if find(edge[1], dsu1) == find(edge[2], dsu1) and find(
                    edge[1], dsu2
                ) == find(edge[2], dsu2):
                    count += 1
                    continue

                union(edge[1], edge[2], dsu1)
                union(edge[1], edge[2], dsu2)
            elif edge[0] == 1:
                if find(edge[1], dsu1) == find(edge[2], dsu1):
                    count += 1

                union(edge[1], edge[2], dsu1)
            else:
                if find(edge[1], dsu2) == find(edge[2], dsu2):
                    count += 1

                union(edge[1], edge[2], dsu2)

        for i in range(1, n + 1):
            find(i, dsu1)
            find(i, dsu2)

        for i in range(2, n + 1):
            if dsu1[i] != dsu1[1] or dsu2[i] != dsu2[1]:
                return -1

        return count


#! Approach 2 (Optimized)
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # approach: build out the graph with all the type 3 edges (no cycles)
        # for subsequent type 1 and 2 edges left, build out the
        # the graph until its fully connected
        # the maximum number of edges we can remove is the number of
        # redundant edges during graph building + number of edges left
        # after completing the graph
        # cycle detection with disjoint set

        alice_nodes = [-1] * (n + 1)
        bob_nodes = [-1] * (n + 1)

        def helper_find_parent(family, node):
            if family[node] < 0:
                return node
            family[node] = helper_find_parent(family, family[node])
            return family[node]

        num_redundant_edges = 0

        for typ, u, v in edges:
            if typ == 3:
                # add it to the graph if not redundant
                p_u = helper_find_parent(alice_nodes, u)
                p_v = helper_find_parent(alice_nodes, v)

                if p_u != p_v:
                    # we can safely join these two subsets
                    alice_nodes[p_u] += alice_nodes[p_v]
                    alice_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1
        bob_nodes = alice_nodes.copy()
        # now we build the graph for alice and bob perspectively
        for typ, u, v in edges:
            if typ == 1:
                # add it to Alice's graph
                # add it to the graph if not redundant
                p_u = helper_find_parent(alice_nodes, u)
                p_v = helper_find_parent(alice_nodes, v)

                if p_u != p_v:
                    # we can safely join these two subsets
                    alice_nodes[p_u] += alice_nodes[p_v]
                    alice_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1

            if typ == 2:
                # add it to Alice's graph
                # add it to the graph if not redundant
                p_u = helper_find_parent(bob_nodes, u)
                p_v = helper_find_parent(bob_nodes, v)

                if p_u != p_v:
                    # we can safely join these two subsets
                    bob_nodes[p_u] += bob_nodes[p_v]
                    bob_nodes[p_v] = p_u
                else:
                    num_redundant_edges += 1
        al = min(alice_nodes)
        bl = min(bob_nodes)
        if al == bl and al == -1 * n:
            return num_redundant_edges
        else:
            return -1
