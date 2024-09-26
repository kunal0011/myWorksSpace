from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)

        # Get the maximum frequency of any task
        max_freq = max(task_counts.values())

        # Count how many tasks have the maximum frequency
        max_count = sum(1 for task, count in task_counts.items()
                        if count == max_freq)

        # Calculate the minimum length of time required
        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length
        total_slots = empty_slots + max_count

        return max(len(tasks), total_slots)
