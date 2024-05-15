"""
    2812. Find the Safest Path in a Grid
    https://leetcode.com/problems/find-the-safest-path-in-a-grid/

    You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

        • A cell containing a thief if grid[r][c] = 1
        • An empty cell if grid[r][c] = 0

    You are initially positioned at cell (0, 0). In one move, you can move to any
        adjacent cell in the grid, including cells containing thieves.

    The safeness factor of a path on the grid is defined as the minimum manhattan
        distance from any cell in the path to any thief in the grid.

    Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

    An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1),
        (r + 1, c) and (r - 1, c) if it exists.

    The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|,
        where |val| denotes the absolute value of val.

"""

# from typing import List
from collections import deque
from heapq import heappop, heappush


def maximumSafenessFactor(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    row, col = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[row - 1][col - 1] == 1:
        return 0
    safeness = [[-1] * col for _ in range(row)]
    q = deque([])

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                safeness[r][c] = 0
                q.append((0, r, c))

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        dis, r, c = q.popleft()
        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and safeness[nr][nc] == -1:
                safeness[nr][nc] = dis + 1
                q.append((dis + 1, nr, nc))

    heap = [(-safeness[row - 1][col - 1], row - 1, col - 1)]
    seen = set([(row - 1, col - 1)])

    while heap:
        dis, r, c = heappop(heap)
        if (r, c) == (0, 0):
            return -dis

        for dr, dc in direction:
            nr, nc = r + dr, c + dc
            if 0 <= nr < row and 0 <= nc < col and (nr, nc) not in seen:
                safe = max(dis, -safeness[nr][nc])
                heappush(heap, (safe, nr, nc))
                seen.add((nr, nc))

    return -1


# -----------------------------------------------------------------------------------------------

# class Solution:
#     def __init__(self):
#         self.roww = [0, 0, -1, 1]
#         self.coll = [-1, 1, 0, 0]

#     def bfs(self, grid, score, n):
#         q = deque()

#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j]:
#                     score[i][j] = 0
#                     q.append((i, j))

#         while q:
#             x, y = q.popleft()
#             s = score[x][y]

#             for i in range(4):
#                 new_x = x + self.roww[i]
#                 new_y = y + self.coll[i]

#                 if 0 <= new_x < n and 0 <= new_y < n and score[new_x][new_y] > s + 1:
#                     score[new_x][new_y] = s + 1
#                     q.append((new_x, new_y))

#     def maximumSafenessFactor(self, grid):
#         n = len(grid)
#         if grid[0][0] or grid[n - 1][n - 1]:
#             return 0

#         score = [[float('inf')] * n for _ in range(n)]
#         self.bfs(grid, score, n)

#         vis = [[False] * n for _ in range(n)]
#         pq = [(-score[0][0], 0, 0)]
#         heapq.heapify(pq)

#         while pq:
#             safe, x, y = heapq.heappop(pq)
#             safe = -safe

#             if x == n - 1 and y == n - 1:
#                 return safe

#             vis[x][y] = True

#             for i in range(4):
#                 new_x = x + self.roww[i]
#                 new_y = y + self.coll[i]

#                 if 0 <= new_x < n and 0 <= new_y < n and not vis[new_x][new_y]:
#                     s = min(safe, score[new_x][new_y])
#                     heapq.heappush(pq, (-s, new_x, new_y))
#                     vis[new_x][new_y] = True

#         return -1
