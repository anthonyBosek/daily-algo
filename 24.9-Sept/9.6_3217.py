"""
    3217. Delete Nodes From Linked List Present in Array
    https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

    You are given an array of integers nums and the head of a linked list. Return the head of the modified
    linked list after removing all nodes from the linked list that have a value that exists in nums.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not nums:
            return head

        # Create a set of nums
        nums_set = set(nums)

        # Create a dummy node
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Traverse the linked list
        while head:
            if head.val in nums_set:
                prev.next = head.next
            else:
                prev = head
            head = head.next

        return dummy.next

    # numSet = set(nums)
    # prev = None
    # node = head
    # while node:
    #     if node.val in numSet:
    #         if node == head:
    #             head = head.next
    #             node = head
    #         else:
    #             node = node.next
    #             prev.next = node
    #     else:
    #         prev = node
    #         node = node.next

    # return head


#! Approach: Hash Set
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Create a set for efficient lookup of values in nums
        values_to_remove = set(nums)

        # Handle the case where the head node needs to be removed
        while head and head.val in values_to_remove:
            head = head.next

        # If the list is empty after removing head nodes, return None
        if not head:
            return None

        # Iterate through the list, removing nodes with values in the set
        current = head
        while current.next:
            if current.next.val in values_to_remove:
                # Skip the next node by updating the pointer
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head
