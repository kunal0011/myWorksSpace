from typing import List


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # Use a dictionary to map each stone to a set of jump lengths that can reach it.
        dp = {stone: set() for stone in stones}
        dp[stones[0]].add(0)

        for stone in stones:
            for k in dp[stone]:
                # Try to jump k-1, k, and k+1 units from the current stone
                for step in [k-1, k, k+1]:
                    if step > 0 and stone + step in dp:
                        dp[stone + step].add(step)

        # If the last stone's set has any jump lengths, the frog can reach it.
        return bool(dp[stones[-1]])
