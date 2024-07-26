"""
    1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
    https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

    There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti]
    represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

    Return the city with the smallest number of cities that are reachable through some path and whose distance is at most
    distanceThreshold, If there are multiple such cities, return the city with the greatest number.

    Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

"""

from typing import List
from heapq import heappush, heappop, heapify
from collections import deque


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        adj = {i: dict() for i in range(n)}
        for u, v, d in edges:
            if d <= distanceThreshold:
                adj[u][v] = d
                adj[v][u] = d

        cities = [0] * n
        for i in range(n):
            count = -1

            distance = [float("inf")] * n
            distance[i] = 0
            visited = [False] * n

            pq = [(0, i)]
            heapify(pq)

            while pq:
                d, node = heappop(pq)
                if d > distanceThreshold:
                    break
                if visited[node]:
                    continue
                visited[node] = True
                count += 1
                for v in adj[node]:
                    if not visited[v] and d + adj[node][v] < distance[v]:
                        distance[v] = d + adj[node][v]
                        heappush(pq, (distance[v], v))
            cities[i] = count

        max_node = 0
        min_distnace = cities[0]
        for i in range(n):
            if cities[i] <= min_distnace:
                max_node = i
                min_distnace = cities[i]
        return max_node


#!Approach 1: Dijkstra Algorithm
class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # Adjacency list to store the graph
        adjacency_list = [[] for _ in range(n)]

        # Matrix to store shortest path distances from each city
        shortest_path_matrix = [[float("inf")] * n for _ in range(n)]

        # Initialize adjacency list and shortest path matrix
        for i in range(n):
            shortest_path_matrix[i][i] = 0  # Distance to itself is zero

        # Populate the adjacency list with edges
        for start, end, weight in edges:
            adjacency_list[start].append((end, weight))
            adjacency_list[end].append((start, weight))  # For undirected graph

        # Compute shortest paths from each city using Dijkstra's algorithm
        for i in range(n):
            self.dijkstra(n, adjacency_list, shortest_path_matrix[i], i)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return self.get_city_with_fewest_reachable(
            n, shortest_path_matrix, distanceThreshold
        )

    # Dijkstra's algorithm to find shortest paths from a source city
    def dijkstra(
        self,
        n: int,
        adjacency_list: List[List[tuple]],
        shortest_path_distances: List[int],
        source: int,
    ):
        # Priority queue to process nodes with the smallest distance first
        priority_queue = [(0, source)]
        shortest_path_distances[:] = [float("inf")] * n
        shortest_path_distances[source] = 0  # Distance to itself is zero

        # Process nodes in priority order
        while priority_queue:
            current_distance, current_city = heapq.heappop(priority_queue)
            if current_distance > shortest_path_distances[current_city]:
                continue

            # Update distances to neighboring cities
            for neighbor_city, edge_weight in adjacency_list[current_city]:
                if (
                    shortest_path_distances[neighbor_city]
                    > current_distance + edge_weight
                ):
                    shortest_path_distances[neighbor_city] = (
                        current_distance + edge_weight
                    )
                    heapq.heappush(
                        priority_queue,
                        (shortest_path_distances[neighbor_city], neighbor_city),
                    )

    # Determine the city with the fewest number of reachable cities within the distance threshold
    def get_city_with_fewest_reachable(
        self,
        n: int,
        shortest_path_matrix: List[List[int]],
        distance_threshold: int,
    ) -> int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n

        # Count number of cities reachable within the distance threshold for each city
        for i in range(n):
            reachable_count = sum(
                1
                for j in range(n)
                if i != j and shortest_path_matrix[i][j] <= distance_threshold
            )

            # Update the city with the fewest reachable cities
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                city_with_fewest_reachable = i
        return city_with_fewest_reachable


#! Approach 2: Bellman-Ford Algorithm
class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # Large value to represent infinity
        INF = int(1e9) + 7
        # Matrix to store shortest path distances from each city
        shortestPathMatrix = [[INF] * n for _ in range(n)]

        # Initialize shortest path matrix
        for i in range(n):
            shortestPathMatrix[i][i] = 0

        # Populate the matrix with initial edge weights
        for start, end, weight in edges:
            shortestPathMatrix[start][end] = weight
            shortestPathMatrix[end][start] = weight  # For undirected graph

        # Compute shortest paths from each city using Bellman-Ford algorithm
        for i in range(n):
            self.bellmanFord(n, edges, shortestPathMatrix[i], i)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return self.getCityWithFewestReachable(n, shortestPathMatrix, distanceThreshold)

    # Bellman-Ford algorithm to find shortest paths from a source city
    def bellmanFord(
        self,
        n: int,
        edges: List[List[int]],
        shortestPathDistances: List[int],
        source: int,
    ) -> None:
        # Initialize distances from the source
        shortestPathDistances[:] = [float("inf")] * n
        shortestPathDistances[source] = 0  # Distance to source itself is zero

        # Relax edges up to n-1 times with early stopping
        for _ in range(n - 1):
            updated = False
            for start, end, weight in edges:
                if (
                    shortestPathDistances[start] != float("inf")
                    and shortestPathDistances[start] + weight
                    < shortestPathDistances[end]
                ):
                    shortestPathDistances[end] = shortestPathDistances[start] + weight
                    updated = True
                if (
                    shortestPathDistances[end] != float("inf")
                    and shortestPathDistances[end] + weight
                    < shortestPathDistances[start]
                ):
                    shortestPathDistances[start] = shortestPathDistances[end] + weight
                    updated = True
            if not updated:
                break  # Stop early if no updates

    # Determine the city with the fewest number of reachable cities within the distance threshold
    def getCityWithFewestReachable(
        self,
        n: int,
        shortestPathMatrix: List[List[int]],
        distanceThreshold: int,
    ) -> int:
        cityWithFewestReachable = -1
        fewestReachableCount = n

        # Count number of cities reachable within the distance threshold for each city
        for i in range(n):
            reachableCount = 0
            for j in range(n):
                if i == j:
                    continue  # Skip self
                if shortestPathMatrix[i][j] <= distanceThreshold:
                    reachableCount += 1

            # Update the city with the fewest reachable cities
            if reachableCount <= fewestReachableCount:
                fewestReachableCount = reachableCount
                cityWithFewestReachable = i
        return cityWithFewestReachable


#! Approach 3: Shortest Path First Algorithm (SPFA)
class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # Adjacency list to store the graph
        adjacency_list = [[] for _ in range(n)]
        # Matrix to store shortest path distances from each city
        shortest_path_matrix = [[float("inf")] * n for _ in range(n)]

        # Initialize adjacency list and shortest path matrix
        for i in range(n):
            shortest_path_matrix[i][i] = 0  # Dist to itself is zero

        # Populate the adjacency list with edges
        for start, end, weight in edges:
            adjacency_list[start].append((end, weight))
            adjacency_list[end].append((start, weight))  # For undirected

        # Compute shortest paths from each city using SPFA algorithm
        for i in range(n):
            self.spfa(n, adjacency_list, shortest_path_matrix[i], i)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return self.get_city_with_fewest_reachable(
            n, shortest_path_matrix, distanceThreshold
        )

    # SPFA algorithm to find shortest paths from a source city
    def spfa(
        self,
        n: int,
        adjacency_list: List[List[tuple]],
        shortest_path_distances: List[int],
        source: int,
    ):
        # Queue to process nodes with updated shortest path distances
        queue = deque([source])
        update_count = [0] * n
        shortest_path_distances[:] = [float("inf")] * n
        shortest_path_distances[source] = 0  # Dist to source itself is zero

        # Process nodes in queue
        while queue:
            current_city = queue.popleft()
            for neighbor_city, edge_weight in adjacency_list[current_city]:
                if (
                    shortest_path_distances[neighbor_city]
                    > shortest_path_distances[current_city] + edge_weight
                ):
                    shortest_path_distances[neighbor_city] = (
                        shortest_path_distances[current_city] + edge_weight
                    )
                    update_count[neighbor_city] += 1
                    queue.append(neighbor_city)

                    # Detect negative weight cycles (not expected in this problem)

                    if update_count[neighbor_city] > n:
                        print("Negative weight cycle detected")

    # Determine the city with the fewest number of reachable cities within the distance threshold
    def get_city_with_fewest_reachable(
        self,
        n: int,
        shortest_path_matrix: List[List[int]],
        distance_threshold: int,
    ) -> int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n
        # Count number of cities reachable within the distance threshold for each city
        for i in range(n):
            reachable_count = sum(
                1
                for j in range(n)
                if i != j and shortest_path_matrix[i][j] <= distance_threshold
            )
            # Update the city with the fewest reachable cities
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                city_with_fewest_reachable = i

        return city_with_fewest_reachable


#! Approach 4: Floyd-Warshall Algorithm
class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # Large value to represent infinity
        INF = int(1e9 + 7)
        # Distance matrix to store shortest paths between all pairs of cities
        distance_matrix = [[INF] * n for _ in range(n)]

        # Initialize distance matrix
        for i in range(n):
            distance_matrix[i][i] = 0  # Distance to itself is zero

        # Populate the distance matrix with initial edge weights
        for start, end, weight in edges:
            distance_matrix[start][end] = weight
            distance_matrix[end][start] = weight  # For undirected graph

        # Compute shortest paths using Floyd-Warshall algorithm
        self.floyd(n, distance_matrix)

        # Find the city with the fewest number of reachable cities within the distance threshold
        return self.get_city_with_fewest_reachable(
            n, distance_matrix, distanceThreshold
        )

    # Floyd-Warshall algorithm to compute shortest paths between all pairs of cities
    def floyd(self, n: int, distance_matrix: List[List[int]]):
        # Update distances for each intermediate city

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    # Update shortest path from i to j through k
                    distance_matrix[i][j] = min(
                        distance_matrix[i][j],
                        distance_matrix[i][k] + distance_matrix[k][j],
                    )

    # Determine the city with the fewest number of reachable cities within the distance threshold
    def get_city_with_fewest_reachable(
        self, n: int, distance_matrix: List[List[int]], distance_threshold: int
    ) -> int:
        city_with_fewest_reachable = -1
        fewest_reachable_count = n

        # Count number of cities reachable within the distance threshold for each city
        for i in range(n):
            reachable_count = sum(
                1
                for j in range(n)
                if i != j and distance_matrix[i][j] <= distance_threshold
            )
            # Update the city with the fewest reachable cities
            if reachable_count <= fewest_reachable_count:
                fewest_reachable_count = reachable_count
                city_with_fewest_reachable = i
        return city_with_fewest_reachable
