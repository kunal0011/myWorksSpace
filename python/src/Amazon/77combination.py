"""
LeetCode 77. Combinations

Problem Statement:
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

Example 2:
Input: n = 1, k = 1
Output: [[1]]

Constraints:
- 1 <= n <= 20
- 1 <= k <= n
"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start: int, combination: list[int]):
            # Base case: if combination is of length k, add it to result
            if len(combination) == k:
                result.append(combination[:])
                return

            # Try each number from start to n
            for i in range(start, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()

        result = []
        backtrack(1, [])
        return result


def test_combine():
    solution = Solution()

    test_cases = [
        {
            "n": 4,
            "k": 2,
            "expected": [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]],
            "description": "Standard case"
        },
        {
            "n": 1,
            "k": 1,
            "expected": [[1]],
            "description": "Single number"
        },
        {
            "n": 3,
            "k": 2,
            "expected": [[1, 2], [1, 3], [2, 3]],
            "description": "Small set"
        },
        {
            "n": 5,
            "k": 3,
            "expected": [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5],
                         [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]],
            "description": "Larger set"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        n = test_case["n"]
        k = test_case["k"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"n = {n}, k = {k}")

        result = solution.combine(n, k)
        result.sort()  # Sort for comparison
        expected.sort()

        assert result == expected, f"Expected {expected}, but got {result}"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_combine()
    print("\nAll test cases passed! 🎉")
