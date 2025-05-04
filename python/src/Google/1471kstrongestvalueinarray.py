"""
LeetCode 1471. The k Strongest Values in an Array

Problem Statement:
Given an array of integers arr and an integer k. A value arr[i] is said to be stronger than a value arr[j] if:
|arr[i] - m| > |arr[j] - m| where m is the median of the array.
If |arr[i] - m| == |arr[j] - m|, then arr[i] > arr[j].
Return a list of the strongest k values in the array in descending order.

Time Complexity: O(nlogn) due to sorting
Space Complexity: O(n) for storing sorted array
"""

from typing import List

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        # Logic:
        # 1. Sort array to find median
        # 2. Median is at (n-1)//2 index in sorted array
        # 3. Sort again based on:
        #    - Primary key: absolute difference from median (descending)
        #    - Secondary key: actual value (descending)
        # 4. Return first k elements
        
        arr.sort()
        median = arr[(len(arr) - 1) // 2]
        arr.sort(key=lambda x: (abs(x - median), x), reverse=True)
        return arr[:k]


# Test driver
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,2,3,4,5], 2),              # Expected: [5,1]
        ([1,1,3,5,5], 2),              # Expected: [5,5]
        ([6,7,11,7,6,8,7], 5),         # Expected: [11,8,7,7,7]
        ([10,6,9,1,4,8,2,3,7,5], 3),   # Expected: [10,9,8]
    ]
    
    for i, (arr, k) in enumerate(test_cases):
        result = solution.getStrongest(arr, k)
        print(f"Test case {i + 1}:")
        print(f"Input array: {arr}")
        print(f"k: {k}")
        print(f"Median: {sorted(arr)[(len(arr)-1)//2]}")
        print(f"k strongest values: {result}")
        print()
