class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        # Create a DP table
        dp = [[0] * n for _ in range(n)]

        # Base case: single element subarrays
        for i in range(n):
            dp[i][i] = nums[i]

        # Fill DP table for subarrays longer than 1
        for length in range(2, n + 1):  # length of the subarray
            for i in range(n - length + 1):
                j = i + length - 1
                # The score difference for subarray nums[i:j+1]
                pick_left = nums[i] - dp[i + 1][j]
                pick_right = nums[j] - dp[i][j - 1]
                dp[i][j] = max(pick_left, pick_right)

        # Player 1 wins if the difference is non-negative
        return dp[0][n - 1] >= 0
