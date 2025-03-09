"""
LeetCode 268 - Missing Number

Problem Statement:
Given an array nums containing n distinct numbers in the range [0, n], return the only number 
in the range that is missing from the array.

Solution Logic:
1. Use XOR approach:
   - XOR all numbers from 0 to n
   - XOR with all numbers in array
   - Missing number is the result
2. Properties used:
   - a ^ a = 0
   - a ^ 0 = a
   - XOR is associative and commutative
3. Time: O(n), Space: O(1)
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)  # Start with n, since the index stops at n-1
        for i in range(len(nums)):
            # XOR the index and the value at that index
            missing ^= i ^ nums[i]
        return missing

def test_missing_number():
    solution = Solution()
    
    # Test Case 1: Missing middle number
    nums1 = [3,0,1]
    print("Test 1: Missing middle number")
    print(f"Array: {nums1}")
    print(f"Missing number: {solution.missingNumber(nums1)}")  # Expected: 2
    
    # Test Case 2: Missing last number
    nums2 = [0,1,2]
    print("\nTest 2: Missing last number")
    print(f"Array: {nums2}")
    print(f"Missing number: {solution.missingNumber(nums2)}")  # Expected: 3
    
    # Test Case 3: Missing first number
    nums3 = [1,2,3]
    print("\nTest 3: Missing first number")
    print(f"Array: {nums3}")
    print(f"Missing number: {solution.missingNumber(nums3)}")  # Expected: 0
    
    # Test Case 4: Single element
    nums4 = [0]
    print("\nTest 4: Single element")
    print(f"Array: {nums4}")
    print(f"Missing number: {solution.missingNumber(nums4)}")  # Expected: 1

if __name__ == "__main__":
    test_missing_number()
