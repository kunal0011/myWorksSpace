class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        # Create a dp array to store the minimum cost to reach each step
        n = len(cost)
        # We need n+1 size because we need to "reach" beyond the last step
        dp = [0] * (n + 1)

        # Base case: no cost to start at step 0 or step 1
        dp[0] = 0
        dp[1] = 0

        # Fill the dp array
        for i in range(2, n + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        # The answer is the cost to reach step n (the top, beyond the last step)
        return dp[n]


# Test the Solution
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    cost = [10, 15, 20]
    # Output: 15
    print(
        f"Minimum cost to reach the top: {solution.minCostClimbingStairs(cost)}")

    # Test case 2
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    # Output: 6
    print(
        f"Minimum cost to reach the top: {solution.minCostClimbingStairs(cost)}")
