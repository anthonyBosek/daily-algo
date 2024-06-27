"""
    1791. Find Center of Star Graph
    https://leetcode.com/problems/find-center-of-star-graph/

    There is an undirected star graph consisting of n nodes labeled from 1 to n.
    A star graph is a graph where there is one center node and exactly n - 1 edges
    that connect the center node with every other node.

    You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates
    that there is an edge between the nodes ui and vi. Return the center of the
    given star graph.

"""


def findCenter(edges):
    """
    :type edges: List[List[int]]
    :rtype: int
    """
    #! -- Approach 0: Set Intersection (Optimized/Copilot) --
    return (set(edges[0]) & set(edges[1])).pop()

    #! -- Approach 1: Degree Count (Brute Force) --
    # degree = {}
    # for edge in edges:
    #     degree[edge[0]] = degree.get(edge[0], 0) + 1
    #     degree[edge[1]] = degree.get(edge[1], 0) + 1

    # for node, count in degree.items():
    #     if count == len(edges):
    #         return node

    # return -1

    #! -- Approach 2: Greedy (Optimized) --
    # first_edge, second_edge = edges[0], edges[1]
    # return first_edge[0] if first_edge[0] in second_edge else first_edge[1]
