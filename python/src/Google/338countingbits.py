"""
LeetCode 338 - Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0 (0 ones)
1 --> 1 (1 one)
2 --> 10 (1 one)

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0 (0 ones)
1 --> 1 (1 one)
2 --> 10 (1 one)
3 --> 11 (2 ones)
4 --> 100 (1 one)
5 --> 101 (2 ones)

Time Complexity: O(n)
Space Complexity: O(1) excluding the output array
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create an array to store the number of 1 bits for each number from 0 to n
        ans = [0] * (n + 1)

        # Iterate over each number from 1 to n
        for i in range(1, n + 1):
            # The number of 1 bits in i is 1 plus the number of 1 bits in i // 2
            ans[i] = ans[i >> 1] + (i & 1)

        return ans


def test_counting_bits():
    # Test cases
    test_cases = [2, 5, 0, 1, 10]
    expected_outputs = [
        [0, 1, 1],
        [0, 1, 1, 2, 1, 2],
        [0],
        [0, 1],
        [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2],
    ]

    solution = Solution()
    for i, (test_input, expected) in enumerate(zip(test_cases, expected_outputs)):
        result = solution.countBits(test_input)
        print(f"Test case {i + 1}:")
        print(f"Input: n = {test_input}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}\n")


if __name__ == "__main__":
    test_counting_bits()
