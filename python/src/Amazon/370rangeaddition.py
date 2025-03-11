"""
LeetCode 370 - Range Addition

Problem Statement:
You are given an integer length and an array updates where updates[i] = [startIdxi, endIdxi, inci].
You have an array arr of length length with all zeros, and you will update the array according to the updates array.
For each update operation, you should increment all the elements arr[startIdxi..endIdxi] (inclusive) by inci.
Return the resulting array after applying all the updates.

Time Complexity: O(n + k) where n is length of array and k is number of updates
Space Complexity: O(1) additional space (not counting output array)

Logic Explanation:
1. Instead of updating each element in the range, we use a prefix sum approach:
   - Add inc at start index
   - Subtract inc at end+1 index (to stop the effect)
2. Finally take cumulative sum to get the final values
This is similar to "difference array" technique.
"""

from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Step 1: Initialize the result array with zeros
        result = [0] * length
        
        # Step 2: Apply each update operation efficiently using difference array technique
        for start, end, inc in updates:
            result[start] += inc
            if end + 1 < length:
                result[end + 1] -= inc
        
        # Step 3: Compute the cumulative sum to get the final result
        for i in range(1, length):
            result[i] += result[i - 1]
            
        return result


def test_range_addition():
    """
    Test driver for the Range Addition solution
    """
    solution = Solution()
    
    # Test Case 1: Basic case
    length1 = 5
    updates1 = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    result1 = solution.getModifiedArray(length1, updates1)
    print(f"Test Case 1:")
    print(f"Length: {length1}")
    print(f"Updates: {updates1}")
    print(f"Result: {result1}")  # Expected: [-2, 0, 3, 5, 3]
    
    # Test Case 2: Single update
    length2 = 3
    updates2 = [[0, 2, 1]]
    result2 = solution.getModifiedArray(length2, updates2)
    print(f"\nTest Case 2:")
    print(f"Length: {length2}")
    print(f"Updates: {updates2}")
    print(f"Result: {result2}")  # Expected: [1, 1, 1]
    
    # Test Case 3: Empty updates
    length3 = 3
    updates3 = []
    result3 = solution.getModifiedArray(length3, updates3)
    print(f"\nTest Case 3:")
    print(f"Length: {length3}")
    print(f"Updates: {updates3}")
    print(f"Result: {result3}")  # Expected: [0, 0, 0]


if __name__ == "__main__":
    test_range_addition()
