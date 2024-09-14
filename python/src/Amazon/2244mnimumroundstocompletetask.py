from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_count = Counter(tasks)
        rounds = 0

        for count in task_count.values():
            if count == 1:
                return -1  # Impossible to complete this difficulty

            # We try to maximize the use of rounds with 3 tasks
            rounds += count // 3
            if count % 3 != 0:
                rounds += 1  # Add one more round to complete the remaining tasks

        return rounds
