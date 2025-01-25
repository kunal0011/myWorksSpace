"""
LeetCode 90. Subsets II

Problem Statement:
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]

Constraints:
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
"""


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        def backtrack(start: int, curr: list[int]):
            result.append(curr[:])

            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        result = []
        nums.sort()  # Sort to handle duplicates
        backtrack(0, [])
        return result


def test_subsets_with_dup():
    solution = Solution()

    test_cases = [
        {
            "nums": [1, 2, 2],
            "expected": [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]],
            "description": "Array with duplicates"
        },
        {
            "nums": [0],
            "expected": [[], [0]],
            "description": "Single element"
        },
        {
            "nums": [1, 1, 1],
            "expected": [[], [1], [1, 1], [1, 1, 1]],
            "description": "All same elements"
        },
        {
            "nums": [1, 2, 3],
            "expected": [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]],
            "description": "No duplicates"
        },
        {
            "nums": [4, 4, 4, 1, 4],
            "expected": [[], [1], [1, 4], [1, 4, 4], [1, 4, 4, 4], [1, 4, 4, 4, 4],
                         [4], [4, 4], [4, 4, 4], [4, 4, 4, 4]],
            "description": "Multiple duplicates"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input: nums = {nums}")

        result = solution.subsetsWithDup(nums)

        # Sort both result and expected for comparison
        result_sorted = [sorted(subset) for subset in result]
        result_sorted.sort()
        expected_sorted = [sorted(subset) for subset in expected]
        expected_sorted.sort()

        assert result_sorted == expected_sorted, \
            f"Expected {expected_sorted}, but got {result_sorted}"
        print("✓ Test case passed!")
        print(f"Generated subsets: {result}")


if __name__ == "__main__":
    test_subsets_with_dup()
    print("\nAll test cases passed! 🎉")
