class Solution:
    def deleteAndEarn(self, nums):
        if not nums:
            return 0

        # Determine the range of numbers in nums
        max_num = max(nums)
        points = [0] * (max_num + 1)

        # Calculate the total points for each number
        for num in nums:
            points[num] += num

        # Use dynamic programming to find the maximum points
        dp = [0] * (max_num + 1)
        dp[1] = points[1]

        for i in range(2, max_num + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + points[i])

        return dp[max_num]


# Example usage
solution = Solution()
print(solution.deleteAndEarn([3, 4, 2]))       # Output: 6
print(solution.deleteAndEarn([2, 2, 3, 3, 3, 4]))  # Output: 9
