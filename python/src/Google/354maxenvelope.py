from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort envelopes by width ascending, and by height descending for ties
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Extract the heights
        heights = [h for _, h in envelopes]

        # Find the length of the longest increasing subsequence of heights
        def length_of_LIS(nums):
            dp = []
            for num in nums:
                pos = bisect_left(dp, num)
                if pos == len(dp):
                    dp.append(num)
                else:
                    dp[pos] = num
            return len(dp)

        return length_of_LIS(heights)


s = Solution()
print(s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
