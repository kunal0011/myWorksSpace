from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result array
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Use the relation countBits(i) = countBits(i // 2) + (i % 2)
            dp[i] = dp[i >> 1] + (i & 1)

        return dp
