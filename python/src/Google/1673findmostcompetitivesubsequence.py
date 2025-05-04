"""
LeetCode 1673. Find the Most Competitive Subsequence

Problem Statement:
Given an array of integers nums and a positive integer k, return the most competitive subsequence of nums of size k.
A subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b
differ, subsequence a has a number less than the corresponding number in b.

Time Complexity: O(n) where n is length of array
Space Complexity: O(k) for the stack
"""

from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # Logic:
        # 1. Use monotonic stack approach
        # 2. For each number:
        #    - While current number is smaller than stack top and we can still remove elements
        #      (we have enough numbers remaining to form k-length subsequence),
        #      pop from stack
        #    - Add current number to stack
        # 3. Return first k elements from stack

        stack = []
        to_remove = len(nums) - k

        for num in nums:
            # Pop from the stack while conditions are met
            while stack and num < stack[-1] and to_remove > 0:
                stack.pop()
                to_remove -= 1
            # Add current number to the stack
            stack.append(num)

        # Return only the first k elements of the stack
        return stack[:k]


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([3, 5, 2, 6], 2),             # Expected: [2,6]
        ([2, 4, 3, 3, 5, 4, 9, 6], 4),     # Expected: [2,3,3,4]
        ([71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2], 3),  # Expected: [8,80,2]
        ([84, 10, 71, 23, 66, 61, 62, 64, 34, 41, 80, 25, 91, 43,
         4, 75, 65, 13, 37, 41, 46, 90, 55, 8, 85, 61, 95, 71], 24)
    ]

    for i, (nums, k) in enumerate(test_cases):
        result = solution.mostCompetitive(nums, k)
        print(f"Test case {i + 1}:")
        print(f"Input array: {nums}")
        print(f"k: {k}")
        print(f"Most competitive subsequence: {result}")
        print()
