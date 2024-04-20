"""
    1992. Find All Groups of Farmland
    https://leetcode.com/problems/find-all-groups-of-farmland/

    You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land
        and a 1 represents a hectare of farmland.

    To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland.
        These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not
        four-directionally adjacent to another farmland in a different group.

    land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right
        corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of
        farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2)
        is represented by the 4-length array [r1, c1, r2, c2].

    Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no
        groups of farmland, return an empty array. You may return the answer in any order.

"""


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n, res = len(land), len(land[0]), []
        for i in range(m):
            j = 0
            while j < n:
                if land[i][j]:
                    if land[i][j] == 1:
                        k, l = j + 1, i + 1
                        while k < n and land[i][k] == 1:
                            k += 1
                        k += 1
                        while l < m and land[l][j] == 1:
                            land[l][j] = -k
                            l += 1
                        if l < m:
                            land[l][j] = 1 - k
                        res.append([i, j, l - 1, k - 2])
                        j = k
                    else:
                        j = -land[i][j]
                else:
                    j += 1
        return res

        # ---------------------------------------------------------------------

        # m, n = len(land), len(land[0])
        # res = []

        # def dfs(r, c):
        #     if r < 0 or r >= m or c < 0 or c >= n or land[r][c] == 0:
        #         return
        #     land[r][c] = 0
        #     return [r, c]

        # for i in range(m):
        #     for j in range(n):
        #         if land[i][j] == 1:
        #             r1, c1 = i, j
        #             r2, c2 = i, j
        #             stack = [(i, j)]
        #             while stack:
        #                 r, c = stack.pop()
        #                 land[r][c] = 0
        #                 if r > r2:
        #                     r2 = r
        #                 if c > c2:
        #                     c2 = c
        #                 if r < r1:
        #                     r1 = r
        #                 if c < c1:
        #                     c1 = c
        #                 if r + 1 < m and land[r + 1][c] == 1:
        #                     stack.append((r + 1, c))
        #                 if c + 1 < n and land[r][c + 1] == 1:
        #                     stack.append((r, c + 1))
        #                 if r - 1 >= 0 and land[r - 1][c] == 1:
        #                     stack.append((r - 1, c))
        #                 if c - 1 >= 0 and land[r][c - 1] == 1:
        #                     stack.append((r, c - 1))
        #             res.append([r1, c1, r2, c2])

        # return res
