from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum_count = {}
        # For the case when the initial sum is equal to goal
        prefix_sum_count[0] = 1
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num
            required_prefix_sum = current_sum - goal

            if required_prefix_sum in prefix_sum_count:
                count += prefix_sum_count[required_prefix_sum]

            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1

        return count


# Example usage:
sol = Solution()
nums = [1, 0, 1, 0, 1]
goal = 2
print(sol.numSubarraysWithSum(nums, goal))  # Output: 4
