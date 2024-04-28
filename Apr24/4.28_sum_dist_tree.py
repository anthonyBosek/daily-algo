"""
    834. Sum of Distances in Tree
    https://leetcode.com/problems/sum-of-distances-in-tree/

    There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

    You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

    Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

"""

from typing import List


# class Solution:
#     def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
#         graph = [[] for _ in range(n)]
#         for u, v in edges:
#             graph[u].append(v)
#             graph[v].append(u)

#         count = [1] * n
#         ans = [0] * n

#         def dfs1(node, parent):
#             for child in graph[node]:
#                 if child == parent:
#                     continue
#                 dfs1(child, node)
#                 count[node] += count[child]
#                 ans[node] += ans[child] + count[child]

#         def dfs2(node, parent):
#             for child in graph[node]:
#                 if child == parent:
#                     continue
#                 ans[child] = ans[node] - count[child] + n - count[child]
#                 dfs2(child, node)

#         dfs1(0, -1)
#         dfs2(0, -1)
#         return ans


# ---------------------------------------------------------------------------------


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        return sum_impl(n, edges)


def dfs_subtree_size(tree, u, subtree_size, depth):
    k = 1
    val = depth[u] + 1
    for v in tree[u]:
        if depth[v] is None:
            depth[v] = val
            k += dfs_subtree_size(tree, v, subtree_size, depth)
    subtree_size[u] = k
    return k


def dfs_sum(tree, u, d_subtree, dist):
    val = dist[u] + len(tree)
    for v in tree[u]:
        if dist[v] is None:
            dist[v] = val - 2 * d_subtree[v]
            dfs_sum(tree, v, d_subtree, dist)


def sum_impl(n, edges):
    assert len(edges) == n - 1
    if not edges:
        return [0]
    tree = [list() for _ in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    subtree_size = [None] * n
    depth = [None] * n
    depth[0] = 0
    dfs_subtree_size(tree, 0, subtree_size, depth)
    dist = [None] * n
    dist[0] = sum(depth)
    dfs_sum(tree, 0, subtree_size, dist)
    return dist
