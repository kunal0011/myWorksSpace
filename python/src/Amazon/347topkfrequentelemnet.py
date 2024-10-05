from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        count = Counter(nums)

        # Step 2: Use a heap to keep track of the top k frequent elements
        # Python's heapq module is a min-heap, so use it to maintain a heap of size k
        min_heap = []

        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 3: Extract the elements from the heap
        result = [num for freq, num in min_heap]

        return result
