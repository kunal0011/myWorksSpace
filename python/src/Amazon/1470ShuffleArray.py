from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Extract the two halves
        first_half = nums[:n]
        second_half = nums[n:]

        # Create the shuffled result
        result = []
        for i in range(n):
            result.append(first_half[i])
            result.append(second_half[i])

        return result


# Testing
solution = Solution()
nums = [2, 5, 1, 3, 4, 7]
n = 3
# Output should be [2, 3, 5, 4, 1, 7]
print("Python Test Result:", solution.shuffle(nums, n))
