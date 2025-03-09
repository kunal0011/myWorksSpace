"""
LeetCode 347: Top K Frequent Elements

Problem Statement:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Explanation: The two most frequent elements are 1 (frequency=3) and 2 (frequency=2)

Example 2:
Input: nums = [1], k = 1
Output: [1]

Logic:
1. Use Counter to count frequency of each element
2. Use a min-heap to maintain k most frequent elements
   - Python's heapq is min-heap, so we store (-frequency, num) pairs
   - Keep heap size <= k by popping smallest elements
3. Final heap contains k most frequent elements
4. Time Complexity: O(n log k) where n is length of nums
5. Space Complexity: O(n) for the counter
"""

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


def run_test_cases():
    solution = Solution()
    
    # Test case 1: Example from problem statement
    nums1 = [1,1,1,2,2,3]
    k1 = 2
    result1 = solution.topKFrequent(nums1, k1)
    print("Test case 1:")
    print(f"Input: nums = {nums1}, k = {k1}")
    print(f"Expected: [1,2] (in any order)")
    print(f"Got: {result1}")
    print(f"Pass? {sorted(result1) == sorted([1,2])}\n")
    
    # Test case 2: Single element
    nums2 = [1]
    k2 = 1
    result2 = solution.topKFrequent(nums2, k2)
    print("Test case 2:")
    print(f"Input: nums = {nums2}, k = {k2}")
    print(f"Expected: [1]")
    print(f"Got: {result2}")
    print(f"Pass? {result2 == [1]}\n")
    
    # Test case 3: All elements have same frequency
    nums3 = [1,2,3,4]
    k3 = 2
    result3 = solution.topKFrequent(nums3, k3)
    print("Test case 3:")
    print(f"Input: nums = {nums3}, k = {k3}")
    print(f"Expected: Any 2 numbers from [1,2,3,4]")
    print(f"Got: {result3}")
    print(f"Pass? {len(result3) == 2 and all(x in [1,2,3,4] for x in result3)}\n")
    
    # Test case 4: k equals array length
    nums4 = [1,1,2,2,3,3]
    k4 = 3
    result4 = solution.topKFrequent(nums4, k4)
    print("Test case 4:")
    print(f"Input: nums = {nums4}, k = {k4}")
    print(f"Expected: [1,2,3] (in any order)")
    print(f"Got: {result4}")
    print(f"Pass? {sorted(result4) == sorted([1,2,3])}\n")
    
    # Test case 5: Multiple elements with different frequencies
    nums5 = [5,5,5,2,2,3,1,1,1,1]
    k5 = 2
    result5 = solution.topKFrequent(nums5, k5)
    print("Test case 5:")
    print(f"Input: nums = {nums5}, k = {k5}")
    print(f"Expected: [1,5] (in any order)")
    print(f"Got: {result5}")
    print(f"Pass? {sorted(result5) == sorted([1,5])}")


if __name__ == "__main__":
    run_test_cases()
