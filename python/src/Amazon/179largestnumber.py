"""
LeetCode 179. Largest Number

Problem Statement:
Given a list of non-negative integers nums, arrange them such that they form the largest number 
and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 10^9
"""

from typing import List, Tuple
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        """
        Create largest number from given integers.
        Time complexity: O(nlogn) where n is length of nums
        Space complexity: O(n)
        """
        # Convert to strings for easier comparison
        str_nums = [str(num) for num in nums]

        # Custom comparison
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        # Sort using custom comparison
        str_nums.sort(key=cmp_to_key(compare))

        # Handle case where all numbers are zero
        if str_nums[0] == '0':
            return '0'

        return ''.join(str_nums)

    def largestNumberWithSteps(self, nums: List[int]) -> Tuple[str, List[dict]]:
        """
        Create largest number with detailed steps.
        Time complexity: O(nlogn)
        Space complexity: O(n)
        """
        steps = []

        # Convert to strings
        str_nums = [str(num) for num in nums]
        steps.append({
            "action": "Convert to strings",
            "original": nums,
            "converted": str_nums
        })

        # Custom comparison function
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        # Track comparisons during sort
        comparisons = []

        def tracking_compare(a: str, b: str) -> int:
            result = compare(a, b)
            comparisons.append({
                "a": a,
                "b": b,
                "combined_ab": a + b,
                "combined_ba": b + a,
                "result": result
            })
            return result

        # Sort numbers
        str_nums.sort(key=cmp_to_key(tracking_compare))

        steps.append({
            "action": "Sort numbers",
            "comparisons": comparisons,
            "sorted": str_nums.copy()
        })

        # Handle all zeros case
        if str_nums[0] == '0':
            steps.append({
                "action": "Handle zeros",
                "reason": "All numbers are zero",
                "result": "0"
            })
            return "0", steps

        # Join numbers
        result = ''.join(str_nums)
        steps.append({
            "action": "Final result",
            "result": result
        })

        return result, steps


def visualize_steps(steps: List[dict]) -> None:
    """Helper function to visualize number arrangement steps."""
    print("\nArrangement Steps:")
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step['action']}")

        if step['action'] == "Convert to strings":
            print(f"Original numbers: {step['original']}")
            print(f"Converted to strings: {step['converted']}")

        elif step['action'] == "Sort numbers":
            print("Comparisons made during sort:")
            for j, comp in enumerate(step['comparisons'], 1):
                print(f"\nComparison {j}:")
                print(f"Comparing {comp['a']} and {comp['b']}")
                print(f"{comp['a'] + comp['b']} vs {comp['b'] + comp['a']}")
                print(
                    f"Result: {'a before b' if comp['result'] < 0 else 'b before a' if comp['result'] > 0 else 'equal'}")
            print(f"\nSorted arrangement: {step['sorted']}")

        elif step['action'] == "Handle zeros":
            print(f"Reason: {step['reason']}")
            print(f"Result: {step['result']}")

        elif step['action'] == "Final result":
            print(f"Largest possible number: {step['result']}")


def test_largest_number():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "nums": [10, 2],
            "expected": "210",
            "description": "Basic case"
        },
        {
            "nums": [3, 30, 34, 5, 9],
            "expected": "9534330",
            "description": "Multiple digits"
        },
        {
            "nums": [0, 0],
            "expected": "0",
            "description": "All zeros"
        },
        {
            "nums": [1],
            "expected": "1",
            "description": "Single number"
        },
        {
            "nums": [432, 43243],
            "expected": "43243432",
            "description": "Similar prefixes"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input numbers: {test_case['nums']}")

        # Test both implementations
        result1 = solution.largestNumber(test_case['nums'])
        result2, steps = solution.largestNumberWithSteps(test_case['nums'])

        print(f"\nResults:")
        print(f"Largest number: {result1}")

        visualize_steps(steps)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_largest_number()
