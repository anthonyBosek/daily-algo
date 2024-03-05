"""
    1750. Minimum Length of String After Deleting Similar Ends
    https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

    Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm
        on the string any number of times:

        1. Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
        2. Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
        3. The prefix and the suffix should not intersect at any index.
        4. The characters from the prefix and suffix must be the same.
        5. Delete both the prefix and the suffix.

    Return the minimum length of s after performing the above operation any number of times (possibly zero times).

"""


class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            char = s[l]
            l += 1
            r -= 1
            while l <= r and s[l] == char:
                l += 1
            while l <= r and s[r] == char:
                r -= 1

        return r - l + 1

        # ------------------------------------------------

        # start = 0
        # end = len(s)-1

        # while start < end and s[start] == s[end]:
        #     curr = s[start]
        #     start += 1
        #     end -= 1
        #     while start <= end and s[start] == curr:
        #         start += 1
        #     while end >= start and s[end] == curr:
        #         end -= 1

        # return end-start+1

        # ------------------------------------------------

        # i, j = 0, len(s) - 1
        # while i < j and s[i] == s[j]:
        #     c = s[i]
        #     while i <= j and s[i] == c:
        #         i += 1
        #     while i <= j and s[j] == c:
        #         j -= 1
        # return j - i + 1
