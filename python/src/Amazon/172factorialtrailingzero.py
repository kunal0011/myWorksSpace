"""
LeetCode 172. Factorial Trailing Zeroes

Problem Statement:
Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1.

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0

Constraints:
- 0 <= n <= 10^4
"""

from typing import List, Tuple


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Count trailing zeroes in n!
        Time complexity: O(log n)
        Space complexity: O(1)
        """
        count = 0
        power_of_5 = 5

        while power_of_5 <= n:
            count += n // power_of_5
            power_of_5 *= 5

        return count

    def trailingZeroesWithSteps(self, n: int) -> Tuple[int, List[dict]]:
        """
        Count trailing zeroes with detailed steps.
        Time complexity: O(log n)
        Space complexity: O(log n) for tracking steps
        """
        steps = []
        count = 0
        power_of_5 = 5

        steps.append({
            "action": "Initialize",
            "n": n,
            "explanation": "Trailing zeros come from pairs of 2 and 5. Since 2s are always more than 5s, "
            "we only need to count the number of 5s."
        })

        while power_of_5 <= n:
            contribution = n // power_of_5
            count += contribution

            steps.append({
                "action": "Count fives",
                "power_of_5": power_of_5,
                "contribution": contribution,
                "running_count": count,
                "explanation": f"Numbers divisible by {power_of_5} contribute {contribution} fives"
            })

            power_of_5 *= 5

        steps.append({
            "action": "Final result",
            "n": n,
            "factorial": f"{n}!",
            "trailing_zeroes": count
        })

        return count, steps

    def calculateFactorial(self, n: int) -> int:
        """Helper function to calculate factorial for small numbers."""
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


def visualize_steps(n: int, steps: List[dict]) -> None:
    """Helper function to visualize counting steps."""
    print("\nCounting Steps:")
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step['action']}")

        if step['action'] == "Initialize":
            print(f"Input number: {step['n']}")
            print(f"Note: {step['explanation']}")

        elif step['action'] == "Count fives":
            print(f"Checking multiples of {step['power_of_5']}")
            print(f"Found {step['contribution']} numbers contributing fives")
            print(f"Running count: {step['running_count']}")
            print(f"Explanation: {step['explanation']}")

        elif step['action'] == "Final result":
            print(f"Input: {step['n']}")
            print(f"Factorial: {step['factorial']}")
            print(f"Trailing zeroes: {step['trailing_zeroes']}")


def test_trailing_zeroes():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "n": 3,
            "expected": 0,
            "description": "No trailing zeros"
        },
        {
            "n": 5,
            "expected": 1,
            "description": "One trailing zero"
        },
        {
            "n": 10,
            "expected": 2,
            "description": "Multiple trailing zeros"
        },
        {
            "n": 25,
            "expected": 6,
            "description": "Power of 5"
        },
        {
            "n": 0,
            "expected": 0,
            "description": "Zero input"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print(f"Input n: {test_case['n']}")

        # Test both implementations
        result1 = solution.trailingZeroes(test_case['n'])
        result2, steps = solution.trailingZeroesWithSteps(test_case['n'])

        print(f"\nResults:")
        print(f"Trailing zeroes: {result1}")

        visualize_steps(test_case['n'], steps)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"

        # Verify result for small numbers
        if test_case['n'] <= 20:  # Limit verification to small numbers
            factorial = solution.calculateFactorial(test_case['n'])
            actual_zeros = len(str(factorial)) - \
                len(str(factorial).rstrip('0'))
            assert actual_zeros == result1, \
                f"Wrong number of trailing zeros. Expected {actual_zeros}, got {result1}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_trailing_zeroes()
