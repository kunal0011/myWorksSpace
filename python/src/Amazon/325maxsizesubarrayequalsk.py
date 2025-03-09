"""
LeetCode 325 - Maximum Size Subarray Sum Equals k

Problem Statement:
Given an integer array nums and an integer k, return the maximum length of a subarray
that sums to k. Return 0 if no such subarray exists.

Logic:
1. Use prefix sum with hashmap approach:
   - Store running sum as key and earliest index as value
   - For each index i, check if (current_sum - k) exists in map
   - If found, update max length if current subarray is longer
2. Key points:
   - Initialize prefix_sum[0] = -1 for subarrays starting at index 0
   - Only store first occurrence of each sum (gives maximum length)
3. Time: O(n), Space: O(n)
"""

from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = {0: -1}
        current_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            current_sum += num
            if current_sum - k in prefix_sum:
                max_len = max(max_len, i - prefix_sum[current_sum - k])
            if current_sum not in prefix_sum:
                prefix_sum[current_sum] = i

        return max_len

def test_max_subarray_len():
    solution = Solution()
    
    # Test cases
    test_cases = [
        {
            'nums': [1, -1, 5, -2, 3], 
            'k': 3,
            'expected': 4,
            'explanation': "Subarray [1, -1, 5, -2] sums to 3"
        },
        {
            'nums': [-2, -1, 2, 1], 
            'k': 1,
            'expected': 2,
            'explanation': "Subarray [-2, -1, 2, 1] contains [-1, 2] that sums to 1"
        },
        {
            'nums': [1, 1, 1], 
            'k': 2,
            'expected': 2,
            'explanation': "Subarray [1, 1] sums to 2"
        },
        {
            'nums': [1], 
            'k': 1,
            'expected': 1,
            'explanation': "Single element equals k"
        },
        {
            'nums': [1, 0, -1], 
            'k': 0,
            'expected': 2,
            'explanation': "Subarray [1, 0, -1] contains [0] or [1, 0, -1] that sums to 0"
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        result = solution.maxSubArrayLen(test_case['nums'], test_case['k'])
        assert result == test_case['expected'], \
            f"Test case {i + 1} failed: expected {test_case['expected']}, got {result}"
        print(f"Test case {i + 1} passed:")
        print(f"Input: nums={test_case['nums']}, k={test_case['k']}")
        print(f"Output: {result}")
        print(f"Explanation: {test_case['explanation']}\n")

if __name__ == "__main__":
    test_max_subarray_len()
    print("All test cases passed!")
