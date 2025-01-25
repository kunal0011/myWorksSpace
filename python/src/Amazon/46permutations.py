from typing import List

"""
LeetCode 46. Permutations

Problem Statement:
Given an array nums of distinct integers, return all possible permutations.
You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
- 1 <= nums.length <= 6
- -10 <= nums[i] <= 10
- All the integers of nums are unique
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int) -> None:
            if start == len(nums):
                # When we've used all numbers, add the permutation to results
                result.append(nums[:])
                return

            # Try each number as the next element
            for i in range(start, len(nums)):
                # Swap current position with i
                nums[start], nums[i] = nums[i], nums[start]

                # Recursively generate permutations for rest of array
                backtrack(start + 1)

                # Backtrack by restoring the swap
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result


def explain_permutations(nums: List[int]) -> None:
    """
    Function to explain the permutation generation process step by step
    """
    print(f"\nGenerating permutations for: {nums}")
    print("=" * 50)

    def backtrack(start: int, depth: int) -> None:
        indent = "  " * depth
        print(f"{indent}Current array: {nums}, start: {start}")

        if start == len(nums):
            print(f"{indent}✓ Found permutation: {nums[:]}")
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            print(f"{indent}Swapping positions {start} and {i}: "
                  f"{nums[start]} <-> {nums[i]}")

            nums[start], nums[i] = nums[i], nums[start]
            print(f"{indent}After swap: {nums}")

            backtrack(start + 1, depth + 1)

            nums[start], nums[i] = nums[i], nums[start]
            print(f"{indent}Backtracked: {nums}")

    result = []
    backtrack(0, 0)

    print("\nAll permutations:")
    for perm in result:
        print(perm)

    return result


def test_permutations():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "nums": [1, 2, 3],
            "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            "description": "Three numbers"
        },
        {
            "nums": [0, 1],
            "expected": [[0, 1], [1, 0]],
            "description": "Two numbers"
        },
        {
            "nums": [1],
            "expected": [[1]],
            "description": "Single number"
        },
        {
            "nums": [1, 2, 3, 4],
            "expected": None,  # Too many to list explicitly
            "description": "Four numbers"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: nums = {nums}")

        result = solution.permute(nums.copy())

        if expected is not None:
            # Sort both lists for comparison
            result_sorted = sorted(map(lambda x: sorted(x), result))
            expected_sorted = sorted(map(lambda x: sorted(x), expected))

            assert result_sorted == expected_sorted, \
                f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        else:
            # For larger inputs, just verify the number of permutations
            expected_length = 1
            for j in range(1, len(nums) + 1):
                expected_length *= j
            assert len(result) == expected_length, \
                f"\nTest case {i} failed!\nExpected length: {expected_length}\nGot length: {len(result)}"

        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_permutations()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_permutations([1, 2, 3])
        explain_permutations([0, 1])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
