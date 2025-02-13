from typing import List


class Solution:
    """
    LeetCode 198 - House Robber

    Problem Statement:
    You are a professional robber planning to rob houses along a street. Each house has a certain amount
    of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses
    have security systems connected and it will automatically contact the police if two adjacent houses
    were broken into on the same night.

    Given an integer array nums representing the amount of money of each house, return the maximum amount
    of money you can rob tonight without alerting the police.
    """

    def rob(self, nums: List[int]) -> int:
        """
        Solution using Dynamic Programming

        Logic:
        - At each house i, we have two options:
          1. Rob this house and add it to the money from i-2 houses
          2. Skip this house and keep the money from i-1 houses
        - Take the maximum of these two options

        Time Complexity: O(n)
        Space Complexity: O(n)

        Args:
            nums: List of non-negative integers representing money in each house
        Returns:
            Maximum amount that can be robbed
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]

    def rob_space_optimized(self, nums: List[int]) -> int:
        """
        Space-optimized solution using only two variables

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev2, prev1 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            current = max(prev1, nums[i] + prev2)
            prev2, prev1 = prev1, current

        return prev1


def run_tests():
    """Test driver for House Robber solutions"""
    solution = Solution()

    test_cases = [
        {
            'nums': [1, 2, 3, 1],
            'expected': 4,
            'explanation': "Rob house 1 (money = 1) and then rob house 3 (money = 3)."
        },
        {
            'nums': [2, 7, 9, 3, 1],
            'expected': 12,
            'explanation': "Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1)."
        },
        {
            'nums': [2, 1, 1, 2],
            'expected': 4,
            'explanation': "Rob house 1 (money = 2) and then rob house 4 (money = 2)."
        },
        {
            'nums': [],
            'expected': 0,
            'explanation': "Empty house list returns 0."
        }
    ]

    # Test both implementations
    methods = [
        ('Standard DP', solution.rob),
        ('Space Optimized', solution.rob_space_optimized)
    ]

    for method_name, method in methods:
        print(f"\nTesting {method_name} solution:")
        print("-" * 50)

        for i, test in enumerate(test_cases, 1):
            result = method(test['nums'])
            passed = result == test['expected']
            print(f"Test {i}:")
            print(f"Input: {test['nums']}")
            print(f"Expected: {test['expected']}")
            print(f"Got: {result}")
            print(f"Explanation: {test['explanation']}")
            print(f"Result: {'✓ PASS' if passed else '✗ FAIL'}\n")


if __name__ == "__main__":
    run_tests()
