"""
    1653. Minimum Deletions to Make String Balanced
    https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

    You are given a string s consisting only of characters 'a' and 'b'​​​​.

    You can delete any number of characters in s to make s balanced. s is balanced if there
    is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

    Return the minimum number of deletions needed to make s balanced.

"""


def minimumDeletions(s):
    """
    :type s: str
    :rtype: int
    """
    #! did not pass all test cases
    # n = len(s)
    # a = [0] * n
    # b = [0] * n
    # b[0] = 1 if s[0] == "b" else 0
    # for i in range(1, n):
    #     b[i] = b[i - 1] + (1 if s[i] == "b" else 0)
    # a[n - 1] = 1 if s[n - 1] == "a" else 0
    # for i in range(n - 2, -1, -1):
    #     a[i] = a[i + 1] + (1 if s[i] == "a" else 0)
    # res = a[0]
    # for i in range(1, n):
    #     res = min(res, a[i] + b[i - 1])
    # return res

    # --------------------------------------------------
    #! Fastest
    ans, count = 0, 0
    for i in s:
        if i == "b":
            count += 1
        elif count:
            ans += 1
            count -= 1
    return ans


#! Approach 1: Three-Pass Count Method
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count_a = [0] * n
        count_b = [0] * n
        b_count = 0

        # First pass: compute count_b which stores the number of
        # 'b' characters to the left of the current position.
        for i in range(n):
            count_b[i] = b_count
            if s[i] == "b":
                b_count += 1

        a_count = 0
        # Second pass: compute count_a which stores the number of
        # 'a' characters to the right of the current position
        for i in range(n - 1, -1, -1):
            count_a[i] = a_count
            if s[i] == "a":
                a_count += 1

        min_deletions = n
        # Third pass: iterate through the string to find the minimum deletions
        for i in range(n):
            min_deletions = min(min_deletions, count_a[i] + count_b[i])
        return min_deletions


#! Approach 2: Combined Pass Method
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count_a = [0] * n
        a_count = 0

        # First pass: compute count_a which stores the number of
        # 'a' characters to the right of the current position
        for i in range(n - 1, -1, -1):
            count_a[i] = a_count
            if s[i] == "a":
                a_count += 1

        min_deletions = n
        b_count = 0
        # Second pass: compute minimum deletions on the fly
        for i in range(n):
            min_deletions = min(count_a[i] + b_count, min_deletions)
            if s[i] == "b":
                b_count += 1

        return min_deletions


#! Approach 3: Two-Variable Method
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_count = sum(1 for ch in s if ch == "a")

        b_count = 0
        min_deletions = n

        # Second pass: iterate through the string to compute minimum deletions
        for ch in s:
            if ch == "a":
                a_count -= 1
            min_deletions = min(min_deletions, a_count + b_count)
            if ch == "b":
                b_count += 1

        return min_deletions


#! Approach 4: Using stack (one pass)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        char_stack = []
        delete_count = 0

        # Iterate through each character in the string
        for char in s:
            # If stack is not empty, top of stack is 'b',
            # and current char is 'a'
            if char_stack and char_stack[-1] == "b" and char == "a":
                char_stack.pop()  # Remove 'b' from stack
                delete_count += 1  # Increment deletion count
            else:
                char_stack.append(char)  # Append current character to stack

        return delete_count


#! Approach 5: Using DP (One Pass)
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        b_count = 0

        # dp[i]: The number of deletions required to
        # balance the substring s[0, i)
        for i in range(n):
            if s[i] == "b":
                dp[i + 1] = dp[i]
                b_count += 1
            else:
                # Two cases: remove 'a' or keep 'a'
                dp[i + 1] = min(dp[i] + 1, b_count)

        return dp[n]


#! Approach 6: Optimized DP
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        min_deletions = 0
        b_count = 0

        # min_deletions variable represents dp[i]
        for ch in s:
            if ch == "b":
                b_count += 1
            else:
                # Two cases: remove 'a' or keep 'a'
                min_deletions = min(min_deletions + 1, b_count)

        return min_deletions
