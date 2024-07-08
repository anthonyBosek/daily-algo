"""
    1823. Find the Winner of the Circular Game
    https://leetcode.com/problems/find-the-winner-of-the-circular-game/

    There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order.
    More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from
    the nth friend brings you to the 1st friend.

    The rules of the game are as follows:

        1. Start at the 1st friend.
        2. Count the next k friends in the clockwise direction including the friend you started at.
            The counting wraps around the circle and may count some friends more than once.
        3. The last friend you counted leaves the circle and loses the game.
        4. If there is still more than one friend in the circle, go back to step 2 starting from the friend
            immediately clockwise of the friend who just lost and repeat.
        5. Else, the last friend in the circle wins the game.

    Given the number of friends, n, and an integer k, return the winner of the game.

    aka: Josephus problem
    https://en.wikipedia.org/wiki/Josephus_problem

"""


def findTheWinner(n, k):
    friends = [i for i in range(1, n + 1)]
    i = 0
    while len(friends) > 1:
        i = (i + k - 1) % len(friends)
        friends.pop(i)
    return friends[0]


#! Approach 1: Simulation with List
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize list of N friends, labeled from 1-N
        circle = list(range(1, n + 1))

        # Maintain the index of the friend to start the count on
        start_index = 0

        # Perform eliminations while there is more than 1 friend left
        while len(circle) > 1:
            # Calculate the index of the friend to be removed
            removal_index = (start_index + k - 1) % len(circle)

            # Remove the friend at removal_index
            circle.pop(removal_index)

            # Update the start_index for the next round
            start_index = removal_index

        return circle[0]


#! Approach 2: Simulation with Queue
from collections import deque


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize deque with n friends
        circle = deque(range(1, n + 1))

        # Perform eliminations while more than 1 player remains
        while len(circle) > 1:
            # Process the first k-1 friends without eliminating them
            for _ in range(k - 1):
                circle.append(circle.popleft())
            # Eliminate the k-th friend
            circle.popleft()

        return circle[0]


#! Approach 3: Recursion
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        return self.winnerHelper(n, k) + 1

    def winnerHelper(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        return (self.winnerHelper(n - 1, k) + k) % n


#! Approach 4: Iterative
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        # add 1 to convert back to 1 indexing
        return ans + 1


#! Approach 5: Fastest
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1
        else:
            return (self.findTheWinner(n - 1, k) + k - 1) % n + 1
