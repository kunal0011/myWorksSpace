"""
LeetCode 703: Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. 
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with k and the initial array.
- int add(int val) Appends val to the stream and returns the kth largest element.

Constraints:
- 1 <= k <= 10^4
- 0 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- -10^4 <= val <= 10^4
- At most 10^4 calls will be made to add
- It's guaranteed that there will be at least k elements in the array when you search for the kth element
"""

import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        # Initialize heap with first k largest elements
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # Add new value to heap
        heapq.heappush(self.heap, val)
        # Remove smaller elements if heap size exceeds k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # Return kth largest (top of min-heap)
        return self.heap[0]

def test_kth_largest():
    """Test driver for KthLargest class"""
    test_cases = [
        {
            'k': 3,
            'nums': [4, 5, 8, 2],
            'operations': [3, 5, 10, 9, 4],
            'expected': [4, 5, 5, 8, 8]
        },
        {
            'k': 1,
            'nums': [],
            'operations': [1, -1, -2, -4, 3],
            'expected': [1, 1, 1, 1, 3]
        }
    ]

    for i, case in enumerate(test_cases, 1):
        print(f"\nTest case {i}:")
        print(f"k = {case['k']}, nums = {case['nums']}")
        
        kth_largest = KthLargest(case['k'], case['nums'])
        results = []
        
        for val, expected in zip(case['operations'], case['expected']):
            result = kth_largest.add(val)
            results.append(result)
            print(f"Adding {val}, expected {expected}, got {result}")
            assert result == expected, f"Failed: Expected {expected}, got {result}"
        
        print(f"✓ All operations passed for test case {i}")

if __name__ == "__main__":
    test_kth_largest()
