"""
    42. Trapping Rain Water
    https://leetcode.com/problems/trapping-rain-water/

    Given n non-negative integers representing an elevation map where the width of each bar is 1,
        compute how much water it can trap after raining.

"""


class Solution:
    def trap(self, height: List[int]) -> int:
        maxIndex = height.index(max(height))
        surface = height[maxIndex]
        n = len(height)

        maxHeight = 0
        for left in range(maxIndex):
            if height[left] > maxHeight:
                maxHeight = height[left]
            surface += maxHeight

        maxHeight = 0
        curIndex = n - 1
        while curIndex > maxIndex:
            if height[curIndex] > maxHeight:
                maxHeight = height[curIndex]
            surface += maxHeight
            curIndex -= 1

        surface2 = 0

        print(surface2)

        # print(height[maxIndex])
        return surface - sum(height)

        # --------------------------------------------------------------

        # if not height:
        #     return 0

        # n = len(height)
        # left_max = [0] * n
        # right_max = [0] * n

        # left_max[0] = height[0]
        # for i in range(1, n):
        #     left_max[i] = max(left_max[i - 1], height[i])

        # right_max[n - 1] = height[n - 1]
        # for i in range(n - 2, -1, -1):
        #     right_max[i] = max(right_max[i + 1], height[i])

        # water = 0
        # for i in range(n):
        #     water += min(left_max[i], right_max[i]) - height[i]

        # return water
