"""
    237. Delete Node in a Linked List
    https://leetcode.com/problems/delete-node-in-a-linked-list/

    There is a singly-linked list head and we want to delete a node node in it.

    You are given the node to be deleted node. You will not be given access to the first node of head.

    All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

    Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

        • The value of the given node should not exist in the linked list.
        • The number of nodes in the linked list should decrease by one.
        • All the values before node should be in the same order.
        • All the values after node should be in the same order.

    Custom testing:

        • For the input, you should provide the entire linked list head and the node to be given node. node should not be the
            last node of the list and should be an actual node in the list.
        • We will build the linked list and pass the node to your function.
        • The output will be the entire list after calling your function.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        pnode, nnode = node, node.next
        while nnode is not None:
            node.val = nnode.val
            pnode, node = node, nnode
            nnode = nnode.next
        pnode.next = None

        # ---------------------------------------------------------------

        # # locate victim node
        # victim_node = node.next

        # # overwrite node's value by victim node's value
        # node.val = victim_node.val

        # # break the linkage of victim node
        # node.next = victim_node.next

        # # release victim node
        # del victim_node

        # return

        # ---------------------------------------------------------------

        # if not node:
        #     return None
        # first = node
        # second = first.next
        # third = second.next

        # first.val = second.val
        # first.next = third
        # second.next= None

        # ---------------------------------------------------------------

        # # Copy the value of the next node to the current node
        # node.val = node.next.val

        # # Delete the next node
        # node.next = node.next.next

        # if node.next:
        #     node.val  = node.next.val
        #     node.next = node.next.next
        # else:
        #     node.next = None
