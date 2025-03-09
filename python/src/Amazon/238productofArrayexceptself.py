"""
LeetCode 238 - Product of Array Except Self

Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to the product
of all the elements of nums except nums[i]. The algorithm must run in O(n) time and without using
the division operation.

Solution Logic:
1. Use two passes through the array:
   - First pass: Build prefix products from left to right
   - Second pass: Build suffix products from right to left
2. For each position i, result is:
   - product of all elements to the left * product of all elements to the right
3. Time: O(n), Space: O(1) excluding output array
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # First pass: Build prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
            
        # Second pass: Build suffix products
        suffix = 1
        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer

def test_product_except_self():
    solution = Solution()
    
    # Test Case 1: Basic case
    nums1 = [1,2,3,4]
    print("Test 1: Basic case")
    print(f"Input: {nums1}")
    print(f"Output: {solution.productExceptSelf(nums1)}")  # Expected: [24,12,8,6]
    
    # Test Case 2: Array with zeros
    nums2 = [0,1,2,3]
    print("\nTest 2: Array with zero")
    print(f"Input: {nums2}")
    print(f"Output: {solution.productExceptSelf(nums2)}")  # Expected: [6,0,0,0]
    
    # Test Case 3: Two elements
    nums3 = [1,2]
    print("\nTest 3: Two elements")
    print(f"Input: {nums3}")
    print(f"Output: {solution.productExceptSelf(nums3)}")  # Expected: [2,1]
    
    # Test Case 4: Array with multiple zeros
    nums4 = [0,0,2,3]
    print("\nTest 4: Multiple zeros")
    print(f"Input: {nums4}")
    print(f"Output: {solution.productExceptSelf(nums4)}")  # Expected: [0,0,0,0]

if __name__ == "__main__":
    test_product_except_self()
