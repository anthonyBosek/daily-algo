"""
    3016. Minimum Number of Pushes to Type Word II
    https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

    You are given a string word containing lowercase English letters.

    Telephone keypads have keys mapped with distinct collections of lowercase English letters,
    which can be used to form words by pushing them. For example, the key 2 is mapped with ["a","b","c"],
    we need to push the key one time to type "a", two times to type "b", and three times to type "c" .

    It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys can be
    remapped to any amount of letters, but each letter must be mapped to exactly one key. You need to
    find the minimum number of times the keys will be pushed to type the string word.

    Return the minimum number of pushes needed to type word after remapping the keys.

    An example mapping of letters to keys on a telephone keypad is given below. Note that 1, *, #, and 0 do not map to any letters.

"""

from collections import Counter


def minimumPushes(word):
    """
    :type word: str
    :rtype: int
    """
    return sum(
        f * (i // 8 + 1)
        for i, f in enumerate(sorted(Counter(word).values(), reverse=True))
    )


#! --- Best ---
class Solution:
    def minimumPushes(self, word: str) -> int:
        l = [0] * (32)
        for i in range(26):
            l[i] = word.count(chr(97 + i))
        l.sort(reverse=True)
        res = 0
        for i in range(4):
            for j in range(8):
                res += (i + 1) * l[8 * i + j]
        return res


#! Approach 1: Greedy Sorting
class Solution:
    def minimumPushes(self, word: str) -> int:
        # Frequency list to store count of each letter
        frequency = [0] * 26

        # Count occurrences of each letter
        for c in word:
            frequency[ord(c) - ord("a")] += 1
        # Sort frequencies in descending order
        frequency.sort(reverse=True)

        total_pushes = 0

        # Calculate total number of presses
        for i in range(26):
            if frequency[i] == 0:
                break
            total_pushes += (i // 8 + 1) * frequency[i]

        return total_pushes


#! Approach 2: Using Heap
class Solution:
    def minimumPushes(self, word: str) -> int:
        # Frequency map to store count of each letter
        frequency_map = Counter(word)

        # Priority queue to store frequencies in descending order
        frequency_queue = [-freq for freq in frequency_map.values()]
        heapq.heapify(frequency_queue)

        total_pushes = 0
        index = 0

        # Calculate total number of presses
        while frequency_queue:
            total_pushes += (1 + (index // 8)) * (-heapq.heappop(frequency_queue))
            index += 1
        return total_pushes
