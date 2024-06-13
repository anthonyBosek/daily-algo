"""
    2037. Minimum Number of Moves to Seat Everyone
    https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/

    There are n seats and n students in a room. You are given an array seats of length n,
    where seats[i] is the position of the ith seat. You are also given the array students
    of length n, where students[j] is the position of the jth student.

    You may perform the following move any number of times:

        • Increase or decrease the position of the ith student by 1
            (i.e., moving the ith student from position x to x + 1 or x - 1)

    Return the minimum number of moves required to move each student to a seat such that no two students are in the same seat.

    **Note that there may be multiple seats or students in the same position at the beginning.

"""


def minMovesToSeat(seats, students):
    """
    :type seats: List[int]
    :type students: List[int]
    :rtype: int
    """
    #! --- Solution 1 ---
    seats.sort()
    students.sort()
    return sum(abs(seat - student) for seat, student in zip(seats, students))

    #! --- Solution 2 ---
    # students.sort()
    # seats.sort()
    # moves = 0
    # for i in range(0, len(seats)):
    #     #? Add the absolute value of the difference
    #     #? between the position of the seat and the student
    #     moves += abs(seats[i] - students[i])
    # return moves

    #! --- Solution 3 ---
    # #? Find the maximum position in the arrays
    # max_position = max(max(seats), max(students))

    # #? Stores difference between number of seats and students at each position
    # differences = [0] * (max_position)

    # #? Count the available seats at each position
    # for position in seats:
    #     differences[position - 1] += 1

    # #? Remove a seat for each student at that position
    # for position in students:
    #     differences[position - 1] -= 1

    # #? Caculate the number of moves needed to seat the students
    # moves = 0
    # unmatched = 0
    # for difference in differences:
    #     moves += abs(unmatched)
    #     unmatched += difference

    # return moves
