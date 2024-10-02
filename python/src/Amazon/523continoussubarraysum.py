class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # Dictionary to store the remainder of cumulative sum and the index at which it occurred
        # Initialize with remainder 0 at index -1 for the edge case
        remainder_map = {0: -1}

        cumulative_sum = 0

        for i in range(len(nums)):
            cumulative_sum += nums[i]
            if k != 0:
                cumulative_sum %= k  # Get the remainder when cumulative_sum is divided by k

            if cumulative_sum in remainder_map:
                # Subarray must be at least size 2
                if i - remainder_map[cumulative_sum] > 1:
                    return True
            else:
                remainder_map[cumulative_sum] = i

        return False
