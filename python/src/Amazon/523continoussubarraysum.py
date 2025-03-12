"""
LeetCode 523 - Continuous Subarray Sum

Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.
A good subarray is a continuous subarray where:
- The length of the subarray is at least 2, and
- The sum of the elements of the subarray is a multiple of k.

Note:
- A continuous subarray is a subarray that consists of consecutive elements of the array.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2,4] is a continuous subarray of size 2 whose elements sum up to 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23,2,6,4,7] is a continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false
Explanation: There is no subarray of at least length 2 whose sum is divisible by 13.
"""

from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Edge case: array length less than 2
        if len(nums) < 2:
            return False
            
        # Handle k = 0 case
        if k == 0:
            # Check if there are two consecutive zeros
            return any(nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums)-1))
            
        # Dictionary to store prefix sum remainders and their indices
        remainder_dict = {0: -1}  # Initialize with 0 at index -1
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            
            # If we've seen this remainder before
            if remainder in remainder_dict:
                # Check if subarray length is at least 2
                if i - remainder_dict[remainder] >= 2:
                    return True
            else:
                # Only store the first occurrence of each remainder
                remainder_dict[remainder] = i
                
        return False

    def checkSubarraySum_alternative(self, nums: List[int], k: int) -> bool:
        """Alternative solution using sliding window approach"""
        if len(nums) < 2:
            return False
            
        # Handle k = 0 case
        if k == 0:
            return any(nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums)-1))
            
        # Convert all numbers to their remainder with k
        nums = [num % k for num in nums]
        
        # Use sliding window to check consecutive pairs
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_sum += nums[i]
            # If current sum is divisible by k
            if curr_sum % k == 0:
                return True
            # Check if there exists a previous subarray whose removal makes sum divisible by k
            temp_sum = curr_sum
            for j in range(i-1):
                temp_sum -= nums[j]
                if temp_sum % k == 0:
                    return True
                    
        return False


def test_continuous_subarray_sum():
    """Test function to verify both solution approaches"""
    solution = Solution()
    
    test_cases = [
        ([23,2,4,6,7], 6, True),
        ([23,2,6,4,7], 6, True),
        ([23,2,6,4,7], 13, False),
        ([1,0], 2, False),
        ([0,0], 1, True),
        ([1,2,3], 5, True),
        ([1,2,3], 6, True),
        ([1,2,3], 7, False),
        ([1,1000000000], 1, True),
        ([0,0,0,0], 0, True),
        ([1,2,3,4,5], 0, False),
        ([5,0,0,0], 3, True),
        ([23,2,4,6,6], 7, True),
        ([1,3,5], 2, True)
    ]
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        # Test main solution
        result_main = solution.checkSubarraySum(nums, k)
        # Test alternative solution
        result_alt = solution.checkSubarraySum_alternative(nums, k)
        
        status_main = "✓" if result_main == expected else "✗"
        status_alt = "✓" if result_alt == expected else "✗"
        
        print(f"Test {i}:")
        print(f"Input: nums={nums}, k={k}")
        print(f"Main Solution: {status_main} Got: {result_main}")
        print(f"Alternative Solution: {status_alt} Got: {result_alt}")
        print(f"Expected: {expected}\n")


if __name__ == "__main__":
    test_continuous_subarray_sum()