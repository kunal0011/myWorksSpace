"""
LeetCode 312 - Burst Balloons

Problem Statement:
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it.
You are asked to burst all the balloons. If you burst balloon i you will get 
nums[i-1] * nums[i] * nums[i+1] coins. After bursting balloon i, balloons i-1 and i+1
become adjacent. Find the maximum coins you can collect.
Note: If i-1 or i+1 goes out of bounds, treat it as if there is a balloon with value 1.

Logic:
1. Use Dynamic Programming with divide and conquer:
   - dp[left][right]: max coins from bursting balloons between left and right
   - Add virtual balloons with value 1 at start and end
2. For each subarray length:
   - Try each position as the last balloon to burst
   - Calculate coins = nums[left] * nums[i] * nums[right]
   - Add recursive solutions for left and right subarrays
3. Time: O(n^3), Space: O(n^2)
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(n - length):
                right = left + length
                for i in range(left + 1, right):
                    dp[left][right] = max(
                        dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

        return dp[0][-1]


def test_max_coins():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([3,1,5,8], 167),           # Standard case
        ([1,5], 10),                # Two balloons
        ([7], 7),                   # Single balloon
        ([], 0),                    # Empty array
        ([1,1,1,1], 4),            # All same values
        ([9,76,64,21], 116672)      # Larger values
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.maxCoins(nums)
        assert result == expected, f"Test case {i + 1} failed: nums={nums}, expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: nums={nums}, max coins={result}")
        print(f"Explanation for test case {i + 1}:")
        if nums == [3,1,5,8]:
            print("  Optimal sequence: 1,5,3,8 -> 3×1×5 + 3×5×8 + 1×3×8 + 1×8×1 = 167")
        print()

if __name__ == "__main__":
    test_max_coins()
    print("All test cases passed!")
