from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        # This line will never be reached because the problem guarantees exactly one solution.
        return []

# Example usage:
# sol = Solution()
# print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
# print(sol.twoSum([2, 3, 4], 6))       # Output: [1, 3]
# print(sol.twoSum([-1, 0], -1))        # Output: [1, 2]
