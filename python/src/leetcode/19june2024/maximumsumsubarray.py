from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0

        max_current = max_global = nums[0]

        for num in nums[1:]:
            max_current = max(num, max_current + num)
            if max_current > max_global:
                max_global = max_current

        return max_global


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
