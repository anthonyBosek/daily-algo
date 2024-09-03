"""
    2699. Modify Graph Edge Weights
    https://leetcode.com/problems/modify-graph-edge-weights/

    You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1,
    and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between
    nodes ai and bi with weight wi.

    Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

    Your task is to modify all edges with a weight of -1 by assigning them positive integer values in
    the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes
    equal to an integer target. If there are multiple modifications that make the shortest distance between
    source and destination equal to target, any of them will be considered correct.

    Return an array containing all edges (even unmodified ones) in any order if it is possible to make the
    shortest distance from source to destination equal to target, or an empty array if it's impossible.

    Note: You are not allowed to modify the weights of edges with initial positive weights.

"""

from typing import List, Tuple
from collections import defaultdict
import heapq, math, json, sys


class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        adjacency_list = [[] for _ in range(n)]
        for i, (nodeA, nodeB, weight) in enumerate(edges):
            adjacency_list[nodeA].append((nodeB, i))
            adjacency_list[nodeB].append((nodeA, i))

        distances = [[float("inf")] * 2 for _ in range(n)]
        distances[source][0] = distances[source][1] = 0

        self.run_dijkstra(adjacency_list, edges, distances, source, 0, 0)
        difference = target - distances[destination][0]

        if difference < 0:
            return []

        self.run_dijkstra(adjacency_list, edges, distances, source, difference, 1)

        if distances[destination][1] < target:
            return []

        for edge in edges:
            if edge[2] == -1:
                edge[2] = 1

        return edges

    def run_dijkstra(self, adjacency_list, edges, distances, source, difference, run):
        n = len(adjacency_list)
        priority_queue = [(0, source)]
        distances[source][run] = 0

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > distances[current_node][run]:
                continue

            for next_node, edge_index in adjacency_list[current_node]:
                weight = edges[edge_index][2]
                if weight == -1:
                    weight = 1
                if run == 1 and edges[edge_index][2] == -1:
                    new_weight = (
                        difference
                        + distances[next_node][0]
                        - distances[current_node][1]
                    )
                    if new_weight > weight:
                        edges[edge_index][2] = weight = new_weight

                if distances[next_node][run] > distances[current_node][run] + weight:
                    distances[next_node][run] = distances[current_node][run] + weight
                    heapq.heappush(
                        priority_queue, (distances[next_node][run], next_node)
                    )


def main():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()

    num_test_cases = len(lines) // 5
    results = []

    for i in range(num_test_cases):
        n = int(lines[i * 5])
        edges = json.loads(lines[i * 5 + 1])
        source = int(lines[i * 5 + 2])
        destination = int(lines[i * 5 + 3])
        target = int(lines[i * 5 + 4])

        result = Solution().modifiedGraphEdges(n, edges, source, destination, target)
        results.append(json.dumps(result))

    with open("user.out", "w") as f:
        for result in results:
            f.write(f"{result}\n")


if __name__ == "__main__":
    main()
    exit(0)

# https://leetcode.com/problems/modify-graph-edge-weights/submissions/1368714331/


#! Approach 1: Traditional Dijkstra's algorithm
from typing import List


class Solution:
    INF = int(2e9)

    def modifiedGraphEdges(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        target: int,
    ) -> List[List[int]]:
        # Step 1: Compute the initial shortest distance from source to destination
        current_shortest_distance = self.run_dijkstra(edges, n, source, destination)

        # If the current shortest distance is less than the target, return an empty result
        if current_shortest_distance < target:
            return []
        matches_target = current_shortest_distance == target

        # Step 2: Iterate through each edge to adjust its weight if necessary
        for edge in edges:
            # Skip edges that already have a positive weight
            if edge[2] > 0:
                continue

            # Set edge weight to a large value if current distance matches target, else set to 1
            edge[2] = self.INF if matches_target else 1

            # Step 3: If current shortest distance does not match target
            if not matches_target:
                # Compute the new shortest distance with the updated edge weight
                new_distance = self.run_dijkstra(edges, n, source, destination)
                # If the new distance is within the target range, update edge weight to match target
                if new_distance <= target:
                    matches_target = True
                    edge[2] += target - new_distance

        # Return modified edges if the target distance is achieved, otherwise return an empty result
        return edges if matches_target else []

    def run_dijkstra(
        self, edges: List[List[int]], n: int, source: int, destination: int
    ) -> int:
        # Step 1: Initialize adjacency matrix and distance arrays
        adj_matrix = [[self.INF] * n for _ in range(n)]
        min_distance = [self.INF] * n
        visited = [False] * n

        # Set the distance to the source node as 0
        min_distance[source] = 0

        # Step 2: Fill the adjacency matrix with edge weights
        for nodeA, nodeB, weight in edges:
            if weight != -1:
                adj_matrix[nodeA][nodeB] = weight
                adj_matrix[nodeB][nodeA] = weight

        # Step 3: Perform Dijkstra's algorithm
        for _ in range(n):
            # Find the nearest unvisited node
            nearest_unvisited_node = -1
            for i in range(n):
                if not visited[i] and (
                    nearest_unvisited_node == -1
                    or min_distance[i] < min_distance[nearest_unvisited_node]
                ):
                    nearest_unvisited_node = i

            # Mark the nearest node as visited
            visited[nearest_unvisited_node] = True

            # Update the minimum distance for each adjacent node
            for v in range(n):
                min_distance[v] = min(
                    min_distance[v],
                    min_distance[nearest_unvisited_node]
                    + adj_matrix[nearest_unvisited_node][v],
                )
        # Return the shortest distance to the destination node
        return min_distance[destination]


#! Approach 2: Dijkstra's Algorithm with Min-Heap
class Solution:
    def modifiedGraphEdges(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        target: int,
    ) -> List[List[int]]:
        INF = int(2e9)
        graph = [[] for _ in range(n)]

        # Build the graph with known weights
        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        # Compute the initial shortest distance
        current_shortest_distance = self._dijkstra(graph, source, destination)
        if current_shortest_distance < target:
            return []

        if current_shortest_distance == target:
            # Update edges with -1 weight to an impossible value
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges

        # Adjust edges with unknown weights
        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue

            # Set edge weight to 1 initially
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))

            # Recompute shortest distance with updated edge weight
            new_distance = self._dijkstra(graph, source, destination)

            if new_distance <= target:
                edges[i][2] += target - new_distance

                # Update remaining edges with -1 weight to an impossible value
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = INF
                return edges
        return []

    def _dijkstra(
        self, graph: List[List[Tuple[int, int]]], src: int, destination: int
    ) -> int:
        min_distance = [math.inf] * len(graph)
        min_distance[src] = 0
        min_heap = [(0, src)]  # (distance, node)

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > min_distance[u]:
                continue
            for v, w in graph[u]:
                if d + w < min_distance[v]:
                    min_distance[v] = d + w
                    heapq.heappush(min_heap, (min_distance[v], v))
        return min_distance[destination]
