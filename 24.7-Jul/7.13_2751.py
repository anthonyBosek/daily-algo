"""
    2751. Robot Collisions
    https://www.lintcode.com/problem/robot-collisions/description

    There are n 1-indexed robots, each having a position on a line, health, and movement direction.

    You are given 0-indexed integer arrays positions, healths, and a string directions (directions[i]
    is either 'L' for left or 'R' for right). All integers in positions are unique.

    All robots start moving on the line simultaneously at the same speed in their given directions.
    If two robots ever share the same position while moving, they will collide.

    If two robots collide, the robot with lower health is removed from the line, and the health of the
    other robot decreases by one. The surviving robot continues in the same direction it was going.
    If both robots have the same health, they are both removed from the line.

    Your task is to determine the health of the robots that survive the collisions, in the same order
    that the robots were given, i.e. final heath of robot 1 (if survived), final health of robot 2
    (if survived), and so on. If there are no survivors, return an empty array.

    Return an array containing the health of the remaining robots (in the order they were given in the input),
    after no further collisions can occur.

    Note: The positions may be unsorted.

"""

from typing import List
from collections import deque


#! Approach: Sorting & Stack
class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        indices = list(range(n))
        result = []
        stack = deque()

        # Sort indices based on their positions
        indices.sort(key=lambda x: positions[x])

        for current_index in indices:
            # Add right-moving robots to the stack
            if directions[current_index] == "R":
                stack.append(current_index)
            else:
                while stack and healths[current_index] > 0:
                    # Pop the top robot from the stack for collision check
                    top_index = stack.pop()

                    if healths[top_index] > healths[current_index]:
                        # Top robot survives, current robot is destroyed
                        healths[top_index] -= 1
                        healths[current_index] = 0
                        stack.append(top_index)
                    elif healths[top_index] < healths[current_index]:
                        # Current robot survives, top robot is destroyed
                        healths[current_index] -= 1
                        healths[top_index] = 0
                    else:
                        # Both robots are destroyed
                        healths[current_index] = 0
                        healths[top_index] = 0

        # Collect surviving robots
        for index in range(n):
            if healths[index] > 0:
                result.append(healths[index])

        return result


#! Another Approach
class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        ind = [i for i in range(n)]
        ind.sort(key=lambda x: positions[x])
        s = []
        for x in ind:
            if directions[x] == "L":
                while s:
                    y = s[-1]
                    if healths[x] == healths[y]:
                        healths[x] = healths[y] = 0
                        s.pop()
                        break
                    if healths[x] > healths[y]:
                        healths[x] -= 1
                        healths[y] = 0
                        s.pop()
                    else:
                        healths[x] = 0
                        healths[y] -= 1
                        break
            else:
                s.append(x)
        r = [x for x in healths if x]
        return r
