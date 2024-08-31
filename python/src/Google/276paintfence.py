class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k

        # There are two cases for each post:
        # 1. The current post has the same color as the previous one.
        # 2. The current post has a different color from the previous one.

        same = k  # Ways to paint the first two posts with the same color
        # Ways to paint the first two posts with different colors
        diff = k * (k - 1)

        for i in range(3, n + 1):
            # If we paint the current post with the same color as the previous post,
            # it means the previous two posts must have different colors.
            same, diff = diff, (same + diff) * (k - 1)

        # The total number of ways to paint n posts is the sum of the two possibilities.
        return same + diff
