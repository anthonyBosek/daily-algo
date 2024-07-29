"""
    1395. Count Number of Teams
    https://leetcode.com/problems/count-number-of-teams/

    There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

    You have to form a team of 3 soldiers amongst them under the following rules:

        • Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
        • A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).

    Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

"""


def numTeams(rating):
    """
    :type rating: List[int]
    :rtype: int
    """
    n = len(rating)
    count = 0
    for i in range(n):
        left_less = left_more = right_less = right_more = 0
        for j in range(i):
            if rating[j] < rating[i]:
                left_less += 1
            if rating[j] > rating[i]:
                left_more += 1
        for j in range(i + 1, n):
            if rating[j] < rating[i]:
                right_less += 1
            if rating[j] > rating[i]:
                right_more += 1
        count += left_less * right_more + left_more * right_less
    return count


#! ---
from typing import List
from bisect import bisect


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l = []
        sr = sorted(rating)
        low = {}
        for idx, r in enumerate(sr):
            low[r] = idx
        res = 0
        n = len(rating)
        for idx, r in enumerate(rating):
            i = bisect(l, r)
            l.insert(i, r)
            j = low[r] - i
            res += i * (n - 1 - idx - j) + j * (idx - i)
        return res

    def numTeams2(self, rating: List[int]) -> int:
        ans, n = 0, len(rating)
        for j in range(n):
            llt, lgt = 0, 0
            for i in range(j):
                llt += rating[i] < rating[j]
                lgt += rating[i] > rating[j]
            rlt, rgt = 0, 0
            for k in range(j + 1, n):
                rlt += rating[k] < rating[j]
                rgt += rating[k] > rating[j]
            ans += llt * rgt + lgt * rlt
        return ans

    def numTeams1(self, rating: List[int]) -> int:
        ans, n = 0, len(rating)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    ans += (
                        1
                        if rating[i] < rating[j] < rating[k]
                        or rating[i] > rating[j] > rating[k]
                        else 0
                    )
        return ans


#! Approach 1: Dynamic Programming (Memoization)
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        increasing_cache = [[-1] * 4 for _ in range(n)]
        decreasing_cache = [[-1] * 4 for _ in range(n)]

        # Calculate total teams by considering each soldier as a starting point
        for start_index in range(n):
            teams += self._count_increasing_teams(
                rating, start_index, 1, increasing_cache
            ) + self._count_decreasing_teams(rating, start_index, 1, decreasing_cache)

        return teams

    def _count_increasing_teams(
        self,
        rating: List[int],
        current_index: int,
        team_size: int,
        increasing_cache: List[List[int]],
    ) -> int:
        n = len(rating)

        # Base case: reached end of array
        if current_index == n:
            return 0

        # Base case: found a valid team of size 3
        if team_size == 3:
            return 1

        # Return cached result if available
        if increasing_cache[current_index][team_size] != -1:
            return increasing_cache[current_index][team_size]

        valid_teams = 0

        # Recursively count teams with increasing ratings
        for next_index in range(current_index + 1, n):
            if rating[next_index] > rating[current_index]:
                valid_teams += self._count_increasing_teams(
                    rating, next_index, team_size + 1, increasing_cache
                )

        # Cache and return the result
        increasing_cache[current_index][team_size] = valid_teams
        return valid_teams

    def _count_decreasing_teams(
        self,
        rating: List[int],
        current_index: int,
        team_size: int,
        decreasing_cache: List[List[int]],
    ) -> int:
        n = len(rating)

        # Base case: reached end of array
        if current_index == n:
            return 0

        # Base case: found a valid team of size 3
        if team_size == 3:
            return 1

        # Return cached result if available
        if decreasing_cache[current_index][team_size] != -1:
            return decreasing_cache[current_index][team_size]

        valid_teams = 0

        # Recursively count teams with decreasing ratings
        for next_index in range(current_index + 1, n):
            if rating[next_index] < rating[current_index]:
                valid_teams += self._count_decreasing_teams(
                    rating, next_index, team_size + 1, decreasing_cache
                )

        # Cache and return the result
        decreasing_cache[current_index][team_size] = valid_teams
        return valid_teams


#! Approach 2: Dynamic Programming (Tabulation)
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        # Tables for increasing and decreasing sequences
        increasing_teams = [[0] * 4 for _ in range(n)]
        decreasing_teams = [[0] * 4 for _ in range(n)]

        # Fill the base cases. (Each soldier is a sequence of length 1)
        for i in range(n):
            increasing_teams[i][1] = 1
            decreasing_teams[i][1] = 1

        # Fill the tables
        for count in range(2, 4):
            for i in range(n):
                for j in range(i + 1, n):
                    if rating[j] > rating[i]:
                        increasing_teams[j][count] += increasing_teams[i][count - 1]
                    if rating[j] < rating[i]:
                        decreasing_teams[j][count] += decreasing_teams[i][count - 1]

        # Sum up the results (All sequences of length 3)
        for i in range(n):
            teams += increasing_teams[i][3] + decreasing_teams[i][3]

        return teams


#! Approach 3: Dynamic Programming (Optimized)
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0

        # Iterate through each soldier as the middle soldier
        for mid in range(n):
            left_smaller = 0
            right_larger = 0

            # Count soldiers with smaller ratings on the left side of the current soldier
            for left in range(mid - 1, -1, -1):
                if rating[left] < rating[mid]:
                    left_smaller += 1

            # Count soldiers with larger ratings on the right side of the current soldier
            for right in range(mid + 1, n):
                if rating[right] > rating[mid]:
                    right_larger += 1

            # Calculate and add the number of ascending rating teams (small-mid-large)
            teams += left_smaller * right_larger

            # Calculate soldiers with larger ratings on the left and smaller ratings on the right
            left_larger = mid - left_smaller
            right_smaller = n - mid - 1 - right_larger

            # Calculate and add the number of descending rating teams (large-mid-small)
            teams += left_larger * right_smaller

        # Return the total number of valid teams
        return teams


#! Approach 4: Binary Indexed Tree (Fenwick Tree)
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # Find the maximum rating
        max_rating = 0
        for r in rating:
            max_rating = max(max_rating, r)

        # Initialize Binary Indexed Trees for left and right sides
        left_BIT = [0] * (max_rating + 1)
        right_BIT = [0] * (max_rating + 1)

        # Populate the right BIT with all ratings initially
        for r in rating:
            self._update_BIT(right_BIT, r, 1)

        teams = 0
        for current_rating in rating:
            # Remove current rating from right BIT
            self._update_BIT(right_BIT, current_rating, -1)

            # Count soldiers with smaller and larger ratings on both sides
            smaller_ratings_left = self._get_prefix_sum(left_BIT, current_rating - 1)
            smaller_ratings_right = self._get_prefix_sum(right_BIT, current_rating - 1)
            larger_ratings_left = self._get_prefix_sum(
                left_BIT, max_rating
            ) - self._get_prefix_sum(left_BIT, current_rating)
            larger_ratings_right = self._get_prefix_sum(
                right_BIT, max_rating
            ) - self._get_prefix_sum(right_BIT, current_rating)

            # Count increasing and decreasing sequences
            teams += smaller_ratings_left * larger_ratings_right
            teams += larger_ratings_left * smaller_ratings_right

            # Add current rating to left BIT
            self._update_BIT(left_BIT, current_rating, 1)

        return teams

    # Update the Binary Indexed Tree
    def _update_BIT(self, BIT: List[int], index: int, value: int) -> None:
        while index < len(BIT):
            BIT[index] += value
            index += index & (-index)  # Move to the next relevant index in BIT

    # Get the sum of all elements up to the given index in the BIT
    def _get_prefix_sum(self, BIT: List[int], index: int) -> int:
        sum = 0
        while index > 0:
            sum += BIT[index]
            index -= index & (-index)  # Move to the parent node in BIT
        return sum
