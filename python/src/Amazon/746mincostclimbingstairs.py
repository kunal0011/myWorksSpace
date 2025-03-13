"""
LeetCode 746: Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Constraints:
- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999
"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Optimized solution using constant space
        Time complexity: O(n)
        Space complexity: O(1)
        """
        # Initialize two variables to keep track of minimum costs
        one_step = two_steps = 0
        
        # Iterate through the array backwards
        for i in range(len(cost) - 1, -1, -1):
            # Current minimum cost is cost at current step plus min of previous calculations
            current = cost[i] + min(one_step, two_steps)
            
            # Update the pointers
            two_steps = one_step
            one_step = current
            
        # Return minimum between starting from first or second step
        return min(one_step, two_steps)
    
    def minCostClimbingStairs_dp(self, cost: List[int]) -> int:
        """
        Alternative solution using dynamic programming array
        Time complexity: O(n)
        Space complexity: O(n)
        """
        n = len(cost)
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            
        return dp[n]


def test_min_cost_climbing_stairs():
    """Test function for Min Cost Climbing Stairs solutions"""
    test_cases = [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ([0, 0, 0, 0], 0),
        ([1, 2], 1),
        ([10, 15], 10),
        ([841,462,566,398,243,248,238,650,989,576], 2937),
    ]
    
    solution = Solution()
    
    for i, (cost, expected) in enumerate(test_cases, 1):
        # Test optimized solution
        result1 = solution.minCostClimbingStairs(cost)
        # Test DP solution
        result2 = solution.minCostClimbingStairs_dp(cost)
        
        print(f"\nTest case {i}:")
        print(f"Input: cost={cost}")
        print(f"Expected: {expected}")
        print(f"Optimized: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"DP Array: {result2} {'✓' if result2 == expected else '✗'}")


if __name__ == "__main__":
    test_min_cost_climbing_stairs()
