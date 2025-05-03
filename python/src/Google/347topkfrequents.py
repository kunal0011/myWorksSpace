"""
LeetCode 347 - Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Time Complexity: O(n log k) where n is the length of nums
Space Complexity: O(n) for storing the frequency counter
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


def test_top_k_frequent():
    # Test cases
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1),
        ([1, 2, 2, 3, 3, 3], 2),
        ([4, 1, -1, 2, -1, 2, 3], 2),
        ([1, 1, 1, 2, 2, 2, 3, 3, 3], 3),
    ]

    expected_outputs = [
        [1, 2],
        [1],
        [2, 3],
        [2, -1],
        [1, 2, 3],
    ]

    solution = Solution()
    for i, ((nums, k), expected) in enumerate(zip(test_cases, expected_outputs)):
        result = solution.topKFrequent(nums, k)
        print(f"Test case {i + 1}:")
        print(f"Input: nums = {nums}, k = {k}")
        print(f"Expected: {sorted(expected)}")
        print(f"Got: {sorted(result)}")
        print(f"{'✓ Passed' if sorted(result) == sorted(expected) else '✗ Failed'}\n")


if __name__ == "__main__":
    test_top_k_frequent()
