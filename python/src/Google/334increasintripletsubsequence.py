"""
LeetCode 334 - Increasing Triplet Subsequence

Problem Statement:
Given an integer array nums, return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
"""

class Solution:
    def increasingTriplet(self, nums):
        # Initialize the first and second smallest numbers
        first = float('inf')
        second = float('inf')

        # Iterate through the array
        for num in nums:
            if num <= first:
                # Update the smallest number
                first = num
            elif num <= second:
                # Update the second smallest number
                second = num
            else:
                # If we find a number greater than both first and second, return True
                return True

        # If no such triplet is found, return False
        return False

def run_tests():
    solution = Solution()
    
    test_cases = [
        ([1,2,3,4,5], True),
        ([5,4,3,2,1], False),
        ([2,1,5,0,4,6], True),
        ([20,100,10,12,5,13], True),
        ([1,1,1,1,1], False),
        ([1,5,0,4,1,3], True),
        ([2,4,-2,-3], False)
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.increasingTriplet(nums)
        print(f"\nTest case {i}:")
        print(f"Input: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")

if __name__ == "__main__":
    run_tests()
