"""
    664. Strange Printer
    https://leetcode.com/problems/strange-printer/

    There is a strange printer with the following two special requirements:

        - The printer can only print a sequence of the same character each time.
        - At each turn, the printer can print new characters starting from and ending
            at any place and will cover the original existing characters.

    Given a string s, return the minimum number of turns the printer needed to print it.

"""


def strangePrinter(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = min([dp[i][k] + dp[k + 1][j] for k in range(i, j)])
    return dp[0][n - 1]


#! Approach 1: Top Down Dynamic Programming (Memoization)

import itertools


class Solution:
    def strangePrinter(self, s: str) -> int:
        # Preprocess the string to remove consecutive duplicate characters
        s = "".join(char for char, _ in itertools.groupby(s))

        memo = {}

        def _minimum_turns(start, end) -> int:
            # Base case: empty string requires 0 turns
            if start > end:
                return 0

            # If result is memoized, return it
            if (start, end) in memo:
                return memo[(start, end)]

            # Initialize with worst case: print each character separately
            min_turns = 1 + _minimum_turns(start + 1, end)

            # Try to optimize by finding matching characters
            for k in range(start + 1, end + 1):
                if s[k] == s[start]:
                    # If match found, try splitting the problem
                    turns_with_match = _minimum_turns(start, k - 1) + _minimum_turns(
                        k + 1, end
                    )
                    min_turns = min(min_turns, turns_with_match)

            # Memoize and return the result
            memo[(start, end)] = min_turns
            return min_turns

        # Start the recursive process
        return _minimum_turns(0, len(s) - 1)


#! Approach 2: Bottom Up Dynamic Programming (Tabulation)
class Solution:
    def strangePrinter(self, s: str) -> int:
        # Preprocess the string to remove consecutive duplicate characters
        s = "".join(char for char, _ in itertools.groupby(s))
        n = len(s)

        # min_turns[i][j] represents the minimum number of turns to print s[i] to s[j]
        min_turns = [[0] * n for _ in range(n)]

        # Initialize base case
        for i in range(n):
            # It takes 1 turn to print a single character
            min_turns[i][i] = 1

        # Fill the dp table
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1

                # Initialize with worst case: print each character separately
                min_turns[start][end] = length

                # Try all possible splits and find the minimum
                for split in range(length - 1):
                    total_turns = (
                        min_turns[start][start + split]
                        + min_turns[start + split + 1][end]
                    )

                    # If the characters at the split and end match, we can save one turn
                    if s[start + split] == s[end]:
                        total_turns -= 1

                    min_turns[start][end] = min(min_turns[start][end], total_turns)

        # Return the minimum turns needed to print the entire string
        return min_turns[0][n - 1] if n > 0 else 0


#! BEST
class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        a = [s[0]]
        for i in range(1, n):
            if s[i] != s[i - 1]:
                a.append(s[i])
        n = len(a)
        h = {}
        t = [n] * n
        for i in reversed(range(n)):
            if a[i] in h:
                t[i] = h[a[i]]
            h[a[i]] = i
        d = [[0] * n for _ in range(n + 1)]
        for i in range(n):
            d[i][i] = 1
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                d[i][j] = 1 + d[i + 1][j]
                k = t[i]
                while k <= j:
                    d[i][j] = min(d[i][j], d[i][k - 1] + d[k + 1][j])
                    k = t[k]
        return d[0][n - 1]
