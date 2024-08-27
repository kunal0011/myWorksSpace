from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operations = []
        target_index = 0

        # Iterate through numbers from 1 to n
        for i in range(1, n + 1):
            # If we've built the entire target array, break the loop
            if target_index == len(target):
                break

            # If the current number matches the target element, push it
            if i == target[target_index]:
                operations.append("Push")
                target_index += 1
            # Otherwise, push and pop it to ignore the number
            else:
                operations.append("Push")
                operations.append("Pop")

        return operations
