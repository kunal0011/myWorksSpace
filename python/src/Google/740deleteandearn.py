from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Step 1: Convert the list to a frequency map
        count = Counter(nums)
        max_num = max(nums)

        # Step 2: Initialize the dp array
        dp = [0] * (max_num + 1)

        # Step 3: Fill the dp array
        dp[1] = count[1] * 1
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)

        return dp[max_num]


# Example usage
solution = Solution()
nums1 = [3, 4, 2]
nums2 = [2, 2, 3, 3, 3, 4]

print(solution.deleteAndEarn(nums1))  # Output: 6
print(solution.deleteAndEarn(nums2))  # Output: 9
