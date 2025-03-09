"""
LeetCode 239 - Sliding Window Maximum

Problem Statement:
Given an array nums and a sliding window of size k moving from the left to the right,
return the maximum element in each window. The sliding window moves right by one position.

Solution Logic:
1. Use a deque to maintain window elements efficiently
2. For each element:
   - Remove elements outside current window
   - Remove smaller elements from back (they can't be max)
   - Add current element
   - After k elements, front of deque is current window max
3. Time: O(n), Space: O(k)
   Each element is pushed and popped at most once
"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        result = []
        dq = deque()  # Will store indices of the elements

        for i in range(len(nums)):
            # Remove elements out of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove elements smaller than the current element from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current element index to the deque
            dq.append(i)

            # Append the current max (from the front of the deque) to the result
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

def test_sliding_window():
    solution = Solution()
    
    # Test Case 1: Regular case
    nums1 = [1,3,-1,-3,5,3,6,7]
    k1 = 3
    print("Test 1: Regular case")
    print(f"Array: {nums1}, k: {k1}")
    print(f"Result: {solution.maxSlidingWindow(nums1, k1)}")  
    # Expected: [3,3,5,5,6,7]
    
    # Test Case 2: Window size 1
    nums2 = [1,-1]
    k2 = 1
    print("\nTest 2: Window size 1")
    print(f"Array: {nums2}, k: {k2}")
    print(f"Result: {solution.maxSlidingWindow(nums2, k2)}")  
    # Expected: [1,-1]
    
    # Test Case 3: Window size equals array length
    nums3 = [1,2,3,4]
    k3 = 4
    print("\nTest 3: Window size equals array length")
    print(f"Array: {nums3}, k: {k3}")
    print(f"Result: {solution.maxSlidingWindow(nums3, k3)}")  
    # Expected: [4]
    
    # Test Case 4: Empty array
    nums4 = []
    k4 = 0
    print("\nTest 4: Empty array")
    print(f"Array: {nums4}, k: {k4}")
    print(f"Result: {solution.maxSlidingWindow(nums4, k4)}")  
    # Expected: []

if __name__ == "__main__":
    test_sliding_window()
