"""
LeetCode 89. Gray Code

Problem Statement:
An n-bit gray code sequence is a sequence of 2^n integers where:
- Every integer is in the inclusive range [0, 2^n - 1]
- The first integer is 0
- An integer appears no more than once in the sequence
- The binary representation of every pair of adjacent integers differs by exactly one bit
- The binary representation of the first and last integers differs by exactly one bit

Given an integer n, return any valid n-bit gray code sequence.

Example 1:
Input: n = 2
Output: [0,1,3,2]
Explanation:
The binary representation of [0,1,3,2] is [00,01,11,10].
- 00 and 01 differ by one bit
- 01 and 11 differ by one bit
- 11 and 10 differ by one bit
- 10 and 00 differ by one bit

Example 2:
Input: n = 1
Output: [0,1]

Constraints:
- 1 <= n <= 16
"""


class Solution:
    def grayCode(self, n: int) -> list[int]:
        result = [0]  # Start with 0

        for i in range(n):
            size = len(result)
            # Add numbers in reverse order with current bit set
            for j in range(size - 1, -1, -1):
                result.append(result[j] | (1 << i))

        return result


def test_gray_code():
    solution = Solution()

    def verify_sequence(seq: list[int], n: int) -> bool:
        """Verify if the sequence is a valid Gray code sequence"""
        # Check length
        if len(seq) != 2**n:
            return False

        # Check range and uniqueness
        seen = set(seq)
        if len(seen) != 2**n or any(x >= 2**n for x in seq):
            return False

        # Check adjacent numbers differ by one bit
        for i in range(len(seq)):
            curr = seq[i]
            next_num = seq[(i + 1) % len(seq)]
            if bin(curr ^ next_num).count('1') != 1:
                return False

        return True

    test_cases = [
        {
            "n": 1,
            "expected_length": 2,
            "description": "1-bit sequence"
        },
        {
            "n": 2,
            "expected_length": 4,
            "description": "2-bit sequence"
        },
        {
            "n": 3,
            "expected_length": 8,
            "description": "3-bit sequence"
        },
        {
            "n": 4,
            "expected_length": 16,
            "description": "4-bit sequence"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        n = test_case["n"]
        expected_length = test_case["expected_length"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        result = solution.grayCode(n)

        # Verify length
        assert len(result) == expected_length, \
            f"Expected length {expected_length}, but got {len(result)}"

        # Verify it's a valid Gray code sequence
        assert verify_sequence(result, n), \
            f"Invalid Gray code sequence: {result}"

        print(f"✓ Test case passed! Generated sequence: {result}")


if __name__ == "__main__":
    test_gray_code()
    print("\nAll test cases passed! 🎉")
