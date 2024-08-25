from collections import Counter
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Step 1: Count the frequency of each element
        frequency = Counter(nums)

        # Step 2: Sort the array based on the frequency and value
        # Primary sort by frequency (increasing)
        # Secondary sort by value (decreasing)
        nums.sort(key=lambda x: (frequency[x], -x))

        return nums
