"""
    752. Open the Lock
    https://leetcode.com/problems/open-the-lock/

    You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to '0', or '0' to '9'.
    Each move consists of turning one wheel one slot.

    The lock initially starts at '0000', a string representing the state of the 4 wheels.

    You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock
    will stop turning and you will be unable to open it.

    Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of
    turns required to open the lock, or -1 if it is impossible.

"""

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # BFS
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        def get_next(status):
            for i in range(4):
                x = int(status[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield status[:i] + str(y) + status[i + 1 :]

        q = deque([("0000", 0)])
        visited = {"0000"}
        while q:
            status, step = q.popleft()
            for next_status in get_next(status):
                if next_status not in visited and next_status not in deadends:
                    if next_status == target:
                        return step + 1
                    q.append((next_status, step + 1))
                    visited.add(next_status)
        return -1
