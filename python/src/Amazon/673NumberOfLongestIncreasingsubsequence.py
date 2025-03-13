"""
LeetCode 673: Number of Longest Increasing Subsequence

Problem Statement:
Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Key Points:
1. Find all longest increasing subsequences
2. Return the count of such sequences
3. The sequences must be strictly increasing
4. Multiple subsequences of same maximum length are possible
"""

from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        # lengths[i] = length of LIS ending at index i
        # counts[i] = number of LIS of length lengths[i] ending at index i
        lengths = [1] * n
        counts = [1] * n
        max_len = 1
        
        # Dynamic Programming approach
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        # Found a longer subsequence
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        # Found another subsequence of same length
                        counts[i] += counts[j]
            max_len = max(max_len, lengths[i])
        
        # Sum up counts of all subsequences with max_len
        result = sum(counts[i] for i in range(n) if lengths[i] == max_len)
        return result

def test_find_number_of_lis():
    solution = Solution()
    
    # Test cases: [nums, expected_result, description]
    test_cases = [
        ([1,3,5,4,7], 2, "Basic case with two LIS: [1,3,4,7] and [1,3,5,7]"),
        ([2,2,2,2,2], 5, "All equal numbers"),
        ([1,2,4,3,5,4,7,2], 3, "Complex case with multiple sequences"),
        ([1], 1, "Single element"),
        ([], 0, "Empty array"),
        ([3,1,2], 1, "Simple increasing sequence"),
        ([1,2,3,1,2,3,1,2,3], 27, "Multiple overlapping sequences"),
        ([10,9,8,7,6], 5, "Decreasing sequence"),
        ([1,1,1,2,2,2,3,3,3], 9, "Repeated numbers")
    ]
    
    for i, (nums, expected, description) in enumerate(test_cases, 1):
        result = solution.findNumberOfLIS(nums)
        assert result == expected, \
            f"Test {i} failed: Expected {expected}, got {result}"
        print(f"\nTest {i}: {description}")
        print(f"Input: {nums}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 50)

if __name__ == "__main__":
    test_find_number_of_lis()
