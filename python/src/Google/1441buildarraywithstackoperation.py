"""
LeetCode 1441. Build an Array With Stack Operations

Problem Statement:
You are given an array target and an integer n. In each iteration, you will read a number from 1 to n.
Build the target array using the following operations:
- "Push": Reads a new element from the beginning array, and pushes it in the array.
- "Pop": Deletes the last element of the array.
If the target array is already built, stop reading more elements.
Return a list of the operations needed to build target. The test cases are generated so that the answer is unique.

Time Complexity: O(n) where n is the input parameter
Space Complexity: O(m) where m is the length of operations list
"""

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # Logic:
        # 1. Iterate through numbers 1 to n
        # 2. For each number i:
        #    - If i matches current target number, "Push" it and move to next target
        #    - If i doesn't match, "Push" then "Pop" it (effectively skipping it)
        # 3. Stop when we've built the complete target array

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


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 3], 3),              # Should output: ["Push", "Push", "Pop", "Push"]
        ([1, 2, 3], 3),          # Should output: ["Push", "Push", "Push"]
        ([1, 2], 4),             # Should output: ["Push", "Push"]
        # Should output: ["Push", "Pop", "Push", "Push", "Push"]
        ([2, 3, 4], 4)
    ]

    for i, (target, n) in enumerate(test_cases):
        result = solution.buildArray(target, n)
        print(f"Test case {i + 1}:")
        print(f"Target: {target}")
        print(f"n: {n}")
        print(f"Operations: {result}")
        print()
