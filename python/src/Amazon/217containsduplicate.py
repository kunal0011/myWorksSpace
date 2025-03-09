"""
LeetCode 217 - Contains Duplicate

Problem Statement:
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Solution Logic:
1. Use HashSet to track seen numbers
2. Iterate through array once
3. If number already in set, return True
4. If complete iteration without finding duplicate, return False
5. Time: O(n), Space: O(n)
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

def test_contains_duplicate():
    solution = Solution()
    
    # Test Case 1: Has duplicates
    nums1 = [1,2,3,1]
    print("Test 1:")
    print(f"Input: {nums1}")
    print(f"Output: {solution.containsDuplicate(nums1)}")  # Expected: True
    
    # Test Case 2: No duplicates
    nums2 = [1,2,3,4]
    print("\nTest 2:")
    print(f"Input: {nums2}")
    print(f"Output: {solution.containsDuplicate(nums2)}")  # Expected: False
    
    # Test Case 3: Multiple duplicates
    nums3 = [1,1,1,3,3,4,3,2,4,2]
    print("\nTest 3:")
    print(f"Input: {nums3}")
    print(f"Output: {solution.containsDuplicate(nums3)}")  # Expected: True

if __name__ == "__main__":
    test_contains_duplicate()
