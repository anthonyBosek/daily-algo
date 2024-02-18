"""
    2402. Meeting Rooms III
    https://www.lintcode.com/problem/meeting-rooms-iii/

    You are given an integer n. There are n rooms numbered from 0 to n - 1.

    You are given a 2D integer array meetings where meetings[i] = [starti, endi] means that a meeting will be held
        during the half-closed time interval [starti, endi). All the values of starti are unique.

    Meetings are allocated to rooms in the following manner:

        1. Each meeting will take place in the unused room with the lowest number.
        2. If there are no available rooms, the meeting will be delayed until a room becomes free.
            The delayed meeting should have the same duration as the original meeting.
        3. When a room becomes unused, meetings that have an earlier original start time should be given the room.

    Return the number of the room that held the most meetings. If there are multiple rooms, return the room with the lowest number.

    A half-closed interval [a, b) is the interval between a and b including a and not including b.

"""

from heapq import heappop, heappush
from operator import itemgetter


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available_rooms = list(range(n))
        used_rooms = []
        meetings_per_room = [0] * n

        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(available_rooms, room)

            if available_rooms:
                room = heappop(available_rooms)
                heappush(used_rooms, (end, room))
            else:
                room_end, room = heappop(used_rooms)
                room_end += end - start
                heappush(used_rooms, (room_end, room))
            meetings_per_room[room] += 1

        max_index, max_value = max(
            enumerate(meetings_per_room), key=operator.itemgetter(1)
        )
        return max_index

    # -----------------------------------------------------------------------

    # ans = [0] * n
    # times = [0] * n
    # meetings.sort()

    # for start, end in meetings:
    #     flag = False
    #     minind = -1
    #     val = float('inf')
    #     for j in range(n):
    #         if times[j] < val:
    #             val = times[j]
    #             minind = j
    #         if times[j] <= start:
    #             flag = True
    #             ans[j] += 1
    #             times[j] = end
    #             break
    #     if not flag:
    #         ans[minind] += 1
    #         times[minind] += (end - start)

    # maxi = -1
    # id = -1
    # for i in range(n):
    #     if ans[i] > maxi:
    #         maxi = ans[i]
    #         id = i
    # return id
