from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        # Step through the list in pairs of (frequency, value)
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]
            # Append `val` `freq` times
            result.extend([val] * freq)
        return result


# Testing
solution = Solution()
nums = [1, 2, 3, 4]
# Output: [2, 4, 4, 4]
print("Python Test Result:", solution.decompressRLElist(nums))
