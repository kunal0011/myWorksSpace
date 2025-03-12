"""
LeetCode 494 - Target Sum

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
- For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

Example:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
"""

from typing import List
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        # If (target + total_sum) is odd or target is larger than total_sum, no solution exists
        if (total_sum + target) % 2 != 0 or abs(target) > total_sum:
            return 0

        # Subset sum we are looking for
        subset_sum = (total_sum + target) // 2

        # DP array to count the number of ways to reach each sum
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # There's one way to make sum 0 (by choosing no elements)

        # Dynamic programming to fill dp array
        for num in nums:
            # Traverse backward to ensure that each number is only used once
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset_sum]

    def findTargetSumWays_memoization(self, nums: List[int], target: int) -> int:
        """Alternative solution using memoization for better space complexity in sparse cases"""
        memo = defaultdict(dict)
        
        def dfs(index: int, curr_sum: int) -> int:
            if index == len(nums):
                return 1 if curr_sum == target else 0
                
            if index in memo and curr_sum in memo[index]:
                return memo[index][curr_sum]
                
            pos = dfs(index + 1, curr_sum + nums[index])
            neg = dfs(index + 1, curr_sum - nums[index])
            memo[index][curr_sum] = pos + neg
            return memo[index][curr_sum]
            
        return dfs(0, 0)


def test_target_sum():
    """Test function to verify both solution approaches"""
    solution = Solution()
    
    test_cases = [
        ([1,1,1,1,1], 3, 5),
        ([1], 1, 1),
        ([1,0], 1, 2),
        ([0,0,0,0,0], 0, 32),
        ([100], -200, 0),
        ([1,2,3,4,5], 15, 0),
        ([], 0, 0)  # Edge case
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        # Test DP solution
        result_dp = solution.findTargetSumWays(nums, target)
        # Test memoization solution
        result_memo = solution.findTargetSumWays_memoization(nums, target)
        
        status_dp = "✓" if result_dp == expected else "✗"
        status_memo = "✓" if result_memo == expected else "✗"
        
        print(f"Test {i}:")
        print(f"Input: nums={nums}, target={target}")
        print(f"DP Solution: {status_dp} Got: {result_dp}")
        print(f"Memo Solution: {status_memo} Got: {result_memo}")
        print(f"Expected: {expected}\n")


if __name__ == "__main__":
    test_target_sum()
