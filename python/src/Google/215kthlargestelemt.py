import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        # Process the rest of the elements
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        # The root of the heap is the kth largest element
        return heap[0]
