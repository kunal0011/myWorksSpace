from typing import List
from collections import Counter

"""
LeetCode 47. Permutations II

Problem Statement:
Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]
Explanation: The input array has two 1's. All unique permutations are listed.

Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Explanation: All possible permutations are listed.

Constraints:
- 1 <= nums.length <= 8
- -10 <= nums[i] <= 10

Solution Logic:
1. Use Counter to keep track of available numbers and their frequencies
2. Use backtracking to build permutations
3. For each position:
   - Try each unique number that still has remaining count
   - Decrement count, add to path, recurse
   - After recursion, restore count and remove from path
4. When path length equals array length, we've found a valid permutation

Time Complexity: O(n!)
Space Complexity: O(n) for recursion stack
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(counter: Counter, path: List[int]) -> None:
            # Base case: found a valid permutation
            if len(path) == len(nums):
                result.append(path[:])
                return

            # Try each unique number from counter
            for num in counter:
                if counter[num] > 0:
                    # Use this number
                    counter[num] -= 1
                    path.append(num)

                    # Recurse with updated counter and path
                    backtrack(counter, path)

                    # Backtrack: restore counter and path
                    path.pop()
                    counter[num] += 1

        result = []
        backtrack(Counter(nums), [])
        return result


def explain_solution(nums: List[int]) -> None:
    """
    Explains the solution process step by step with detailed visualization
    """
    print(f"\nGenerating unique permutations for: {nums}")
    print("=" * 50)

    def backtrack(counter: Counter, path: List[int], depth: int = 0) -> None:
        indent = "  " * depth
        print(f"{indent}Current path: {path}")
        print(f"{indent}Available numbers: {dict(counter)}")

        if len(path) == len(nums):
            print(f"{indent}✓ Found valid permutation: {path}")
            result.append(path[:])
            return

        for num in counter:
            if counter[num] > 0:
                print(
                    f"{indent}Trying {num} (remaining count: {counter[num]})")
                counter[num] -= 1
                path.append(num)
                backtrack(counter, path, depth + 1)
                path.pop()
                counter[num] += 1
                print(f"{indent}Backtrack: removed {num}, restored count")

    result = []
    counter = Counter(nums)
    print(f"Initial frequency count: {dict(counter)}")
    backtrack(counter, [])

    print("\nAll unique permutations found:")
    for perm in result:
        print(perm)
    return result


def test_permutations():
    """
    Comprehensive test cases to verify the solution
    """
    solution = Solution()
    test_cases = [
        {
            "nums": [1, 1, 2],
            "expected": [[1, 1, 2], [1, 2, 1], [2, 1, 1]],
            "description": "Basic case with duplicates"
        },
        {
            "nums": [1, 2, 3],
            "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]],
            "description": "No duplicates"
        },
        {
            "nums": [1, 1, 1],
            "expected": [[1, 1, 1]],
            "description": "All same numbers"
        },
        {
            "nums": [1],
            "expected": [[1]],
            "description": "Single number"
        },
        {
            "nums": [1, 1, 2, 2],
            "expected": [[1, 1, 2, 2], [1, 2, 1, 2], [1, 2, 2, 1],
                         [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1]],
            "description": "Multiple duplicates"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: nums = {nums}")

        result = solution.permuteUnique(nums.copy())
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)

        assert result_sorted == expected_sorted, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_permutations()
        print("\nAll test cases passed successfully! 🎉")

        # Demonstrate solution process with examples
        explain_solution([1, 1, 2])
        explain_solution([1, 2, 2])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
