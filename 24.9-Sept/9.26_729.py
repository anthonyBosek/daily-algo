"""
    729. My Calendar I
    https://leetcode.com/problems/my-calendar-i/

    You are implementing a program to use as your calendar. We can add a new event
    if adding the event will not cause a double booking.

    A double booking happens when two events have some non-empty intersection
    (i.e., some moment is common to both events.).

    The event can be represented as a pair of integers start and end that represents
    a booking on the half-open interval [start, end), the range of real numbers x such
    that start <= x < end.

    Implement the MyCalendar class:

        • MyCalendar() Initializes the calendar object.

        • boolean book(int start, int end) Returns true if the event can be added to
            the calendar successfully without causing a double booking. Otherwise,
            return false and do not add the event to the calendar.

"""


class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

#! Approach: Sorted List + Binary Search
from sortedcontainers import SortedList


class MyCalendar:
    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.calendar.bisect_right((start, end))
        if (idx > 0 and self.calendar[idx - 1][1] > start) or (
            idx < len(self.calendar) and self.calendar[idx][0] < end
        ):
            return False
        self.calendar.add((start, end))
        return True


#!
from bisect import bisect_left


class MyCalendar:

    def __init__(self):
        self.bookings = [(-1, -1), (float("inf"), float("inf"))]

    def book(self, start: int, end: int) -> bool:
        # Use bisect to efficiently find the insertion point for the new booking's end date
        index = bisect_left(self.bookings, (start, end))

        # Check for clash with previous booking (if any)
        if start < self.bookings[index - 1][1]:
            return False

        # Check for clash with next booking (if any)
        if end > self.bookings[index][0]:
            return False

        # No clash found, insert the new booking at the appropriate position
        self.bookings.insert(index, (start, end))
        return True
