"""
LeetCode 611 - Valid Triangle Number

Given an integer array nums, return the number of triplets chosen from the array that can make triangles 
if we take them as side lengths of a triangle.

Example 1:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid combinations are: 
- 2,2,3
- 2,3,4
- 2,2,4

Example 2:
Input: nums = [4,2,3,4]
Output: 4

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000
"""

from typing import List
from time import time


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Optimized solution for counting valid triangles.
        
        Logic:
        1. Sort the array in ascending order
        2. Fix two sides (i and j) and binary search for the third side
        3. For a triangle to be valid: sum of any two sides > third side
           - In sorted array, we only need to check: nums[i] + nums[j] > nums[k]
           - Other two conditions (nums[j] + nums[k] > nums[i] and nums[k] + nums[i] > nums[j])
             are automatically satisfied due to sorting
        
        Time Complexity: O(n^2 log n) where n is the length of nums
        Space Complexity: O(1) excluding the space used for sorting
        """
        if not nums:
            return 0
            
        n = len(nums)
        nums.sort()  # Sort in ascending order
        count = 0
        
        # Fix the largest side and find pairs of smaller sides
        for k in range(n-1, 1, -1):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    # All values between i and j can form triangles with nums[k]
                    count += j - i
                    j -= 1
                else:
                    i += 1
                    
        return count
    
    def triangleNumber_bruteforce(self, nums: List[int]) -> int:
        """
        Brute force solution for validation (not recommended for large inputs)
        Time Complexity: O(n^3)
        Space Complexity: O(1)
        """
        n = len(nums)
        count = 0
        
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if (nums[i] + nums[j] > nums[k] and 
                        nums[j] + nums[k] > nums[i] and 
                        nums[k] + nums[i] > nums[j]):
                        count += 1
                        
        return count


def test_triangle_number():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([2,2,3,4], 3),
        ([4,2,3,4], 4),
        
        # Edge cases
        ([1], 0),
        ([1,2], 0),
        ([0,0,0], 0),
        
        # Test cases with duplicates
        ([2,2,2,2], 4),
        ([1,1,1,1,1], 10),
        
        # Test cases with various lengths
        ([3,4,5,6], 3),
        ([1,2,3,4,5,6], 7),
        
        # Test case with zeros
        ([0,1,2,3], 0),
        
        # Complex test cases
        ([5,5,5,5,5,5], 20),
        ([1,2,3,4,5,6,7,8], 35),
        
        # Test case with larger numbers
        ([10,20,30,40,50], 3)
    ]
    
    print("Running tests for Valid Triangle Number...\n")
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        start_time = time()
        result = solution.triangleNumber(nums.copy())  # Use copy to prevent modifying original
        end_time = time()
        
        print(f"Test Case {i}:")
        print(f"Input: nums = {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
        
        if result == expected:
            print("✅ Test case passed!")
        else:
            print("❌ Test case failed!")
        print()


if __name__ == "__main__":
    test_triangle_number()
