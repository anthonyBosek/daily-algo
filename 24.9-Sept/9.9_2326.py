"""
    2326. Spiral Matrix IV
    https://leetcode.com/problems/spiral-matrix-iv/

    You are given two integers m and n, which represent the dimensions of a matrix.

    You are also given the head of a linked list of integers.

    Generate an m x n matrix that contains the integers in the linked list presented in
    spiral order (clockwise), starting from the top-left of the matrix. If there are
    remaining empty spaces, fill them with -1.

    Return the generated matrix.

"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        if not head:
            return [[-1] * n for _ in range(m)]
        res = [[-1] * n for _ in range(m)]
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        i, j = 0, 0
        di, dj = 0, 1
        for num in nums:
            res[i][j] = num
            if 0 <= i + di < m and 0 <= j + dj < n and res[i + di][j + dj] == -1:
                i += di
                j += dj
            else:
                di, dj = dj, -di
                i += di
                j += dj
        return res


#! Approach: Simulation
class Solution:
    def spiralMatrix(self, m: int, n: int, head: "ListNode") -> List[List[int]]:
        # Store the east, south, west, north movements in a matrix.
        i = 0
        j = 0
        cur_d = 0
        movement = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = [[-1 for _ in range(n)] for _ in range(m)]

        while head is not None:
            res[i][j] = head.val
            newi = i + movement[cur_d][0]
            newj = j + movement[cur_d][1]

            # If we bump into an edge or an already filled cell, change the
            # direction.
            if min(newi, newj) < 0 or newi >= m or newj >= n or res[newi][newj] != -1:
                cur_d = (cur_d + 1) % 4
            i += movement[cur_d][0]
            j += movement[cur_d][1]

            head = head.next

        return res


#! **
class Solution:
    def spiralMatrix(self, m: int, n: int, head: ListNode) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]

        topRow, bottomRow = 0, m - 1
        leftCol, rightCol = 0, n - 1

        while head:

            for j in range(leftCol, rightCol + 1):
                if head:
                    matrix[topRow][j] = head.val
                    head = head.next
            topRow += 1

            for i in range(topRow, bottomRow + 1):
                if head:
                    matrix[i][rightCol] = head.val
                    head = head.next
            rightCol -= 1

            for j in range(rightCol, leftCol - 1, -1):
                if head:
                    matrix[bottomRow][j] = head.val
                    head = head.next
            bottomRow -= 1

            for i in range(bottomRow, topRow - 1, -1):
                if head:
                    matrix[i][leftCol] = head.val
                    head = head.next
            leftCol += 1

        return matrix


def format_output(result):
    return "[" + ",".join(str(row).replace(" ", "") for row in result) + "]"


def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()

    num_test_cases = len(lines) // 3
    results = []

    for i in range(num_test_cases):
        m = int(lines[i * 3])
        n = int(lines[i * 3 + 1])
        head_values = json.loads(lines[i * 3 + 2])

        if not head_values:
            head = None
        else:
            head = ListNode(head_values[0])
            current = head
            for value in head_values[1:]:
                current.next = ListNode(value)
                current = current.next

        result = Solution().spiralMatrix(m, n, head)
        formatted_result = format_output(result)
        results.append(formatted_result)

    with open("user.out", "w") as f:
        for result in results:
            f.write(f"{result}\n")


if __name__ == "__main__":
    kdsmain()
    exit(0)
