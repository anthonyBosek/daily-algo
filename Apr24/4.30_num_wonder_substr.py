"""
    1915. Number of Wonderful Substrings
    https://leetcode.com/problems/number-of-wonderful-substrings/

    A wonderful string is a string where at most one letter appears an odd number of times.

        - For example, "ccjjc" and "abab" are wonderful, but "ab" is not.

    Given a string word that consists of the first ten lowercase English letters ('a' through 'j'),
        return the number of wonderful non-empty substrings in word. If the same substring appears
        multiple times in word, then count each occurrence separately.

    A substring is a contiguous sequence of characters in a string.

"""

from collections import defaultdict
from string import ascii_lowercase


def wonderfulSubstrings(word):
    # toBit = {c: 1 << i for i, c in enumerate(ascii_lowercase[:10])}
    # mask = 0

    # count = defaultdict(int)
    # count[0] = 1

    # for c in word:
    #     mask ^= toBit[c]
    #     count[mask] += 1

    # res = 0
    # for mask, cnt in count.items():
    #     res += cnt * (cnt - 1) // 2
    #     for i in range(10):
    #         mask2 = mask ^ (1 << i)
    #         if mask2 < mask:
    #             res += cnt * count.get(mask2, 0)

    # return res

    # -------------------------------------------------------------------

    # toBit = {c: 1 << i for i, c in enumerate(ascii_lowercase[:10])}
    # mask = 0
    # count = defaultdict(int)
    # count[0] = 1
    # res = 0
    # for c in word:
    #     mask ^= toBit[c]
    #     res += count[mask]
    #     res += sum(count.get(mask ^ (1 << i), 0) for i in range(10))
    #     count[mask] += 1
    # return res

    # -------------------------------------------------------------------

    # Initialize the count of wonderful substrings
    count = 0
    # Initialize the prefix sum array
    prefix_sum = [0] * 1024
    # Initialize the prefix sum of 0
    prefix_sum[0] = 1
    # Initialize the mask
    mask = 0
    # Loop through the word
    for char in word:
        # Get the bit of the character
        bit = 1 << (ord(char) - ord("a"))
        # Toggle the bit
        mask ^= bit
        # Update the count
        count += prefix_sum[mask]
        # Loop through the bits
        for i in range(10):
            # Update the count
            count += prefix_sum[mask ^ (1 << i)]
        # Update the prefix sum
        prefix_sum[mask] += 1
    # Return the count
    return count
