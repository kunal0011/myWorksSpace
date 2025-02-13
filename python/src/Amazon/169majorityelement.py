"""
LeetCode 169. Majority Element

Problem Statement:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n/2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
"""

from typing import List, Dict, Tuple
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

    def majorityElementWithSteps(self, nums: List[int]) -> Tuple[int, List[dict]]:
        """
        Boyer-Moore Voting Algorithm with step tracking.
        Time complexity: O(n)
        Space complexity: O(n) for tracking steps
        """
        steps = []
        count = 0
        candidate = None

        steps.append({
            "action": "Initialize",
            "count": count,
            "candidate": candidate
        })

        for i, num in enumerate(nums):
            old_count = count
            old_candidate = candidate

            if count == 0:
                candidate = num
                count = 1
            else:
                count += 1 if num == candidate else -1

            steps.append({
                "action": "Process number",
                "index": i,
                "number": num,
                "old_count": old_count,
                "old_candidate": old_candidate,
                "new_count": count,
                "new_candidate": candidate
            })

        # Verify majority (not strictly necessary given problem constraints)
        verification_count = sum(1 for num in nums if num == candidate)

        steps.append({
            "action": "Verify result",
            "candidate": candidate,
            "occurrences": verification_count,
            "total_numbers": len(nums)
        })

        return candidate, steps


def visualize_steps(nums: List[int], steps: List[dict]) -> None:
    """Helper function to visualize Boyer-Moore algorithm steps."""
    print("\nBoyer-Moore Algorithm Steps:")
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step['action']}")

        if step['action'] == "Initialize":
            print(f"Initial count: {step['count']}")
            print(f"Initial candidate: {step['candidate']}")

        elif step['action'] == "Process number":
            print(f"Processing index {step['index']}: {step['number']}")
            print(
                f"Previous state: count={step['old_count']}, candidate={step['old_candidate']}")
            print(
                f"New state: count={step['new_count']}, candidate={step['new_candidate']}")

        elif step['action'] == "Verify result":
            print(f"Final candidate: {step['candidate']}")
            print(
                f"Occurrences: {step['occurrences']}/{step['total_numbers']}")


def test_majority_element():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "nums": [3, 2, 3],
            "expected": 3,
            "description": "Simple case"
        },
        {
            "nums": [2, 2, 1, 1, 1, 2, 2],
            "expected": 2,
            "description": "Multiple elements"
        },
        {
            "nums": [1],
            "expected": 1,
            "description": "Single element"
        },
        {
            "nums": [1, 1, 1, 1, 2, 2, 2],
            "expected": 1,
            "description": "Clear majority"
        },
        {
            "nums": [-1, -1, 2, -1],
            "expected": -1,
            "description": "Negative numbers"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input array: {test_case['nums']}")

        # Test both implementations
        result1 = solution.majorityElement(test_case['nums'])
        result2, steps = solution.majorityElementWithSteps(test_case['nums'])

        print(f"\nResults:")
        print(f"Majority element: {result1}")

        visualize_steps(test_case['nums'], steps)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"

        # Verify majority
        count = sum(1 for num in test_case['nums'] if num == result1)
        assert count > len(test_case['nums']) // 2, \
            f"Result {result1} is not a majority element"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_majority_element()
