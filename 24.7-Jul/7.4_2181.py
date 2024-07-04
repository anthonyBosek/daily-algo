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
        l = head
        r = head.next

        sum = 0
        while r:
            if r.val == 0:
                l = l.next
                l.val = sum
                sum = 0
            else:
                sum += r.val
            r = r.next

        l.next = None
        return head.next


# Approach 1: Two-Pointer (One-Pass)
class Solution:
    def mergeNodes(self, head):
        # Initialize a sentinel/dummy node with the first non-zero value.
        modify = head.next
        next_sum = modify

        while next_sum:
            sum = 0
            # Find the sum of all nodes until you encounter a 0.
            while next_sum.val != 0:
                sum += next_sum.val
                next_sum = next_sum.next

            # Assign the sum to the current node's value.
            modify.val = sum
            # Move nextSum to the first non-zero value of the next block.
            next_sum = next_sum.next
            # Move modify also to this node.
            modify.next = next_sum
            modify = modify.next
        return head.next


# Approach 2: Recursion
class Solution:
    def mergeNodes(self, head):
        # Start with the first non-zero value.
        head = head.next
        if not head:
            return head

        # Initialize a dummy head node.
        temp = head
        sum = 0
        while temp.val != 0:
            sum += temp.val
            temp = temp.next

        # Store the sum in head's value.
        head.val = sum
        # Store head's next node as the recursive result for temp node.
        head.next = self.mergeNodes(temp)
        return head
