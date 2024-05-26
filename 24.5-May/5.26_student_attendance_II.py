"""
    552. Student Attendance Record II
    https://leetcode.com/problems/student-attendance-record-ii/

    An attendance record for a student can be represented as a string where each
    character signifies whether the student was absent, late, or present on that day.
    The record only contains the following three characters:

        • 'A': Absent.
        • 'L': Late.
        • 'P': Present.

    Any student is eligible for an attendance award if they meet both of the following criteria:

        • The student was absent ('A') for strictly fewer than 2 days total.
        • The student was never late ('L') for 3 or more consecutive days.

    Given an integer n, return the number of possible attendance records of length n that
    make a student eligible for an attendance award. The answer may be very large,
    so return it modulo 109 + 7.

"""

# from functools import lru_cache
# from functools import cache
from typing import List


# @lru_cache(maxsize=None)
# def f(n, a, l):
#     if n == 0:
#         return 1
#     ans = 0
#     # try P
#     ans = (ans + f(n - 1, a, 0)) % 1000000007
#     # try A if a < 2
#     if a + 1 < 2:
#         ans = (ans + f(n - 1, a + 1, 0)) % 1000000007
#     # try L if current l < 3
#     if l + 1 < 3:
#         ans = (ans + f(n - 1, a, l + 1)) % 1000000007
#     return ans


# class Solution:
#     def checkRecord(self, n: int) -> int:
#         return f(n, 0, 0)

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


# @cache
# def countRecords(n, conseqLates, absences):
#     if n == 0:
#         return 1
#     count = 0
#     # P
#     count += countRecords(n - 1, 0, absences)
#     # A
#     if absences < 1:
#         count += countRecords(n - 1, 0, absences + 1)
#     # L
#     if conseqLates < 2:
#         count += countRecords(n - 1, conseqLates + 1, absences)

#     return count % (pow(10, 9) + 7)


# class Solution:
#     def checkRecord(self, n: int) -> int:
#         return countRecords(n, 0, 0)


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------


class Solution:
    def checkRecord(self, n: int) -> int:
        temp: List[List[List[int]]] = [
            [[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)
        ]  # temp[cur_ind][count_a][count_l]
        MOD: int = 10**9 + 7

        def check_all_records(cur_ind, count_a, count_l) -> int:
            if cur_ind == n:
                return 1
            if temp[cur_ind][count_a][count_l] != -1:
                return temp[cur_ind][count_a][count_l]
            with_a_next: int = (
                check_all_records(cur_ind + 1, count_a + 1, 0) if count_a == 0 else 0
            )
            with_l_next: int = (
                0
                if count_l == 2
                else check_all_records(cur_ind + 1, count_a, count_l + 1)
            )
            with_p_next: int = check_all_records(cur_ind + 1, count_a, 0)
            total: int = (with_a_next + with_l_next + with_p_next) % MOD

            temp[cur_ind][count_a][count_l] = total
            return total

        return check_all_records(0, 0, 0)
