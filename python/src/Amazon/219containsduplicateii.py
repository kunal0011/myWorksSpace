"""
LeetCode 219 - Contains Duplicate II

Problem Statement:
Given an integer array nums and an integer k, return true if there are two distinct indices 
i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Solution Logic:
1. Use HashMap to store last seen index of each number
2. For each number:
   - If number exists in map and current index - last index <= k, return True
   - Update map with current index
3. Time: O(n), Space: O(min(n,k))
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i, v in enumerate(nums):
            if v in mp and i - mp[v] <= k:
                return True
            mp[v] = i
        return False

def test_contains_nearby_duplicate():
    solution = Solution()
    
    # Test Case 1: Has nearby duplicates
    nums1 = [1,2,3,1]
    k1 = 3
    print("Test 1:")
    print(f"Input: nums={nums1}, k={k1}")
    print(f"Output: {solution.containsNearbyDuplicate(nums1, k1)}")  # Expected: True
    
    # Test Case 2: Duplicates too far
    nums2 = [1,0,1,1]
    k2 = 1
    print("\nTest 2:")
    print(f"Input: nums={nums2}, k={k2}")
    print(f"Output: {solution.containsNearbyDuplicate(nums2, k2)}")  # Expected: True
    
    # Test Case 3: No duplicates
    nums3 = [1,2,3,4]
    k3 = 1
    print("\nTest 3:")
    print(f"Input: nums={nums3}, k={k3}")
    print(f"Output: {solution.containsNearbyDuplicate(nums3, k3)}")  # Expected: False

if __name__ == "__main__":
    test_contains_nearby_duplicate()
