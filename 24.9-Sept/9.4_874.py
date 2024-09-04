"""
    874. Walking Robot Simulation
    https://leetcode.com/problems/walking-robot-simulation/

    A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot
    can receive a sequence of these three possible types of commands:

        • -2: Turn left 90 degrees.
        • -1: Turn right 90 degrees.
        • 1 <= k <= 9: Move forward k units, one unit at a time.

    Some of the grid squares are obstacles. The ith obstacle is at grid point
    obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will
    instead stay in its current location and move on to the next command.

    Return the maximum Euclidean distance that the robot ever gets from the
    origin squared (i.e. if the distance is 5, return 25).

    Note:
        • North means +Y direction.
        • East means +X direction.
        • South means -Y direction.
        • West means -X direction.
        • There can be obstacle in [0,0].

"""

from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set(map(tuple, obstacles))
        x, y = 0, 0
        dx, dy = 0, 1
        max_dist = 0
        for command in commands:
            if command == -2:
                dx, dy = -dy, dx
            elif command == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x += dx
                    y += dy
                max_dist = max(max_dist, x * x + y * y)
        return max_dist


#! Editorial
class Solution:
    def __init__(self):
        self.HASH_MULTIPLIER = 60001  # Slightly larger than 2 * max coordinate value

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Store obstacles in an set for efficient lookup
        obstacle_set = {self._hash_coordinates(x, y) for x, y in obstacles}

        # Define direction vectors: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0
        max_distance_squared = 0
        current_direction = 0  # 0: North, 1: East, 2: South, 3: West

        for command in commands:
            if command == -1:  # Turn right
                current_direction = (current_direction + 1) % 4
                continue

            if command == -2:  # Turn left
                current_direction = (current_direction + 3) % 4
                continue

            # Move forward
            dx, dy = directions[current_direction]
            for _ in range(command):
                next_x, next_y = x + dx, y + dy
                if self._hash_coordinates(next_x, next_y) in obstacle_set:
                    break
                x, y = next_x, next_y

            max_distance_squared = max(max_distance_squared, x * x + y * y)

        return max_distance_squared

    # Hash function to convert (x, y) coordinates to a unique integer value
    def _hash_coordinates(self, x: int, y: int) -> int:
        return x + self.HASH_MULTIPLIER * y
