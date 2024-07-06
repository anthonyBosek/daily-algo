"""
    2582. Pass the Pillow
    https://leetcode.com/problems/pass-the-pillow/

    There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially.
    Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches
    the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

        - For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.

    Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

"""


def passThePillow(n, time):
    """
    :type n: int
    :type time: int
    :rtype: int
    """
    left_to_right = True
    pos = 1
    for i in range(1, time + 1):
        if left_to_right:
            pos += 1
        else:
            pos -= 1
        if i % (n - 1) == 0:
            left_to_right = not left_to_right
    return pos


# ---------------------------------------------------------------------
#! Approach 1: Simulation
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current_pillow_position = 1
        current_time = 0
        direction = 1
        while current_time < time:
            if 0 < current_pillow_position + direction <= n:
                current_pillow_position += direction
                current_time += 1
            else:
                # Reverse the direction if the next position is out of bounds
                direction *= -1
        return current_pillow_position


# ---------------------------------------------------------------------
#! Approach 2: Math
class Solution:
    def passThePillow(self, n, time):
        # Calculate the number of complete rounds of pillow passing
        full_rounds = time // (n - 1)

        # Calculate the remaining time after complete rounds
        extra_time = time % (n - 1)

        # Determine the position of the person holding the pillow
        # If full_rounds is even, the pillow is moving forward.
        # If full_rounds is odd, the pillow is moving backward.
        if full_rounds % 2 == 0:
            return extra_time + 1  # Position when moving forward
        else:
            return n - extra_time  # Position when moving backward
