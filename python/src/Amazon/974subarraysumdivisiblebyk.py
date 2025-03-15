"""
LeetCode 974: Subarray Sums Divisible by K

Given an integer array nums and an integer k, return the number of non-empty subarrays 
that have a sum divisible by k.

A subarray is a contiguous part of an array.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10^4
"""

from typing import List
from collections import defaultdict
from time import perf_counter

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = defaultdict(int)
        remainders[0] = 1  # Empty subarray
        
        curr_sum = 0
        count = 0
        
        for num in nums:
            curr_sum += num
            # Handle negative numbers properly with modulo
            remainder = curr_sum % k
            count += remainders[remainder]
            remainders[remainder] += 1
            
        return count

def validate_input(nums: List[int], k: int) -> bool:
    """Validate input according to constraints"""
    if not 1 <= len(nums) <= 3 * 10**4:
        return False
    if not all(-10**4 <= x <= 10**4 for x in nums):
        return False
    if not 2 <= k <= 10**4:
        return False
    return True

def find_divisible_subarrays(nums: List[int], k: int) -> List[List[int]]:
    """Find all subarrays with sum divisible by k (for small inputs)"""
    result = []
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum % k == 0:
                result.append(nums[i:j+1])
    return result

def test_subarrays_div_by_k():
    """Test function for Subarray Sums Divisible by K"""
    test_cases = [
        ([4,5,0,-2,-3,1], 5, 7),
        ([5], 9, 0),
        ([0,0,0], 2, 6),
        ([1,2,3,4,5], 3, 4),
        ([-1,-2,-3,-4,0], 3, 3),
        ([7,8,9,10], 7, 1)
    ]
    
    solution = Solution()
    
    for i, (nums, k, expected) in enumerate(test_cases, 1):
        is_valid = validate_input(nums, k)
        
        start_time = perf_counter()
        result = solution.subarraysDivByK(nums, k)
        end_time = perf_counter()
        
        print(f"\nTest case {i}:")
        print(f"Array: {nums}")
        print(f"k: {k}")
        print(f"Expected count: {expected}")
        print(f"Got count: {result}")
        print(f"Time taken: {(end_time - start_time)*1000:.3f}ms")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Show divisible subarrays for small inputs
        if len(nums) <= 10:
            divisible = find_divisible_subarrays(nums, k)
            print("\nDivisible subarrays:")
            for subarray in divisible:
                print(f"{subarray} (sum={sum(subarray)})")
        
        # Additional statistics
        print("\nArray statistics:")
        print(f"Length: {len(nums)}")
        print(f"Sum: {sum(nums)}")
        print(f"Range: [{min(nums)}, {max(nums)}]")
        print(f"Remainder distribution:")
        remainders = [sum(nums[i:j+1]) % k for i in range(len(nums)) 
                     for j in range(i, len(nums))]
        for r in range(k):
            count = remainders.count(r)
            if count > 0:
                print(f"  Remainder {r}: {count} subarrays")

if __name__ == "__main__":
    test_subarrays_div_by_k()
