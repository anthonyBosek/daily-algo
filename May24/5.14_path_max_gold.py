"""
    1219. Path with Maximum Gold
    https://leetcode.com/problems/path-with-maximum-gold/

    In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

    Return the maximum amount of gold you can collect under the conditions:

        • Every time you are located in a cell you will collect all the gold in that cell.

        • From your position you can walk one step to the left, right, up or down.

        • You can't visit the same cell more than once.

        • Never visit a cell with 0 gold.

        • You can start and stop collecting gold from any position in the grid that has some gold.

"""

from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # def dfs(row, col):
        #     if (
        #         row < 0
        #         or row >= m
        #         or col < 0
        #         or col >= n
        #         or grid[row][col] == 0
        #         or visited[row][col]
        #     ):
        #         return 0
        #     visited[row][col] = True
        #     gold = grid[row][col]
        #     max_gold = 0
        #     for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #         max_gold = max(max_gold, dfs(row + dr, col + dc))
        #     visited[row][col] = False
        #     return gold + max_gold

        # n = len(grid[0])
        # m = len(grid)
        # visited = [[False] * n for _ in range(m)]
        # max_gold = 0
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] != 0:
        #             max_gold = max(max_gold, dfs(i, j))
        # return max_gold

        # -------------------------------------------------------------------------------------------------

        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            gold = grid[i][j]
            grid[i][j] = 0
            max_gold = 0
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                max_gold = max(max_gold, dfs(i + x, j + y))
            grid[i][j] = gold
            return max_gold + gold

        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j))
        return max_gold


# def getMaximumGold(grid):
#     """
#     :type grid: List[List[int]]
#     :rtype: int
#     """
#     def dfs(i, j):
#         if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
#             return 0
#         gold = grid[i][j]
#         grid[i][j] = 0
#         max_gold = 0
#         for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#             max_gold = max(max_gold, dfs(i + x, j + y))
#         grid[i][j] = gold
#         return max_gold + gold

#     max_gold = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] != 0:
#                 max_gold = max(max_gold, dfs(i, j))
#     return max_gold


# -------------------------------------------------------------------------------------------------
# ----- proper solution -----
# class Cell:
#     def __init__(self, id: int, row: int, col: int, gold: int):
#         self.id = id
#         self.row = row
#         self.col = col
#         self.gold = gold
#         self.neighbors = set()

#     def __str__(self):
#         return "{} - {}".format(self.id, self.gold)

#     def __repr__(self):
#         return "[{},{}] - {}".format(self.row, self.col, self.gold)


# class Cluster:
#     def __init__(self, id):
#         self.id = id
#         self.cells = set()
#         self.total = 0

#     def __repr__(self):
#         return "id={}, gold={}, {}".format(self.id, self.total, self.cells)


# class Solution:
#     def getMaximumGold(self, grid: List[List[int]]) -> int:
#         index = 0
#         cells = dict()

#         m = len(grid)
#         n = len(grid[0])
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] > 0:
#                     index += 1
#                     newCell = Cell(index, i, j, grid[i][j])
#                     for c in cells.values():
#                         if (
#                             c.row == i
#                             and (c.col == j + 1 or c.col == j - 1)
#                             or c.col == j
#                             and (c.row == i + 1 or c.row == i - 1)
#                         ):
#                             newCell.neighbors.add(c)
#                             c.neighbors.add(newCell)
#                     cells[index] = newCell

#         # print(cells)
#         self.clusters = dict()
#         self.buildClusters(cells, index + 1)
#         # print(self.clusters)
#         self.result = 0
#         self.path = deque()
#         # for cell in cells.values():
#         #     self.visit(cell, 0)

#         sortedClusters = [c for c in self.clusters.values()]
#         sortedClusters.sort(key=lambda cl: cl.total, reverse=True)
#         # print("Sorted", sortedClusters)
#         for cluster in self.clusters.values():
#             self.visitCluster(cluster)

#         return self.result

#     def buildClusters(self, cells: dict, n: int):
#         assigned = [0] * n
#         for k in cells:
#             cell = cells[k]
#             self.tryToAddCellToCluster(cell, assigned)

#     def tryToAddCellToCluster(self, cell, assigned):
#         if assigned[cell.id] == 0:
#             for neighbor in cell.neighbors:
#                 if assigned[neighbor.id] > 0:
#                     cluster = self.clusters[assigned[neighbor.id]]
#                     self.addCellToCluster(cluster, cell, assigned)
#                     break
#         if assigned[cell.id] == 0:
#             index = len(self.clusters) + 1
#             cluster = Cluster(index)
#             self.clusters[index] = cluster
#             self.addCellToCluster(cluster, cell, assigned)
#         for neighbor in cell.neighbors:
#             if assigned[neighbor.id] == 0:
#                 self.tryToAddCellToCluster(neighbor, assigned)

#     def addCellToCluster(self, cluster, cell, assigned):
#         cluster.cells.add(cell)
#         cluster.total += cell.gold
#         assigned[cell.id] = cluster.id

#     def visitCluster(self, cluster: Cluster):
#         if self.result >= cluster.total:
#             return

#         if len(cluster.cells) <= 3:
#             self.result = cluster.total
#             return

#         self.path.clear()
#         for cell in cluster.cells:
#             self.visitCell(cell, 0, cluster.total)

#     def visitCell(self, cell: Cell, current: int, ceiling: int):
#         # print(cellId, self.path)
#         self.path.append(cell.id)
#         current += cell.gold
#         if current > self.result:
#             self.result = current
#         if self.result < ceiling:
#             toVisit = [c for c in cell.neighbors if c.id not in self.path]
#             for neighbor in toVisit:
#                 self.visitCell(neighbor, current, ceiling)

#         self.path.pop()
