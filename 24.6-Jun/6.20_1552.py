"""
    1552. Magnetic Force Between Two Balls
    https://leetcode.com/problems/magnetic-force-between-two-balls/
    
    In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls
    if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at
    position[i], Morty has m balls and needs to distribute the balls into the baskets such that
    the minimum magnetic force between any two balls is maximum.

    Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

    Given the integer array position and the integer m. Return the required force.

"""

from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # approach 1
        def check(minmax):
            rem = m - 1
            lim = position[0] + minmax
            for p in position[1:]:
                if p >= lim:
                    rem -= 1
                    lim = p + minmax
            return rem <= 0

        position.sort()
        if m == 2:
            return position[-1] - position[0]
        low = 1
        high = (position[-1] - position[0]) // (m - 1)
        while low < high:
            mid = (low + high + 1) // 2
            if check(mid):
                low = mid
            else:
                high = mid - 1
        return low

        #! -------------------------------------------------------------------
        # #? approach 2
        # position.sort()
        # n = len(position)

        # def check(d):
        #     cnt = 1
        #     pre = position[0]
        #     for i in range(1, n):
        #         if position[i] - pre >= d:
        #             cnt += 1
        #             pre = position[i]
        #     return cnt >= m

        # l, r = 0, position[-1] - position[0]
        # while l < r:
        #     mid = (l + r + 1) // 2
        #     if check(mid):
        #         l = mid
        #     else:
        #         r = mid - 1
        # return l


#! ---------------------------------------------------------------------------


# another approach (from leetcode)
class Solution:
    # Check if we can place 'm' balls at 'position'
    # with each ball having at least 'x' gap.
    def can_place_balls(self, x, position, m):
        # Place the first ball at the first position.
        prev_ball_pos = position[0]
        balls_placed = 1

        # Iterate on each 'position' and place a ball there if we can place it.
        for i in range(1, len(position)):
            curr_pos = position[i]
            # Check if we can place the ball at the current position.
            if curr_pos - prev_ball_pos >= x:
                balls_placed += 1
                prev_ball_pos = curr_pos
            # If all 'm' balls are placed, return 'True'.
            if balls_placed == m:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        answer = 0
        n = len(position)
        position.sort()

        # Initial search space.
        low = 1
        high = int(position[-1] / (m - 1.0)) + 1
        while low <= high:
            mid = low + (high - low) // 2
            # If we can place all balls having a gap at least 'mid',
            if self.can_place_balls(mid, position, m):
                # then 'mid' can be our answer,
                answer = mid
                # and discard the left half search space.
                low = mid + 1
            else:
                # Discard the right half search space.
                high = mid - 1
        return answer
