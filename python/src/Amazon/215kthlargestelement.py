import heapq
import random
from typing import List

"""
LeetCode 215 - Kth Largest Element in an Array

Problem Statement:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Solution Logic:
1. Min-Heap Approach (Current implementation):
   - Maintain min-heap of size k
   - First k elements form initial heap
   - For remaining elements, if larger than heap top, replace top
   - Time: O(N log k), Space: O(k)

2. Alternative QuickSelect Approach (commented below):
   - Similar to QuickSort but only process required partition
   - Average Time: O(N), Worst: O(N²), Space: O(1)
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Use QuickSelect implementation (more efficient on average)
        return self.quickSelect(nums, 0, len(nums) - 1, len(nums) - k)
    
    def quickSelect(self, nums: List[int], left: int, right: int, k: int) -> int:
        # If the list contains only one element, return that element
        if left == right:
            return nums[left]
        
        # Select a random pivot
        pivot_idx = random.randint(left, right)
        pivot_idx = self.partition(nums, left, right, pivot_idx)
        
        if k == pivot_idx:
            return nums[k]
        elif k < pivot_idx:
            return self.quickSelect(nums, left, pivot_idx - 1, k)
        else:
            return self.quickSelect(nums, pivot_idx + 1, right, k)
    
    def partition(self, nums: List[int], left: int, right: int, pivot_idx: int) -> int:
        pivot = nums[pivot_idx]
        # Move pivot to end
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        
        # Move smaller elements to the left
        store_idx = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_idx], nums[i] = nums[i], nums[store_idx]
                store_idx += 1
        
        # Move pivot to its final place
        nums[right], nums[store_idx] = nums[store_idx], nums[right]
        
        return store_idx

    # Heap-based solution (original implementation)
    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        # Process the rest of the elements
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        # The root of the heap is the kth largest element
        return heap[0]

def test_kth_largest():
    solution = Solution()
    
    # Test both implementations
    def test_case(nums, k):
        heap_result = solution.findKthLargestHeap(nums.copy(), k)
        quick_result = solution.findKthLargest(nums.copy(), k)
        print(f"Array: {nums}, k: {k}")
        print(f"Heap result: {heap_result}")
        print(f"QuickSelect result: {quick_result}")
        assert heap_result == quick_result
    
    # Test cases
    print("Test 1:")
    test_case([3,2,1,5,6,4], 2)  # Expected: 5
    
    print("\nTest 2:")
    test_case([3,2,3,1,2,4,5,5,6], 4)  # Expected: 4
    
    print("\nTest 3:")
    test_case([1], 1)  # Expected: 1
    
    print("\nTest 4:")
    test_case([-1,-1,2,0], 2)  # Expected: 0

if __name__ == "__main__":
    test_kth_largest()
