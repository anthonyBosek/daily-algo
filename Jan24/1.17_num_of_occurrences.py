"""
    1207. Unique Number of Occurrences
    https://leetcode.com/problems/unique-number-of-occurrences/


    Given an array of integers arr, write a function that returns true if and only if the number
        of occurrences of each value in the array is unique.

"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        return len(freq) == len(set(freq.values()))

        # ------------------------------------------------------------

        # my_set = set()
        # my_dict = {}
        # for num in arr:
        #     if num in my_dict:
        #         my_dict[num] += 1
        #     else:
        #         my_dict[num] = 1

        # for key in my_dict:
        #     if my_dict[key] in my_set:
        #         return False
        #     else:
        #         my_set.add(my_dict[key])

        # return True
