"""
    539. Minimum Time Difference
    https://leetcode.com/problems/minimum-time-difference/

    Given a list of 24-hour clock time points in "HH:MM" format, return the minimum
    time difference (in minutes) between any two time points in the list.

"""


class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        # Convert time points to minutes
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(":"))
            minutes.append(h * 60 + m)

        # Sort the minutes
        minutes.sort()

        # Initialize the minimum difference
        min_diff = float("inf")

        # Calculate the minimum difference
        for i in range(len(minutes)):
            # Calculate the difference between the current and next time point
            diff = (minutes[(i + 1) % len(minutes)] - minutes[i]) % (24 * 60)
            min_diff = min(min_diff, diff)

        return min_diff


#! Approach 1: Sort
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert input to minutes
        minutes = [int(time[:2]) * 60 + int(time[3:]) for time in timePoints]

        # sort times in ascending order
        minutes.sort()

        # find minimum difference across adjacent elements
        ans = min(minutes[i + 1] - minutes[i] for i in range(len(minutes) - 1))

        # consider difference between last and first element
        return min(ans, 24 * 60 - minutes[-1] + minutes[0])


#! Approach 2: Bucket Sort
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # create buckets array for the times converted to minutes
        minutes = [False] * (24 * 60)
        for time in timePoints:
            h, m = map(int, time.split(":"))
            min_time = h * 60 + m
            if minutes[min_time]:
                return 0
            minutes[min_time] = True
        prevIndex = float("inf")
        firstIndex = float("inf")
        lastIndex = float("inf")
        ans = float("inf")

        # find differences between adjacent elements in sorted array
        for i in range(24 * 60):
            if minutes[i]:
                if prevIndex != float("inf"):
                    ans = min(ans, i - prevIndex)
                prevIndex = i
                if firstIndex == float("inf"):
                    firstIndex = i
                lastIndex = i

        return min(ans, 24 * 60 - lastIndex + firstIndex)


#!
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # other way around --> compare last & 24 + first

        # [2, 2*10^4]

        # 1440 minutes / day

        times = set()

        for timePoint in timePoints:
            time_val = 60 * int(timePoint[:2]) + int(timePoint[3:])
            if time_val in times:
                return 0
            times.add(time_val)

        times = list(times)
        times.sort()

        first = times[0]
        last = times[-1]

        min_diff = 1440 + first - last

        for i in range(len(times) - 1):
            curr_diff = times[i + 1] - times[i]
            if min_diff > curr_diff:
                min_diff = curr_diff

        return min_diff
