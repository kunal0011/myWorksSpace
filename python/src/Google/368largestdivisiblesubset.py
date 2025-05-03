"""
LeetCode 368 - Largest Divisible Subset

Problem Statement:
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
- answer[i] % answer[j] == 0, or
- answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        if not nums:
            return []
        
        # Sort the array to ensure if a divides b and b divides c, then a divides c
        nums.sort()
        n = len(nums)
        
        # dp[i] stores the length of largest divisible subset ending at nums[i]
        dp = [1] * n
        
        # prev[i] stores the previous index that forms the subset with nums[i]
        prev = [-1] * n
        max_len = 1
        max_index = 0
        
        # Build dp array
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            
            # Keep track of the index that gives the longest subset
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i
        
        # Reconstruct the subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = prev[max_index]
        
        return result[::-1]  # Reverse to get elements in ascending order


def test_largest_divisible_subset():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,2,3], [1,2]),
        ([1,2,4,8], [1,2,4,8]),
        ([3,4,16,8], [4,8,16]),
        ([1], [1]),
        ([4,8,16], [4,8,16]),
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.largestDivisibleSubset(nums)
        # Check if result is valid (might be different from expected as multiple solutions possible)
        is_valid = len(result) == len(expected)
        if is_valid:
            # Verify that each pair in the result satisfies the divisibility condition
            for i in range(len(result)):
                for j in range(len(result)):
                    if not (result[i] % result[j] == 0 or result[j] % result[i] == 0):
                        is_valid = False
                        break
        print(f"Test case {i}:")
        print(f"Input: {nums}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"Valid: {is_valid}\n")


if __name__ == "__main__":
    test_largest_divisible_subset()