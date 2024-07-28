"""
    2045. Second Minimum Time to Reach Destination
    https://leetcode.com/problems/second-minimum-time-to-reach-destination/

    A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive).
    The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional
    edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
    The time taken to traverse any edge is time minutes.

    Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes.
    All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green.
    You cannot wait at a vertex if the signal is green.

    The second minimum value is defined as the smallest value strictly larger than the minimum value.

    For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.
    Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

    Notes:
        - You can go through any vertex any number of times, including 1 and n.
        - You can assume that when the journey starts, all signals have just turned green.

"""

from typing import List
from collections import deque


class Solution:
    def secondMinimum(
        self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        q = deque([(1, 1)])
        dist1 = [-1] * (n + 1)
        dist2 = [-1] * (n + 1)
        dist1[1] = 0
        while q:
            x, freq = q.popleft()
            t = dist1[x] if freq == 1 else dist2[x]
            if (t // change) % 2:
                t = change * (t // change + 1) + time
            else:
                t += time
            for y in g[x]:
                if dist1[y] == -1:
                    dist1[y] = t
                    q.append((y, 1))
                elif dist2[y] == -1 and dist1[y] != t:
                    if y == n:
                        return t
                    dist2[y] = t
                    q.append((y, 2))
        return 0

        #! ------------------------------------------------------------------------------------------

        # # Create the graph using a defaultdict of lists
        # g = defaultdict(list)
        # for u, v in edges:
        #     g[u].append(v)
        #     g[v].append(u)

        # # Priority queue for Dijkstra's algorithm
        # q = []
        # heapq.heappush(q, (0, 1))  # (time, node)

        # uniqueVisit = [0] * (n + 1)  # To track the number of unique visits
        # dis = [-1] * (n + 1)  # To store the minimum time to reach each node

        # while q:
        #     t, node = heapq.heappop(q)  # Get the node with the smallest time

        #     if dis[node] == t or uniqueVisit[node] >= 2:
        #         continue  # Skip if already visited or relaxed twice

        #     uniqueVisit[node] += 1
        #     dis[node] = t

        #     if node == n and uniqueVisit[node] == 2:
        #         return dis[node]

        #     # Calculate the leaving time (waiting for the green light)
        #     if (t // change) % 2 != 0:
        #         t = (t // change + 1) * change

        #     for nei in g[node]:
        #         heapq.heappush(q, (t + time, nei))

        # return -1


#! Approach 1: Dijkstra
#! in JAVA
# class Solution {
#     public int secondMinimum(int n, int[][] edges, int time, int change) {
#         Map<Integer, List<Integer>> adj = new HashMap<>();
#         for (int[] edge : edges) {
#             int a = edge[0], b = edge[1];
#             adj.computeIfAbsent(a, value -> new ArrayList<Integer>()).add(b);
#             adj.computeIfAbsent(b, value -> new ArrayList<Integer>()).add(a);
#         }
#         int[] dist1 = new int[n + 1], dist2 = new int[n + 1], freq = new int[n + 1];
#         #? // dist1[i] stores the minimum time taken to reach node i from node 1. dist2[i]
#         #? // stores the second minimum time taken to reach node from node 1. freq[i] stores
#         #? // the number of times a node is popped out of the heap.
#         for (int i = 1; i <= n; i++) {
#             dist1[i] = dist2[i] = Integer.MAX_VALUE;
#             freq[i] = 0;
#         }

#         PriorityQueue<int []> pq = new PriorityQueue<>((a, b) -> (a[1] - b[1]));
#         pq.offer(new int[] {1, 0});
#         dist1[1] = 0;

#         while (!pq.isEmpty()) {
#             int [] temp = pq.poll();
#             int node = temp[0];
#             int time_taken = temp[1];

#             freq[node]++;

#             #? // If the node is being visited for the second time and is 'n', return the
#             #? // answer.
#             if (freq[node] == 2 && node == n)
#                 return time_taken;
#             #? // If the current light is red, wait till the path turns green.
#             if ((time_taken / change) % 2 == 1)
#                 time_taken = change * (time_taken / change + 1) + time;
#             else
#                 time_taken = time_taken + time;

#             if (!adj.containsKey(node))
#                 continue;
#             for (int neighbor : adj.get(node)) {
#                 #? // Ignore nodes that have already popped out twice, we are not interested in
#                 #? // visiting them again.
#                 if (freq[neighbor] == 2)
#                     continue;

#                 #? // Update dist1 if it's more than the current time_taken and store its value in
#                 #? // dist2 since that becomes the second minimum value now.
#                 if (dist1[neighbor] > time_taken) {
#                     dist2[neighbor] = dist1[neighbor];
#                     dist1[neighbor] = time_taken;
#                     pq.offer(new int [] {neighbor, time_taken});
#                 } else if (dist2[neighbor] > time_taken && dist1[neighbor] != time_taken) {
#                     dist2[neighbor] = time_taken;
#                     pq.offer(new int[] {neighbor, time_taken});
#                 }
#             }

#         }
#         return 0;
#     }
# }

#! Approach 2: Breadth First Search
#! in JAVA
# class Solution {
#     public int secondMinimum(int n, int[][] edges, int time, int change) {
#         Map<Integer, List<Integer>> adj = new HashMap<>();
#         for (int[] edge : edges) {
#             int a = edge[0], b = edge[1];
#             adj.computeIfAbsent(a, value -> new ArrayList<Integer>()).add(b);
#             adj.computeIfAbsent(b, value -> new ArrayList<Integer>()).add(a);
#         }
#         int[] dist1 = new int[n + 1], dist2 = new int[n + 1];
#         for (int i = 1; i <= n; i++) {
#             dist1[i] = dist2[i] = -1;
#         }
#         Queue<int[]> queue = new LinkedList<>();
#         #? // Start with node 1, with its minimum distance.
#         queue.offer(new int[] { 1, 1 });
#         dist1[1] = 0;

#         while (!queue.isEmpty()) {
#             int[] temp = queue.poll();
#             int node = temp[0];
#             int freq = temp[1];

#             int timeTaken = freq == 1 ? dist1[node] : dist2[node];
#             #? // If the time_taken falls under the red bracket, wait till the path turns
#             #? // green.
#             if ((timeTaken / change) % 2 == 1) {
#                 timeTaken = change * (timeTaken / change + 1) + time;
#             } else {
#                 timeTaken = timeTaken + time;
#             }

#             if (!adj.containsKey(node))
#                 continue;
#             for (int neighbor : adj.get(node)) {
#                 if (dist1[neighbor] == -1) {
#                     dist1[neighbor] = timeTaken;
#                     queue.offer(new int[] { neighbor, 1 });
#                 } else if (dist2[neighbor] == -1 && dist1[neighbor] != timeTaken) {
#                     if (neighbor == n)
#                         return timeTaken;
#                     dist2[neighbor] = timeTaken;
#                     queue.offer(new int[] { neighbor, 2 });
#                 }
#             }

#         }
#         return 0;
#     }
# }
