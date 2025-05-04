"""
LeetCode 771: Jewels and Stones

Problem Statement:
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Logic:
1. Convert jewels string to a set for O(1) lookup time
2. Iterate through stones and count how many are in jewels set
3. Use list comprehension with sum() for a concise solution

Time Complexity: O(J + S) where J is length of jewels and S is length of stones
Space Complexity: O(J) for storing the jewels set
"""

from typing import List


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # Convert J to a set for O(1) lookups
        jewels = set(J)
        # Count how many stones in S are also jewels
        return sum(s in jewels for s in S)


def test_jewels_and_stones():
    solution = Solution()

    # Test case 1: Basic case with mixed case
    jewels1 = "aA"
    stones1 = "aAAbbbb"
    result1 = solution.numJewelsInStones(jewels1, stones1)
    assert result1 == 3, f"Test case 1 failed. Expected 3, got {result1}"
    print(
        f"Test case 1 passed: jewels={jewels1}, stones={stones1}, count={result1}")

    # Test case 2: No matching jewels
    jewels2 = "z"
    stones2 = "ZZ"
    result2 = solution.numJewelsInStones(jewels2, stones2)
    assert result2 == 0, f"Test case 2 failed. Expected 0, got {result2}"
    print(
        f"\nTest case 2 passed: jewels={jewels2}, stones={stones2}, count={result2}")

    # Test case 3: All stones are jewels
    jewels3 = "abc"
    stones3 = "abc"
    result3 = solution.numJewelsInStones(jewels3, stones3)
    assert result3 == 3, f"Test case 3 failed. Expected 3, got {result3}"
    print(
        f"\nTest case 3 passed: jewels={jewels3}, stones={stones3}, count={result3}")

    # Test case 4: Empty strings
    jewels4 = ""
    stones4 = ""
    result4 = solution.numJewelsInStones(jewels4, stones4)
    assert result4 == 0, f"Test case 4 failed. Expected 0, got {result4}"
    print(
        f"\nTest case 4 passed: jewels={jewels4}, stones={stones4}, count={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_jewels_and_stones()
