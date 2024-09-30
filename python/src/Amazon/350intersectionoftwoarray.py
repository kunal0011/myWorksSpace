from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a Counter (hashmap) to store the frequency of elements in nums1
        counts = Counter(nums1)
        intersection = []

        # Iterate through nums2 and collect elements that are also in nums1
        for num in nums2:
            if counts[num] > 0:  # If num is in nums1 and hasn't been fully used
                intersection.append(num)
                counts[num] -= 1  # Decrease the count since it's been used

        return intersection
