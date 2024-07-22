"""
    2418. Sort the People
    https://leetcode.com/problems/sort-the-people/

    You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

    For each index i, names[i] and heights[i] denote the name and height of the ith person.

    Return names sorted in descending order by the people's heights.

"""


def sortPeople(names, heights):
    """
    type names: List[str]
    type heights: List[int]
    rtype: List[str]
    """
    return [name for _, name in sorted(zip(heights, names), reverse=True)]
    # ---
    # return [name for _, name in sorted(zip(heights, names), key=lambda x: x[0], reverse=True)]
    # ---
    # d = {}
    # descend = [""] * len(names)
    # for i in range(len(names)):
    #     d[heights[i]] = names[i]
    # h = sorted(heights)
    # return [d[height] for height in h[::-1]]
    # ---
    # pass


#! Approach 1: Map
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        number_of_people = len(names)

        # Create a dictionary to store height-name pairs
        height_to_name_map = dict(zip(heights, names))

        sorted_heights = sorted(heights, reverse=True)

        # Create a list of sorted names based on descending heights
        sorted_names = [height_to_name_map[height] for height in sorted_heights]

        return sorted_names


#! Approach 2: Sorted Map
from collections import OrderedDict


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        number_of_people = len(names)

        height_to_name_map = OrderedDict()

        # Populate the OrderedDict with height as key and name as value
        for height, name in zip(heights, names):
            height_to_name_map[height] = name

        # Sort the OrderedDict by height in descending order
        height_to_name_map = OrderedDict(
            sorted(height_to_name_map.items(), reverse=True)
        )

        # Create a list of sorted names based on descending heights
        sorted_names = list(height_to_name_map.values())

        return sorted_names


#! Approach 3: Sort Permutation
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        number_of_people = len(names)

        # Create a list of indices and sort them based on heights in descending order
        sorted_indices = sorted(
            range(number_of_people), key=lambda i: heights[i], reverse=True
        )

        # Apply the sorted indices to rearrange names
        sorted_names = [names[i] for i in sorted_indices]

        return sorted_names


#! Approach 4: Quick Sort
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        self._quick_sort(heights, names, 0, len(heights) - 1)
        return names

    def _swap(self, heights: List[int], names: List[str], index1: int, index2: int):
        # Swap heights
        heights[index1], heights[index2] = heights[index2], heights[index1]

        # Swap corresponding names
        names[index1], names[index2] = names[index2], names[index1]

    def _partition(
        self, heights: List[int], names: List[str], start: int, end: int
    ) -> int:
        pivot = heights[end]
        i = start - 1

        for j in range(start, end):
            # If current element is greater than or equal to pivot
            if heights[j] >= pivot:
                i += 1
                self._swap(heights, names, i, j)

        # Place the pivot in its correct position
        self._swap(heights, names, i + 1, end)
        return i + 1

    def _quick_sort(self, heights: List[int], names: List[str], start: int, end: int):
        if start < end:
            # Find the partition index
            partition_index = self._partition(heights, names, start, end)

            # Recursively sort the left and right sub-arrays
            self._quick_sort(heights, names, start, partition_index - 1)
            self._quick_sort(heights, names, partition_index + 1, end)


#! Approach 5: Merge Sort
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        self._merge_sort(names, heights, 0, len(heights) - 1)
        return names

    def _merge_sort(self, names: List[str], heights: List[int], start: int, end: int):
        if start < end:
            mid = start + (end - start) // 2
            self._merge_sort(names, heights, start, mid)
            self._merge_sort(names, heights, mid + 1, end)
            self._merge(names, heights, start, mid, end)

    def _merge(
        self,
        names: List[str],
        heights: List[int],
        start: int,
        mid: int,
        end: int,
    ):
        left_size = mid - start + 1
        right_size = end - mid

        # Create temporary lists
        left_heights = heights[start : start + left_size]
        right_heights = heights[mid + 1 : mid + 1 + right_size]
        left_names = names[start : start + left_size]
        right_names = names[mid + 1 : mid + 1 + right_size]

        # Merge the temporary lists
        left_index, right_index = 0, 0
        merge_index = start
        while left_index < left_size and right_index < right_size:
            if (
                left_heights[left_index] >= right_heights[right_index]
            ):  # Descending order
                heights[merge_index] = left_heights[left_index]
                names[merge_index] = left_names[left_index]
                left_index += 1
            else:
                heights[merge_index] = right_heights[right_index]
                names[merge_index] = right_names[right_index]
                right_index += 1
            merge_index += 1

        # Copy remaining elements of left_heights, if any
        while left_index < left_size:
            heights[merge_index] = left_heights[left_index]
            names[merge_index] = left_names[left_index]
            left_index += 1
            merge_index += 1

        # Copy remaining elements of right_heights, if any
        while right_index < right_size:
            heights[merge_index] = right_heights[right_index]
            names[merge_index] = right_names[right_index]
            right_index += 1
            merge_index += 1
