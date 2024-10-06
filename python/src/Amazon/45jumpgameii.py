from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):  # We don't need to jump from the last index
            farthest = max(farthest, i + nums[i])

            # If we have reached the end of the range for the current jump
            if i == current_end:
                jumps += 1
                current_end = farthest

                # If we can reach or exceed the last index, break early
                if current_end >= n - 1:
                    break

        return jumps
