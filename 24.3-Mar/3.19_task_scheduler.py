"""
    621. Task Scheduler
    https://leetcode.com/problems/task-scheduler/

    You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each
        cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's
        a constraint: identical tasks must be separated by at least n intervals due to cooling time.

    ​Return the minimum number of intervals required to complete all tasks.

"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord("A")] += 1

        # Sort the frequency array in descending order
        freq.sort()

        # Find the maximum frequency
        max_freq = freq[-1]

        # Count the number of tasks with the maximum frequency
        count = 1
        for i in range(24, -1, -1):
            if freq[i] == max_freq:
                count += 1
            else:
                break

        # Calculate the minimum number of intervals required
        result = (max_freq - 1) * (n + 1) + count
        return max(result, len(tasks))

        # ---------------------------------------------------

        # # Create a dictionary to store the frequency of each task
        # task_freq = {}
        # for task in tasks:
        #     if task in task_freq:
        #         task_freq[task] += 1
        #     else:
        #         task_freq[task] = 1

        # # Sort the tasks based on their frequency
        # task_freq = sorted(task_freq.values(), reverse=True)

        # # Get the maximum frequency
        # max_freq = task_freq[0]

        # # Count the number of tasks with the maximum frequency
        # max_freq_count = 0
        # for freq in task_freq:
        #     if freq == max_freq:
        #         max_freq_count += 1
        #     else:
        #         break

        # # Calculate the number of intervals required to complete all tasks
        # intervals = (max_freq - 1) * (n + 1) + max_freq_count

        # # Return the maximum of the calculated intervals and the length of the tasks array
        # return max(intervals, len(tasks))

        # ---------------------------------------------------

        # task_map = [0] * 26
        # for task in tasks:
        #     task_map[ord(task) - ord('A')] += 1
        # task_map.sort()
        # max_val = task_map[25] - 1
        # idle_slots = max_val * n
        # for i in range(24, -1, -1):
        #     idle_slots -= min(task_map[i], max_val)
        # return len(tasks) + max(0, idle_slots)
