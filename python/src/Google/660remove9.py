"""
LeetCode 660 - Remove 9

Problem Statement:
Start from integer 1, remove any integer that contains 9 such as 9, 19, 29...
Now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, ...
Given a positive integer n, you need to return the nth integer after removing 9.

Logic:
1. Key insight: The sequence forms numbers in base-9
2. For example:
   - In decimal: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12...
   - Maps to base-9: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11...
3. Solution approach:
   - Convert given decimal number to base-9
   - This automatically handles removing numbers containing 9

Time Complexity: O(log n) - number of digits in n
Space Complexity: O(1) - only using constant extra space
"""


class Solution:
    def newInteger(self, n: int) -> int:
        # Convert the number `n` to its base-9 equivalent.
        # Since we're excluding the digit 9, the numbers are essentially base-9 numbers.
        res = 0
        base = 1
        while n > 0:
            res += (n % 9) * base
            n //= 9
            base *= 10
        return res


def test_remove_9():
    solution = Solution()

    test_cases = [
        {
            'n': 9,
            'expected': 10,
            'description': "First number after 8"
        },
        {
            'n': 19,
            'expected': 21,
            'description': "Numbers containing 9 are skipped"
        },
        {
            'n': 1,
            'expected': 1,
            'description': "First number in sequence"
        },
        {
            'n': 100,
            'expected': 121,
            'description': "Larger number conversion"
        }
    ]

    print("Testing Remove 9 Solution:")
    for i, test in enumerate(test_cases, 1):
        result = solution.newInteger(test['n'])
        print(f"\nTest Case {i} ({test['description']}):")
        print(f"Input n: {test['n']}")
        print(f"Expected: {test['expected']}")
        print(f"Result: {result}")
        print(
            f"Status: {'PASSED' if result == test['expected'] else 'FAILED'}")

        # Additional information for understanding
        if i == 1:
            print("\nFirst 15 numbers in sequence:")
            print([solution.newInteger(x) for x in range(1, 16)])


if __name__ == "__main__":
    test_remove_9()
