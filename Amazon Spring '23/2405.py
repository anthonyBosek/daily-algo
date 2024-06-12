"""
    2405. Optimal Partition of String
    https://leetcode.com/problems/optimal-partition-of-string/

    Given a string s, partition the string into one or more substrings such that the characters in
    each substring are unique. That is, no letter appears in a single substring more than once.

    Return the minimum number of substrings in such a partition.

    Note that each character should belong to exactly one substring in a partition.

"""


class Solution:
    def partitionString(self, s: str) -> int:
        # ? Initialize variables
        count_map = {}
        result = 0
        # ? Iterate over the string
        for char in s:
            # ? If character is already present in the map
            if char in count_map:
                # ? Increment the result
                result += 1
                # ? Clear the map
                count_map.clear()
            # ? Add the character to the map
            count_map[char] = 1
        # ? Increment the result
        result += 1
        return result

        #! -----------------------------------------

        # cur = ""
        # c = 1
        # for i in s:
        #     if i not in cur:
        #         cur += i
        #     else:
        #         cur = i
        #         c += 1
        # return c

        #! -----------------------------------------

        # chars = set()
        # cnt = 1
        # for c in s:
        #     if c in chars:
        #         cnt += 1
        #         chars = {c}
        #     else:
        #         chars.add(c)
        # return cnt
