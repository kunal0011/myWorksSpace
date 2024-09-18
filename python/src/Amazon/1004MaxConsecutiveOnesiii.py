from typing import List


class Solution:
    def longestOnes(self, nums: List[int], K: int) -> int:
        left = 0
        max_length = 0
        zero_count = 0

        for right in range(len(nums)):
            # If we encounter a 0, increase the zero count
            if nums[right] == 0:
                zero_count += 1

            # If zero count exceeds K, move the left pointer to reduce zeros
            while zero_count > K:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # Calculate the length of the current window
            max_length = max(max_length, right - left + 1)

        return max_length


# Testing
solution = Solution()
nums = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1]
K = 2
print("Python Test Result:", solution.longestOnes(nums, K))  # Output: 6
