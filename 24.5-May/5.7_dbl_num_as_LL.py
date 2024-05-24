"""
    2816. Double a Number Represented as a Linked List
    https://leetcode.com/problems/double-a-number-represented-as-linked-list/

    You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

    Return the head of the linked list after doubling it.

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head.val > 4:
        #     head = ListNode(0, head)
        # node = head
        # while node:
        #     node.val = (node.val * 2) % 10
        #     if node.next and node.next.val > 4:
        #         node.val += 1
        #     node = node.next
        # return head

        # ------------------------------------------------------------

        curr = head
        if curr.val > 4:
            head = ListNode(1, head)
            # ans = ListNode(1, head)
        while curr.next:
            curr.val = (curr.val * 2 + (curr.next.val > 4)) % 10
            curr = curr.next
        curr.val = (curr.val * 2) % 10

        return head

        # ------------------------------------------------------------

        # if not head:
        #     return None

        # # reverse the linked list
        # prev = None
        # current = head
        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node

        # head = prev

        # carry = 0
        # current = head
        # while current:
        #     current.val = current.val * 2 + carry
        #     carry = current.val // 10
        #     current.val = current.val % 10
        #     current = current.next

        # if carry:
        #     current = head
        #     while current.next:
        #         current = current.next
        #     current.next = ListNode(carry)

        # # reverse the linked list
        # prev = None
        # current = head
        # while current:
        #     next_node = current.next
        #     current.next = prev
        #     prev = current
        #     current = next_node

        # return prev
