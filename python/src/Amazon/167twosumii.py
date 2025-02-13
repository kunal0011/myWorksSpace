"""
LeetCode 167. Two Sum II - Input Array Is Sorted

Problem Statement:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Return the indices of the two numbers, index1 and index2, as a 1-indexed array.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3.

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2.

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution
"""

from typing import List, Tuple


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two pointer approach.
        Time complexity: O(n)
        Space complexity: O(1)
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return []  # No solution found (shouldn't happen given constraints)

    def twoSumWithSteps(self, numbers: List[int], target: int) -> Tuple[List[int], List[dict]]:
        """
        Two pointer approach with step tracking.
        Time complexity: O(n)
        Space complexity: O(n) for tracking steps
        """
        steps = []
        left, right = 0, len(numbers) - 1

        steps.append({
            "action": "Initialize",
            "left": left,
            "right": right,
            "left_value": numbers[left],
            "right_value": numbers[right]
        })

        while left < right:
            current_sum = numbers[left] + numbers[right]

            steps.append({
                "action": "Check sum",
                "left": left,
                "right": right,
                "left_value": numbers[left],
                "right_value": numbers[right],
                "current_sum": current_sum,
                "target": target
            })

            if current_sum == target:
                result = [left + 1, right + 1]
                steps.append({
                    "action": "Found solution",
                    "indices": result,
                    "values": [numbers[left], numbers[right]]
                })
                return result, steps
            elif current_sum < target:
                steps.append({
                    "action": "Move left",
                    "reason": f"Sum {current_sum} < target {target}"
                })
                left += 1
            else:
                steps.append({
                    "action": "Move right",
                    "reason": f"Sum {current_sum} > target {target}"
                })
                right -= 1

        return [], steps


def visualize_steps(numbers: List[int], target: int, steps: List[dict]) -> None:
    """Helper function to visualize the two pointer approach."""
    print("\nTwo Pointer Steps:")
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step['action']}")

        if step['action'] == "Initialize":
            print(
                f"Left pointer at index {step['left']} (value: {step['left_value']})")
            print(
                f"Right pointer at index {step['right']} (value: {step['right_value']})")

        elif step['action'] == "Check sum":
            print(
                f"Left pointer at index {step['left']} (value: {step['left_value']})")
            print(
                f"Right pointer at index {step['right']} (value: {step['right_value']})")
            print(f"Current sum: {step['current_sum']}")
            print(f"Target: {step['target']}")

        elif step['action'] == "Found solution":
            print(f"Found solution at indices: {step['indices']}")
            print(f"Values: {step['values']}")

        elif step['action'] in ["Move left", "Move right"]:
            print(f"Reason: {step['reason']}")


def test_two_sum():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "numbers": [2, 7, 11, 15],
            "target": 9,
            "expected": [1, 2],
            "description": "Basic case"
        },
        {
            "numbers": [2, 3, 4],
            "target": 6,
            "expected": [1, 3],
            "description": "Three numbers"
        },
        {
            "numbers": [-1, 0],
            "target": -1,
            "expected": [1, 2],
            "description": "Negative numbers"
        },
        {
            "numbers": [1, 2, 3, 4, 5, 6, 7],
            "target": 13,
            "expected": [6, 7],
            "description": "Larger array"
        },
        {
            "numbers": [-10, -8, -2, 1, 2, 5, 6],
            "target": -12,
            "expected": [1, 2],
            "description": "Mixed numbers"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Numbers: {test_case['numbers']}")
        print(f"Target: {test_case['target']}")

        # Test both implementations
        result1 = solution.twoSum(test_case['numbers'], test_case['target'])
        result2, steps = solution.twoSumWithSteps(
            test_case['numbers'], test_case['target'])

        print(f"\nResults:")
        print(f"Found indices: {result1}")

        visualize_steps(test_case['numbers'], test_case['target'], steps)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"

        # Verify solution
        if result1:
            sum_values = test_case['numbers'][result1[0] -
                                              1] + test_case['numbers'][result1[1]-1]
            assert sum_values == test_case['target'], \
                f"Invalid solution. Sum {sum_values} != target {test_case['target']}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_two_sum()
