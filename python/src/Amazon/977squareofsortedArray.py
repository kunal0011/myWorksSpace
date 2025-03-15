"""
LeetCode 977: Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares 
of each number sorted in non-decreasing order.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order
"""

from typing import List
from time import perf_counter

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1
        
        while left <= right:
            left_sq = nums[left] * nums[left]
            right_sq = nums[right] * nums[right]
            
            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:
                result[pos] = right_sq
                right -= 1
            pos -= 1
            
        return result

def validate_array(nums: List[int]) -> bool:
    """Validate array according to constraints"""
    if not 1 <= len(nums) <= 10**4:
        return False
    if not all(-10**4 <= x <= 10**4 for x in nums):
        return False
    # Check if sorted
    return all(nums[i] <= nums[i+1] for i in range(len(nums)-1))

def visualize_squares(nums: List[int], result: List[int]) -> None:
    """Create visual representation of squares transformation"""
    max_val = max(abs(min(nums)), abs(max(nums)))
    scale = 40 // (max_val * 2)
    
    print("\nInput array visualization:")
    for num in nums:
        stars = "*" * int(abs(num) * scale)
        print(f"{num:6d} | {'▲' if num >= 0 else '▼'}{stars}")
        
    print("\nSquared array visualization:")
    for num in result:
        stars = "*" * int((num ** 0.5) * scale)
        print(f"{num:6d} | ▲{stars}")

def test_sorted_squares():
    """Test function for Squares of a Sorted Array"""
    test_cases = [
        ([-4,-1,0,3,10], [0,1,9,16,100]),
        ([-7,-3,2,3,11], [4,9,9,49,121]),
        ([0,1,2,3,4], [0,1,4,9,16]),
        ([-5,-4,-3,-2,-1], [1,4,9,16,25]),
        ([-10000,10000], [100000000,100000000])
    ]
    
    solution = Solution()
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        is_valid = validate_array(nums)
        
        start_time = perf_counter()
        result = solution.sortedSquares(nums)
        end_time = perf_counter()
        
        print(f"\nTest case {i}:")
        print(f"Input array: {nums}")
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        print(f"Time taken: {(end_time - start_time)*1000:.3f}ms")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        if len(nums) <= 10:  # Only visualize small arrays
            visualize_squares(nums, result)
            
        # Additional statistics
        print("\nArray statistics:")
        print(f"Length: {len(nums)}")
        print(f"Input range: [{min(nums)}, {max(nums)}]")
        print(f"Output range: [{min(result)}, {max(result)}]")
        print(f"Zero crossings: {sum(1 for i in range(len(nums)-1) if nums[i] < 0 and nums[i+1] >= 0)}")

if __name__ == "__main__":
    test_sorted_squares()
