from typing import List

"""
LeetCode 2057: Smallest Index With Equal Value
Problem: Find the smallest index i where i mod 10 equals nums[i]
Logic: Linear scan through array checking modulo condition
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1

# Test driver


def test_solution():
    sol = Solution()
    test_cases = [
        [0, 1, 2],
        [4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    ]

    for nums in test_cases:
        print(f"\nTest Case:")
        print(f"Input: nums = {nums}")
        print(f"Output: {sol.smallestEqual(nums)}")


if __name__ == "__main__":
    test_solution()
