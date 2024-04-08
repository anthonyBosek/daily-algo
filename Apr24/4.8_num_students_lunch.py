"""
    1700. Number of Students Unable to Eat Lunch
    https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

    The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue.
        Each student either prefers square or circular sandwiches.

    The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

        - If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
        - Otherwise, they will leave it and go to the queue's end.
    This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

    You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack)
        and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue).
        Return the number of students that are unable to eat.

"""


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cntr = 0
        while True:
            if len(students) == 0:
                return 0
            if len(students) == cntr:
                return cntr
            if students[0] == sandwiches[0]:
                cntr = 0
                students.pop(0)
                sandwiches.pop(0)
            else:
                cntr += 1
                students.append(students.pop(0))

        # -----------------------------------------------------------------------

        # dq_st, dq_sa = deque(students), deque(sandwiches)
        # counter = 0
        # while dq_st:
        #     if counter == len(dq_st):
        #         break

        #     cur_st = dq_st.popleft()
        #     if cur_st == dq_sa[0]:
        #         dq_sa.popleft()
        #         counter = 0
        #     else:
        #         dq_st.append(cur_st)
        #         counter += 1
        # return len(dq_st)

        # -----------------------------------------------------------------------

        # # Count the number of students who prefer circular and square sandwiches
        # count = [0, 0]
        # for student in students:
        #     count[student] += 1

        # # Iterate through the sandwiches
        # for sandwich in sandwiches:
        #     # If the student prefers the sandwich, decrement the count
        #     if count[sandwich] > 0:
        #         count[sandwich] -= 1
        #     # If the student does not prefer the sandwich, break
        #     else:
        #         break

        # # Return the number of students who are unable to eat
        # return count[0] + count[1]
