"""
LeetCode 621 - Task Scheduler

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks 
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of time that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: A -> B -> A -> B -> A -> B

Constraints:
- 1 <= task.length <= 10^4
- tasks[i] is uppercase English letter
- 0 <= n <= 100
"""

from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)

        # Get the maximum frequency of any task
        max_freq = max(task_counts.values())

        # Count how many tasks have the maximum frequency
        max_count = sum(1 for count in task_counts.values() if count == max_freq)

        # Calculate the minimum length of time required
        # Formula: (max_freq - 1) * (n + 1) + max_count
        # Explanation:
        # - We need (max_freq - 1) intervals of length (n + 1) for the most frequent tasks
        # - Then we add max_count for the last row of tasks
        # - Finally, we take max with len(tasks) to handle cases where n is small
        part_count = max_freq - 1
        part_length = n + 1
        empty_slots = part_count * part_length
        total_slots = empty_slots + max_count

        return max(len(tasks), total_slots)
    
    def leastInterval_simulation(self, tasks: List[str], n: int) -> int:
        """
        Alternative solution using simulation approach.
        This is less efficient but might be easier to understand.
        Time Complexity: O(total_time)
        Space Complexity: O(1) since we only store 26 characters
        """
        if n == 0:
            return len(tasks)
            
        task_counts = Counter(tasks)
        time = 0
        while any(count > 0 for count in task_counts.values()):
            # Sort tasks by remaining count
            available = sorted([(count, task) for task, count in task_counts.items() if count > 0],
                            reverse=True)
            
            # Try to schedule up to n+1 different tasks
            scheduled = 0
            for _ in range(min(n + 1, len(available))):
                if available:
                    count, task = available[0]
                    task_counts[task] -= 1
                    available.pop(0)
                    scheduled += 1
            
            # If we scheduled any tasks or there are still tasks remaining,
            # we need to account for this time slot
            if scheduled > 0 or any(count > 0 for count in task_counts.values()):
                time += max(scheduled, min(n + 1, len(tasks)))
                
        return time


def test_task_scheduler():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        (["A","A","A","B","B","B"], 2, 8),
        (["A","A","A","B","B","B"], 0, 6),
        (["A","A","A","A","A","A","B","C","D","E","F","G"], 2, 16),
        
        # Edge cases
        (["A"], 1, 1),
        (["A","A"], 2, 4),
        
        # Test cases with varying cooldown periods
        (["A","A","A","B","B","B","C","C"], 1, 8),
        (["A","A","A","B","B","B"], 1, 6),
        
        # Complex test cases
        (["A","A","A","B","B","B","C","C","C","D","D","E"], 2, 12),
        (["A","A","A","A","B","B","B","B","C","C","C","C"], 1, 12),
        
        # Test cases with single task type
        (["A","A","A","A"], 3, 10),
        (["A","A","A","A"], 0, 4),
        
        # Test cases with many different tasks
        (["A","B","C","D","E","F","G","H","I","J"], 0, 10),
        (["A","B","C","D","A","B","C","D"], 3, 8),
    ]
    
    print("Running tests for Task Scheduler...\n")
    
    for i, (tasks, n, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result = solution.leastInterval(tasks, n)
        result_sim = solution.leastInterval_simulation(tasks, n)
        
        print(f"Test Case {i}:")
        print(f"Input: tasks = {tasks}, n = {n}")
        print(f"Expected: {expected}")
        print(f"Optimized Solution: {result} {'✅' if result == expected else '❌'}")
        print(f"Simulation Solution: {result_sim} {'✅' if result_sim == expected else '❌'}")
        
        if result != expected:
            print(f"❌ Test case failed!")
            print(f"Got: {result}")
            print(f"Expected: {expected}")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_task_scheduler()
