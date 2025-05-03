"""
LeetCode 410 - Split Array Largest Sum

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that 
the largest sum among all subarrays is minimized.

Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

Example 1:
Input: nums = [7,2,5,10,8], k = 2
Output: 18
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

Example 2:
Input: nums = [1,2,3,4,5], k = 2
Output: 9
Explanation: There are four ways to split nums into two subarrays.
The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.
"""

from typing import List

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(largest_sum: int) -> bool:
            """Check if we can split array into k or fewer subarrays with max sum <= largest_sum"""
            count = 1
            current_sum = 0
            
            for num in nums:
                if current_sum + num <= largest_sum:
                    current_sum += num
                else:
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
            return True
        
        # Binary search boundaries
        left = max(nums)  # Minimum possible result
        right = sum(nums)  # Maximum possible result
        
        # Binary search for the minimum largest subarray sum
        result = right
        while left <= right:
            mid = (left + right) // 2
            
            if can_split(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result


# Test driver
def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([7,2,5,10,8], 2),    # Should return 18
        ([1,2,3,4,5], 2),     # Should return 9
        ([1,4,4], 3),         # Should return 4
        ([2,3,1,2,4,3], 5),   # Should return 4
        ([1,1,1,1,1], 3)      # Should return 2
    ]
    
    for nums, k in test_cases:
        result = solution.splitArray(nums, k)
        print(f"\nInput: nums = {nums}, k = {k}")
        print(f"Output: {result}")


if __name__ == "__main__":
    main()