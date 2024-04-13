"""
    85. Maximal Rectangle
    https://leetcode.com/problems/maximal-rectangle/

    Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

"""


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def largestRectangleArea(heights):
            n = len(heights)
            stack = []
            maxArea = 0
            for i, h in enumerate(heights):
                start = i
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()
                    maxArea = max(maxArea, height * (i - index))
                    start = index
                stack.append((start, h))

            for i, h in stack:
                maxArea = max(maxArea, h * (len(heights) - i))
            return maxArea

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            res = max(res, largestRectangleArea(heights))

        return res

        # ------------------------------------------------------------------------

        # if not matrix:
        #     return 0

        # n = len(matrix[0])
        # heights = [0] * n
        # max_area = 0

        # for row in matrix:
        #     for i in range(n):
        #         heights[i] = heights[i] + 1 if row[i] == '1' else 0

        #     stack = []
        #     for i, h in enumerate(heights + [0]):
        #         while stack and h < heights[stack[-1]]:
        #             height = heights[stack.pop()]
        #             width = i if not stack else i - stack[-1] - 1
        #             max_area = max(max_area, height * width)
        #         stack.append(i)

        # return max_area
