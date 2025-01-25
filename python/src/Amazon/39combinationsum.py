from typing import List

"""
LeetCode 39. Combination Sum

Problem Statement:
Given an array of distinct integers candidates and a target integer target, return a list 
of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 + 2 + 3 = 7
7 = 7

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Constraints:
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct
1 <= target <= 40
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain: int, combo: List[int], start: int) -> None:
            if remain == 0:
                # Found a valid combination
                result.append(combo[:])
                return

            for i in range(start, len(candidates)):
                # Skip if candidate is too large
                if candidates[i] > remain:
                    continue

                # Add candidate to combination
                combo.append(candidates[i])

                # Recursively find combinations with updated remain
                # Note: we pass i instead of i+1 because we can reuse same element
                backtrack(remain - candidates[i], combo, i)

                # Backtrack by removing the last added candidate
                combo.pop()

        # Sort candidates to optimize skipping too large numbers
        candidates.sort()
        result = []
        backtrack(target, [], 0)
        return result


def explain_backtracking(candidates: List[int], target: int) -> None:
    """
    Function to explain the backtracking process step by step
    """
    print(f"\nFinding combinations for target {target} using {candidates}")
    print("=" * 50)

    def backtrack_with_explanation(remain: int, combo: List[int], start: int, depth: int) -> None:
        indent = "  " * depth
        print(f"{indent}Current combination: {combo}")
        print(f"{indent}Remaining target: {remain}")

        if remain == 0:
            print(f"{indent}✓ Found valid combination: {combo}")
            result.append(combo[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                print(f"{indent}✗ {candidates[i]} is too large, skipping...")
                continue

            print(f"{indent}Try adding {candidates[i]}")
            combo.append(candidates[i])

            backtrack_with_explanation(
                remain - candidates[i], combo, i, depth + 1)

            removed = combo.pop()
            print(f"{indent}Backtrack: remove {removed}")

    candidates.sort()
    result = []
    backtrack_with_explanation(target, [], 0, 0)
    print("\nFinal result:", result)


def test_combination_sum():
    """
    Test function to verify the combinationSum solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "candidates": [2, 3, 6, 7],
            "target": 7,
            "expected": [[2, 2, 3], [7]],
            "description": "Basic case"
        },
        {
            "candidates": [2, 3, 5],
            "target": 8,
            "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
            "description": "Multiple combinations"
        },
        {
            "candidates": [2],
            "target": 1,
            "expected": [],
            "description": "No valid combinations"
        },
        {
            "candidates": [1],
            "target": 1,
            "expected": [[1]],
            "description": "Single candidate equals target"
        },
        {
            "candidates": [1],
            "target": 2,
            "expected": [[1, 1]],
            "description": "Need to reuse candidate"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        candidates = test_case["candidates"]
        target = test_case["target"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: candidates = {candidates}, target = {target}")

        result = solution.combinationSum(candidates.copy(), target)

        # Sort for comparison
        result = sorted(sorted(combo) for combo in result)
        expected = sorted(sorted(combo) for combo in expected)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_combination_sum()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with an example
        explain_backtracking([2, 3, 6, 7], 7)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
