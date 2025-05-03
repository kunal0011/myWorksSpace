"""
LeetCode 377 - Combination Sum IV

Problem Statement:
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
The test cases are generated such that the answer can fit in a 32-bit integer.
The order of the combinations matters (unlike Combination Sum problems I, II, and III).

Example:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(2, 1, 1)
(1, 3)
(3, 1)
(2, 2)

Time Complexity: O(target * len(nums))
Space Complexity: O(target)
"""

class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        # dp[i] represents number of ways to make sum i
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: empty sum can be made in 1 way
        
        # For each sum from 1 to target
        for i in range(1, target + 1):
            # Try to use each number from nums
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        
        return dp[target]


def test_combination_sum4():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,2,3], 4, 7),           # Example from problem statement
        ([9], 3, 0),               # Impossible case
        ([1,2,3], 32, 181997601),  # Large target
        ([4,2,1], 32, 39882198),   # Different numbers
        ([1], 1, 1),               # Single number, single target
        ([1,2,3], 0, 1),           # Zero target
    ]
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution.combinationSum4(nums, target)
        print(f"Test case {i}:")
        print(f"nums = {nums}")
        print(f"target = {target}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Pass: {result == expected}\n")


if __name__ == "__main__":
    test_combination_sum4()