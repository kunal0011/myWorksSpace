"""
LeetCode 152. Maximum Product Subarray

Problem Statement:
Given an integer array nums, find a subarray that has the largest product,
and return the product.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Time complexity: O(n)
        Space complexity: O(1)

        The key insight is to keep track of both max and min products ending at current position,
        because a negative number can change the max to min and vice versa.
        """
        if not nums:
            return 0

        max_so_far = min_so_far = result = nums[0]

        for num in nums[1:]:
            candidates = (num, max_so_far * num, min_so_far * num)
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            result = max(result, max_so_far)

        return result


def test_max_product():
    """Test function with various test cases."""
    solution = Solution()

    test_cases = [
        {
            "nums": [2, 3, -2, 4],
            "expected": 6,
            "description": "Basic case with negative number"
        },
        {
            "nums": [-2, 0, -1],
            "expected": 0,
            "description": "Array with zero"
        },
        {
            "nums": [-2, 3, -4],
            "expected": 24,
            "description": "All negative numbers multiply to positive"
        },
        {
            "nums": [0, 2],
            "expected": 2,
            "description": "Array with leading zero"
        },
        {
            "nums": [-2],
            "expected": -2,
            "description": "Single negative number"
        },
        {
            "nums": [-2, -3, -4],
            "expected": 12,
            "description": "All negative numbers"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        result = solution.maxProduct(test_case["nums"])
        assert result == test_case["expected"], \
            f'Test case {i} failed. Expected {test_case["expected"]}, got {result}'
        print(f'Test case {i} passed: {test_case["description"]}')

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_max_product()
