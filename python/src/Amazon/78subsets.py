"""
LeetCode 78. Subsets

Problem Statement:
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start: int, curr: list[int]):
            # Add current subset to result
            result.append(curr[:])

            # Try adding each remaining number
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        result = []
        backtrack(0, [])
        return result


def test_subsets():
    solution = Solution()

    test_cases = [
        {
            "nums": [1, 2, 3],
            "expected": [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]],
            "description": "Three numbers"
        },
        {
            "nums": [0],
            "expected": [[], [0]],
            "description": "Single number"
        },
        {
            "nums": [1, 2],
            "expected": [[], [1], [2], [1, 2]],
            "description": "Two numbers"
        },
        {
            "nums": [4, 5, 6, 7],
            "expected": [[], [4], [5], [6], [7], [4, 5], [4, 6], [4, 7], [5, 6], [5, 7],
                         [6, 7], [4, 5, 6], [4, 5, 7], [4, 6, 7], [5, 6, 7], [4, 5, 6, 7]],
            "description": "Four numbers"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"nums = {nums}")

        result = solution.subsets(nums)

        # Sort for comparison
        result_sorted = [sorted(subset) for subset in result]
        result_sorted.sort()
        expected_sorted = [sorted(subset) for subset in expected]
        expected_sorted.sort()

        assert result_sorted == expected_sorted, \
            f"Expected {expected_sorted}, but got {result_sorted}"
        print("✓ Test case passed!")


if __name__ == "__main__":
    test_subsets()
    print("\nAll test cases passed! 🎉")
