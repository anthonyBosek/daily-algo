"""
    2181. Merge Nodes in Between Zeros
    https://leetcode.com/problems/merge-nodes-in-between-zeros/
    You are given the head of a linked list, which contains a series of integers separated by 0's.
    The beginning and end of the linked list will have Node.val == 0.

    For every two consecutive 0's, merge all the nodes lying in between them into a single node whose
    value is the sum of all the merged nodes. The modified list should not contain any 0's.

    Return the head of the modified linked list.

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
