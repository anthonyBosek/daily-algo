"""
    1669. Merge In Between Linked Lists
    https://leetcode.com/problems/merge-in-between-linked-lists/

    You are given two linked lists: list1 and list2 of sizes n and m respectively.

    Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        first = list2
        last = list2
        while last.next:
            last = last.next

        prev = ListNode(-1)
        curr = list1
        cntr = 0
        while curr:
            if cntr == a:
                prev.next = first
            if cntr == b:
                last.next = curr.next
                return list1

            cntr += 1
            prev = curr
            curr = curr.next

        return list1

        # ---------------------------------------------------------------------------------

        # # find the a-1th node
        # prev = list1
        # for _ in range(a - 1):
        #     prev = prev.next
        # # find the bth node
        # curr = prev
        # for _ in range(b - a + 2):
        #     curr = curr.next
        # # find the last node of list2
        # last = list2
        # while last.next:
        #     last = last.next
        # # link the a-1th node to list2
        # prev.next = list2
        # # link the last node of list2 to the bth node
        # last.next = curr
        # return list1
