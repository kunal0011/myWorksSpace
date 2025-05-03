"""
LeetCode 312 - Burst Balloons

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums.
You are asked to burst all the balloons. If you burst balloon i, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Handle empty input
        if not nums:
            return 0
            
        # Add 1s to the start and end of the nums array
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] represents the maximum coins that can be obtained
        # by bursting all balloons between index i and j (exclusive)
        dp = [[0] * n for _ in range(n)]
        
        # We start from smaller subproblems (shorter subarrays)
        # and build up to larger ones
        for gap in range(1, n-1):  # gap is the size of subarray - 1
            for i in range(0, n-gap-1):  # i is the start index
                j = i + gap + 1  # j is the end index
                for k in range(i+1, j):  # k is the last balloon to burst
                    # Calculate coins: left boundary * current balloon * right boundary
                    # Plus the maximum coins from left and right subarrays
                    current = nums[i] * nums[k] * nums[j]
                    current += dp[i][k] + dp[k][j]
                    dp[i][j] = max(dp[i][j], current)
        
        return dp[0][n-1]


def test_burst_balloons():
    solution = Solution()

    # Test cases
    test_cases = [
        ([3, 1, 5, 8], 167),
        ([1, 5], 10),
        ([7], 7),
        ([], 0),
        ([3, 1, 5, 8, 2], 432),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = solution.maxCoins(nums)
        assert result == expected, f"Test case {i + 1} failed: got {result}, expected {expected}"
        print(f"Test case {i + 1} passed! Input: {nums}, Output: {result}")


if __name__ == "__main__":
    test_burst_balloons()
