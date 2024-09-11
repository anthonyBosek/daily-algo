"""
    2807. Insert Greatest Common Divisors in Linked List
    https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

    Given the head of a linked list head, in which each node contains an integer value.

    Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

    Return the linked list after insertion.

    The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            a, b = head.val, head.next.val
            g = gcd(a, b)
            node = ListNode(g)
            node.next = head.next
            head.next = node
            prev = head
            head = node.next
        return dummy.next

        # ? fast solution
        # if not head.next:
        #     return head
        # tmp = head
        # while tmp.next:
        #     new = ListNode(gcd(tmp.val, tmp.next.val))
        #     new.next = tmp.next
        #     tmp.next = new
        #     tmp = new.next
        # return head


"""
Algorithm
Main method insertGreatestCommonDivisors:

If the list contains only one node (head.next is null), return the head as no insertion is needed.
Initialize ListNode variables node1 and node2 to head and head.next respectively, to traverse the linked list.
While node2 is not null:
Calculate the GCD's of the values in node1 and node2.
Create a new ListNode gcdNode with the calculated GCD value.
Update node1.next to gcdNode.
Update gcdNode.next to node2.
Set node1 to node2 and node2 to node2.next, respectively. This essentially moves node1 and node2 to the next pair of nodes in the list.
Return the modified head of the list as our answer.
Helper method calculateGCD(a, b):

While b is greater than 0:
Set a variable temp to b.
Set b to a%b and a to temp, respectively.
Return a.
Note: We have used a custom method to calculate the GCD for completeness. In an interview, clarify with your interviewer if built-in GCD methods are acceptable.
"""


#! Approach: Simulation
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Helper method to calculate the greatest common divisor using the Euclidean algorithm
        def _calculate_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        # If the list contains only one node, return the head as no insertion is needed
        if not head.next:
            return head

        # Initialize pointers to traverse the list
        node1 = head
        node2 = head.next

        # Traverse the linked list
        while node2:
            gcd_value = _calculate_gcd(node1.val, node2.val)
            gcd_node = ListNode(gcd_value)

            # Insert the GCD node between node1 and node2
            node1.next = gcd_node
            gcd_node.next = node2

            # Move to the next pair of nodes
            node1 = node2
            node2 = node2.next

        return head
