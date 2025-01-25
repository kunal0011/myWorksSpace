from typing import List

"""
LeetCode 40. Combination Sum II

Problem Statement:
Given a collection of candidate numbers (candidates) and a target number (target), find all 
unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6], [1,2,5], [1,7], [2,6]]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2], [5]]

Constraints:
1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(remain: int, combo: List[int], start: int) -> None:
            if remain == 0:
                result.append(combo[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                # Skip if candidate is too large
                if candidates[i] > remain:
                    break

                combo.append(candidates[i])
                # Note: i + 1 as we can't reuse
                backtrack(remain - candidates[i], combo, i + 1)
                combo.pop()

        # Sort candidates to handle duplicates and optimize
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
            # Skip duplicates
            if i > start and candidates[i] == candidates[i-1]:
                print(f"{indent}Skip duplicate {candidates[i]}")
                continue

            if candidates[i] > remain:
                print(f"{indent}✗ {candidates[i]} is too large, breaking...")
                break

            print(f"{indent}Try adding {candidates[i]}")
            combo.append(candidates[i])

            backtrack_with_explanation(
                remain - candidates[i], combo, i + 1, depth + 1)

            removed = combo.pop()
            print(f"{indent}Backtrack: remove {removed}")

    candidates.sort()
    print(f"Sorted candidates: {candidates}")
    result = []
    backtrack_with_explanation(target, [], 0, 0)
    print("\nFinal result:", result)


def test_combination_sum2():
    """
    Test function to verify the combinationSum2 solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "candidates": [10, 1, 2, 7, 6, 1, 5],
            "target": 8,
            "expected": [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]],
            "description": "Multiple combinations with duplicates"
        },
        {
            "candidates": [2, 5, 2, 1, 2],
            "target": 5,
            "expected": [[1, 2, 2], [5]],
            "description": "Multiple duplicates in candidates"
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
            "expected": [],
            "description": "No valid combinations"
        },
        {
            "candidates": [1, 1, 1, 1, 1],
            "target": 3,
            "expected": [[1, 1, 1]],
            "description": "Multiple same numbers"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        candidates = test_case["candidates"]
        target = test_case["target"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: candidates = {candidates}, target = {target}")

        result = solution.combinationSum2(candidates.copy(), target)

        # Sort for comparison
        result = sorted(sorted(combo) for combo in result)
        expected = sorted(sorted(combo) for combo in expected)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_combination_sum2()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with examples
        explain_backtracking([10, 1, 2, 7, 6, 1, 5], 8)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
