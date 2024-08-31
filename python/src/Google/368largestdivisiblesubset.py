from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Sort the array
        nums.sort()

        n = len(nums)
        dp = [1] * n
        parent = [-1] * n

        # Fill the dp and parent arrays
        max_len = 0
        max_index = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            # Update max_len and max_index
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        # Reconstruct the largest divisible subset
        subset = []
        while max_index >= 0:
            subset.append(nums[max_index])
            max_index = parent[max_index]

        return subset[::-1]  # Reverse to return the subset in ascending order
