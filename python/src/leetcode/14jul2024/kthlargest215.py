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


s = Solution()
# Example usage
nums = [3, 2, 1, 5, 6, 4]
k = 2
print(s.findKthLargest(nums, k))  # Output: 5

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(s.findKthLargest(nums, k))  # Output: 4
