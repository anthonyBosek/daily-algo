"""
    234. Palindrome Linked List
    https://leetcode.com/problems/palindrome-linked-list/

    Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. Find the middle of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half of the linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # 3. Compare the first and second half of the linked list
        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

        # ---------------------------------------------------

        # rev = None
        # slow = fast = head

        # while fast and fast.next:
        #     fast = fast.next.next
        #     tmp = rev
        #     rev = slow
        #     slow = slow.next
        #     rev.next = tmp

        # # if fast is None, odd number of nodes
        # if fast:
        #     slow = slow.next
        # while rev and rev.val == slow.val:
        #     rev = rev.next
        #     slow = slow.next

        # return not rev

        # ---------------------------------------------------

        # slow, fast, prev = head, head, None
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # prev, slow, prev.next = slow, slow.next, None
        # while slow:
        #     slow.next, prev, slow = prev, slow, slow.next
        # slow = prev
        # fast = head
        # while slow:
        #     if fast.val != slow.val:
        #         return False
        #     slow = slow.next
        #     fast = fast.next
        # return True
