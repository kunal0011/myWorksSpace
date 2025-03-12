"""
LeetCode 477 - Total Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given an integer array nums, return the sum of Hamming distances between all pairs of the integers in nums.

Example 1:
Input: nums = [4,14,2]
Output: 6
Explanation: In binary representation:
4  = 0100
14 = 1110
2  = 0010
The total Hamming distance between all pairs is:
hamming(4,14) + hamming(4,2) + hamming(14,2) = 2 + 2 + 2 = 6
"""

from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        total_distance = 0
        n = len(nums)
        
        # Optimize using list comprehension for counting ones at each bit position
        for bit_position in range(32):
            # Count ones at current bit position using bit manipulation
            count_ones = sum(1 for num in nums if num & (1 << bit_position))
            count_zeros = n - count_ones
            # For each bit position, contribution to total distance is
            # (number of 1s) * (number of 0s)
            total_distance += count_ones * count_zeros
            
        return total_distance

def test_hamming_distance():
    """Test function to verify the solution with multiple test cases"""
    test_cases = [
        ([4, 14, 2], 6),
        ([1, 2, 3], 4),
        ([2, 4, 6], 4),
        ([], 0),
        ([1], 0),
        ([1]*1000, 0)  # Edge case with identical numbers
    ]
    
    solution = Solution()
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.totalHammingDistance(nums)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Input: {nums}")
        print(f"Expected: {expected}, Got: {result}\n")

if __name__ == "__main__":
    test_hamming_distance()
