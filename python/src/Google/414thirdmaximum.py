"""
LeetCode 414 - Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation: The first distinct maximum is 3, the second distinct maximum is 2, 
and the third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation: The first distinct maximum is 2, the second distinct maximum is 1, 
and the third distinct maximum does not exist, so the maximum (2) is returned.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation: The first distinct maximum is 3, the second distinct maximum is 2, 
and the third distinct maximum is 1.
"""

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Initialize three maximum variables with None
        first = second = third = float('-inf')
        
        # Process each number
        for num in nums:
            # Skip duplicates
            if num in [first, second, third]:
                continue
            
            # Update maximums
            if num > first:
                third = second
                second = first
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        
        # Return third maximum if it exists, otherwise return first maximum
        return third if third != float('-inf') else first


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        [3, 2, 1],           # Should return 1
        [1, 2],              # Should return 2
        [2, 2, 3, 1],        # Should return 1
        [5, 2, 2, 1, 5, 4],  # Should return 2
        [1, 1, 2],           # Should return 2
        [1, 2, -2147483648]  # Should return -2147483648
    ]
    
    for nums in test_cases:
        result = solution.thirdMax(nums)
        print(f"\nInput: nums = {nums}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()