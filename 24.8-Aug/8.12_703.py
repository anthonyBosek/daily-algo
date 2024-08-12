"""
    703. Kth Largest Element in a Stream
    https://leetcode.com/problems/kth-largest-element-in-a-stream/

    Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

    Implement KthLargest class:

        • KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
        • int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

"""


class KthLargest:

    def __init__(self, k, nums):
        self._nums = sorted(nums)
        self._k = k - 1

    def add(self, val):
        self._nums.append(val)
        l = sorted(self._nums, reverse=True)
        return l[self._k]


#! Approach 1: Maintain Sorted List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.stream = nums
        self.stream.sort()

    def add(self, val: int) -> int:
        index = self.getIndex(val)
        # Add val to correct position
        self.stream.insert(index, val)
        return self.stream[-self.k]

    def getIndex(self, val: int) -> int:
        left, right = 0, len(self.stream) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_element = self.stream[mid]
            if mid_element == val:
                return mid
            # Go to left half
            elif mid_element > val:
                right = mid - 1
            # Go to right half
            else:
                left = mid + 1
        return left


#! Approach 2: Heap

import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k

        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add to our min_heap if we haven't processed k elements yet
        # or if val is greater than the top element (the k-th largest)
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]


#! Approach 3
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        self.k = k
        heapq.heapify(self.stream)
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)
        return self.stream[0]
