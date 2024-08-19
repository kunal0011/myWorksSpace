from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        count = 0

        if k == 0:
            # For k = 0, we need to count elements that appear more than once
            for num in num_count:
                if num_count[num] > 1:
                    count += 1
        else:
            # For k > 0, we need to find if num + k exists in the map
            for num in num_count:
                if num + k in num_count:
                    count += 1

        return count
