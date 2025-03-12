"""
LeetCode 293: Flip Game

Problem Statement:
You are playing a Flip Game with your friend. You are given a string currentState that contains only '+' and '-'.
You and your friend take turns to flip two consecutive "++" into "--". 
The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Return all possible states of the string after one valid move.

Example:
Input: currentState = "++++"
Output: ["--++", "+--+", "++--"]

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(n) for storing the result list
"""

from typing import List


class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        result = []
        if not s or len(s) < 2:
            return result

        # Convert string to list for faster manipulation
        chars = list(s)
        for i in range(len(s) - 1):
            # Check for consecutive '++'
            if chars[i] == '+' and chars[i + 1] == '+':
                # Make the flip
                chars[i] = chars[i + 1] = '-'
                result.append(''.join(chars))
                # Restore the original state
                chars[i] = chars[i + 1] = '+'

        return result


def test_flip_game():
    solution = Solution()

    # Test Case 1: Basic case
    s1 = "++++"
    result1 = solution.generatePossibleNextMoves(s1)
    expected1 = ["--++", "+--+", "++--"]
    assert sorted(result1) == sorted(expected1), f"Test case 1 failed: Expected {expected1}, got {result1}"
    print(f"Test case 1 passed: Input = '{s1}'\nOutput = {result1}")

    # Test Case 2: No possible moves
    s2 = "+-+-"
    result2 = solution.generatePossibleNextMoves(s2)
    expected2 = []
    assert result2 == expected2, f"Test case 2 failed: Expected {expected2}, got {result2}"
    print(f"\nTest case 2 passed: Input = '{s2}'\nOutput = {result2}")

    # Test Case 3: Single possible move
    s3 = "++"
    result3 = solution.generatePossibleNextMoves(s3)
    expected3 = ["--"]
    assert result3 == expected3, f"Test case 3 failed: Expected {expected3}, got {result3}"
    print(f"\nTest case 3 passed: Input = '{s3}'\nOutput = {result3}")

    # Test Case 4: Empty string
    s4 = ""
    result4 = solution.generatePossibleNextMoves(s4)
    expected4 = []
    assert result4 == expected4, f"Test case 4 failed: Expected {expected4}, got {result4}"
    print(f"\nTest case 4 passed: Input = '{s4}'\nOutput = {result4}")

    # Test Case 5: Multiple '+' with gap
    s5 = "++++++"
    result5 = solution.generatePossibleNextMoves(s5)
    expected5 = ["--++++", "+--+++", "++--++", "+++--+", "++++--"]
    assert sorted(result5) == sorted(expected5), f"Test case 5 failed: Expected {expected5}, got {result5}"
    print(f"\nTest case 5 passed: Input = '{s5}'\nOutput = {result5}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_flip_game()
