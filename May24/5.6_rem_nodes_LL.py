"""
    2487. Remove Nodes From Linked List
    https://leetcode.com/problems/remove-nodes-from-linked-list/

    You are given the head of a linked list.

    Remove every node which has a node with a greater value anywhere to the right side of it.

    Return the head of the modified linked list.

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # optimal
        # O(N)

        head_rev = self.reverseList(head)

        temp = head_rev
        max_val = -1
        prev = None
        while temp:
            if temp.val >= max_val:
                max_val = temp.val
                prev = temp
            else:
                prev.next = temp.next
            temp = temp.next
        return self.reverseList(head_rev)

    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            curr_next = curr.next
            curr.next = prev
            prev = curr
            curr = curr_next
        return prev

        # ------------------------------------------------------------------

        # dummy = head
        # rev = None

        # # reverse the list and store in temp rev
        # while dummy:
        #     next_node = dummy.next
        #     dummy.next = rev
        #     rev = dummy
        #     dummy = next_node

        # # iterate over reversed list
        # dummy = rev
        # head = None
        # max_value = float("-inf")

        # # Create new list
        # while dummy:
        #     if dummy.val >= max_value:
        #         max_value = dummy.val

        #         # same logic as for reversing
        #         new_node = dummy.next
        #         dummy.next = head
        #         head = dummy
        #         dummy = new_node
        #     else:
        #         dummy = dummy.next

        # return head

        # ------------------------------------------------------------------

        # cur = head
        # stack = []
        # while cur:
        #     while stack and stack[-1].val < cur.val:
        #         stack.pop()
        #     stack.append(cur)
        #     cur = cur.next

        # nxt = None
        # while stack:
        #     cur = stack.pop()
        #     cur.next = nxt
        #     nxt = cur

        # return cur
