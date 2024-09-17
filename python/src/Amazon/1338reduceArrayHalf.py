from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Step 1: Count the frequency of each element
        freq = Counter(arr)

        # Step 2: Sort the frequencies in descending order
        freq_values = sorted(freq.values(), reverse=True)

        # Step 3: Remove elements by frequency until at least half are removed
        half_size = len(arr) // 2
        removed = 0
        set_size = 0

        for count in freq_values:
            removed += count
            set_size += 1
            if removed >= half_size:
                break

        return set_size


# Testing
solution = Solution()
arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
print("Python Test Result:", solution.minSetSize(arr))  # Output: 2
