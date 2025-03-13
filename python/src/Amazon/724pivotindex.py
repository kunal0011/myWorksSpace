"""
LeetCode 724: Find Pivot Index

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left
of the index is equal to the sum of all the numbers strictly to the right of the index.

If the index is on the left edge of the array, then the left sum is 0 because there
are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        
        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        
        return -1

def test_pivot_index():
    """Test function for pivotIndex with multiple test cases"""
    solution = Solution()
    
    test_cases = [
        ([1,7,3,6,5,6], 3),
        ([1,2,3], -1),
        ([2,1,-1], 0),
        ([], -1),
        ([1], 0),
        ([1,2], -1),
        ([-1,-1,-1,0,1,1], 0)
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.pivotIndex(nums)
        success = result == expected
        print(f"\nTest case {i}:")
        print(f"Input array: {nums}")
        print(f"Expected pivot: {expected}")
        print(f"Got pivot: {result}")
        print(f"{'✓ Passed' if success else '✗ Failed'}")

if __name__ == "__main__":
    test_pivot_index()
