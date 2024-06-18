from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [float('inf') for i in range(n)]

        dp[0] = 0

        for i in range(1, n):
            for j in range(i):
                if nums[j] >= i-j:
                    dp[i] = min(dp[i], dp[j]+1)

        return dp[n-1]


class Solution1:
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


if __name__ == '__main__':
    s = Solution1()
    print(s.jump([2, 3, 1, 1, 4]))
    print(s.jump([2, 3, 0, 1, 4]))
