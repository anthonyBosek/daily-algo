"""
    2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
    https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

    A critical point in a linked list is defined as either a local maxima or a local minima.

    A node is a local maxima if the current node has a value strictly greater than the previous node and the next node.

    A node is a local minima if the current node has a value strictly smaller than the previous node and the next node.

    Note that a node can only be a local maxima/minima if there exists both a previous node and a next node.

    Given a linked list head, return an array of length 2 containing [minDistance, maxDistance] where minDistance is the minimum
    distance between any two distinct critical points and maxDistance is the maximum distance between any two distinct critical
    points. If there are fewer than two critical points, return [-1, -1].

"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        #! Approach: One Pass
        result = [-1, -1]

        # Initialize minimum distance to the maximum possible value
        min_distance = float("inf")

        # Pointers to track the previous node, current node, and indices
        previous_node = head
        current_node = head.next
        current_index = 1
        previous_critical_index = 0
        first_critical_index = 0

        while current_node.next is not None:
            # Check if the current node is a local maxima or minima
            if (
                current_node.val < previous_node.val
                and current_node.val < current_node.next.val
            ) or (
                current_node.val > previous_node.val
                and current_node.val > current_node.next.val
            ):

                # If this is the first critical point found
                if previous_critical_index == 0:
                    previous_critical_index = current_index
                    first_critical_index = current_index
                else:
                    # Calculate the minimum distance between critical points
                    min_distance = min(
                        min_distance, current_index - previous_critical_index
                    )
                    previous_critical_index = current_index

            # Move to the next node and update indices
            current_index += 1
            previous_node = current_node
            current_node = current_node.next

        # If at least two critical points were found
        if min_distance != float("inf"):
            max_distance = previous_critical_index - first_critical_index
            result = [min_distance, max_distance]

        return result

        #! another approach
        # mind = math.inf
        # prevc = None
        # currc = None
        # prev = head
        # cur = head.next
        # nex = cur.next
        # firstc = None
        # i = 1
        # while nex:
        #     if (nex.val > cur.val and prev.val > cur.val) or (
        #         nex.val < cur.val and prev.val < cur.val
        #     ):
        #         if prevc == None:
        #             firstc = i
        #             prevc = i
        #             currc = i
        #         else:
        #             prevc = currc
        #             currc = i
        #             mind = min(mind, currc - prevc)
        #     i += 1
        #     prev = cur
        #     cur = nex
        #     nex = cur.next

        # if mind == math.inf:
        #     return [-1, -1]
        # return [mind, currc - firstc]
