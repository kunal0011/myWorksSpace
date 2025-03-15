"""
LeetCode 918: Maximum Sum Circular Subarray

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array.
Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
"""

from typing import List
from time import perf_counter

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        # Handle single element case
        if len(nums) == 1:
            return nums[0]
            
        def kadane(arr: List[int], find_max: bool = True) -> int:
            curr = best = arr[0]
            for num in arr[1:]:
                if find_max:
                    curr = max(num, curr + num)
                    best = max(best, curr)
                else:
                    curr = min(num, curr + num)
                    best = min(best, curr)
            return best
        
        # Case 1: Maximum non-circular subarray
        max_normal = kadane(nums, True)
        
        # Case 2: Maximum circular subarray
        total = sum(nums)
        min_normal = kadane(nums, False)
        max_circular = total - min_normal if total != min_normal else float('-inf')
        
        return max(max_normal, max_circular)

def validate_array(nums: List[int]) -> bool:
    """Validate input according to constraints"""
    if not 1 <= len(nums) <= 3 * 10**4:
        return False
    return all(-3 * 10**4 <= x <= 3 * 10**4 for x in nums)

def visualize_array(nums: List[int], max_sum: int) -> str:
    """Create visual representation of the array and its maximum sum"""
    max_val = max(abs(x) for x in nums)
    scale = 40 // (max_val * 2)  # Scale factor for visualization
    
    result = []
    for num in nums:
        stars = "*" * int(abs(num) * scale)
        line = f"{num:4d} | {'▲' if num > 0 else '▼'}{stars}"
        result.append(line)
    
    result.append("-" * 50)
    result.append(f"Max Sum: {max_sum}")
    return "\n".join(result)

def test_circular_max_sum():
    """Test function for Maximum Sum Circular Subarray"""
    test_cases = [
        ([1,-2,3,-2], 3),
        ([5,-3,5], 10),
        ([-3,-2,-3], -2),
        ([3,-1,2,-1], 4),
        ([1,-1,3,-1], 4),
        ([2,-1,2], 3),
        ([1,2,3,4,-10,5], 15)
    ]
    
    solution = Solution()
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        is_valid = validate_array(nums)
        
        start_time = perf_counter()
        result = solution.maxSubarraySumCircular(nums)
        end_time = perf_counter()
        
        print(f"\nTest case {i}:")
        print(f"Array: {nums}")
        print("\nVisualization:")
        print(visualize_array(nums, result))
        print(f"\nExpected sum: {expected}")
        print(f"Actual sum: {result}")
        print(f"Time taken: {(end_time - start_time)*1000:.3f}ms")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional statistics
        print("\nArray statistics:")
        print(f"Length: {len(nums)}")
        print(f"Sum: {sum(nums)}")
        print(f"Average: {sum(nums)/len(nums):.2f}")
        print(f"Range: [{min(nums)}, {max(nums)}]")

if __name__ == "__main__":
    test_circular_max_sum()
