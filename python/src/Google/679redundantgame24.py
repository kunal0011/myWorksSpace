"""
LeetCode 679: 24 Game

Problem Statement:
You are given an array of 4 integers nums, all between 1 and 9 inclusive.
Return true if it's possible to build the number 24 by using addition, subtraction, multiplication, and division 
operations (+, -, *, /) among all 4 numbers, and false otherwise.
Note: You have to use each number exactly once and in any order.

Example:
Input: nums = [4, 1, 8, 7]
Output: true
Explanation: (8-4) * (7-1) = 24

Logic:
1. Use DFS (Depth First Search) to try all possible combinations of operations
2. For each recursive step:
   - If only one number remains, check if it equals 24 (within epsilon for floating point comparison)
   - For each pair of numbers, try all four operations
   - Create a new list with remaining numbers and the result
3. Key optimizations:
   - Use epsilon comparison for floating point arithmetic
   - Handle division by zero cases
   - Backtrack after each operation

Time Complexity: O(4^3) = O(64) operations for selecting numbers, with 4 possible operations = O(256)
Space Complexity: O(1) since input is always 4 numbers
"""

from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        EPSILON = 1e-6

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            # Iterate over every possible pair of numbers
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        # Prepare a new list for the next recursion
                        newNums = []
                        # Add all numbers except nums[i] and nums[j] into newNums
                        for k in range(len(nums)):
                            if k != i and k != j:
                                newNums.append(nums[k])

                        # Try all operations
                        for op in ['+', '-', '*', '/']:
                            # Apply each operation and append the result to newNums
                            if op == '+':
                                newNums.append(nums[i] + nums[j])
                            elif op == '-':
                                newNums.append(nums[i] - nums[j])
                            elif op == '*':
                                newNums.append(nums[i] * nums[j])
                            elif op == '/' and abs(nums[j]) > EPSILON:
                                newNums.append(nums[i] / nums[j])
                            else:
                                continue

                            # Recur to see if this path leads to 24
                            if dfs(newNums):
                                return True

                            # Undo the addition for backtracking
                            newNums.pop()
            return False

        return dfs(nums)


def test_24_game():
    # Test case 1: Valid case
    print("Test Case 1:")
    solution = Solution()
    nums = [4, 1, 8, 7]
    print(f"Input: {nums}")
    print(f"Can make 24? {solution.judgePoint24(nums)}")  # Expected: True

    # Test case 2: Another valid case
    print("\nTest Case 2:")
    nums = [1, 2, 1, 2]
    print(f"Input: {nums}")
    print(f"Can make 24? {solution.judgePoint24(nums)}")  # Expected: True

    # Test case 3: Impossible case
    print("\nTest Case 3:")
    nums = [1, 1, 1, 1]
    print(f"Input: {nums}")
    print(f"Can make 24? {solution.judgePoint24(nums)}")  # Expected: False

    # Test case 4: Case requiring division
    print("\nTest Case 4:")
    nums = [3, 3, 8, 8]
    print(f"Input: {nums}")
    print(f"Can make 24? {solution.judgePoint24(nums)}")  # Expected: True


if __name__ == "__main__":
    test_24_game()
