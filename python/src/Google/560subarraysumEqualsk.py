from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = defaultdict(int)
        # To handle the case when subarray starts from index 0
        prefix_sums[0] = 1

        for num in nums:
            current_sum += num
            # Check if there is a prefix sum that we can subtract to get k
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            # Add the current prefix sum to the map
            prefix_sums[current_sum] += 1

        return count


print(Solution().subarraySum([1, 1, 1], 2))
print(Solution().subarraySum([1, 2, 3], 3))
