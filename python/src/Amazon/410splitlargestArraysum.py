from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def can_split(max_sum):
            current_sum = 0
            required_parts = 1  # At least one part is needed

            for num in nums:
                if current_sum + num > max_sum:
                    required_parts += 1
                    current_sum = num
                    if required_parts > m:
                        return False
                else:
                    current_sum += num

            return True

        # Binary search setup
        low, high = max(nums), sum(nums)

        while low < high:
            mid = (low + high) // 2
            if can_split(mid):
                high = mid  # Try for a smaller maximum sum
            else:
                low = mid + 1  # Increase the maximum sum

        return low
