"""
    2326. Spiral Matrix IV
    https://leetcode.com/problems/spiral-matrix-iv/

    You are given two integers m and n, which represent the dimensions of a matrix.

    You are also given the head of a linked list of integers.

    Generate an m x n matrix that contains the integers in the linked list presented in
    spiral order (clockwise), starting from the top-left of the matrix. If there are
    remaining empty spaces, fill them with -1.

    Return the generated matrix.

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        pass
