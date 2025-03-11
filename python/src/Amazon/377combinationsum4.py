"""
LeetCode 377: Combination Sum IV
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated such that the answer can fit in a 32-bit integer.
Follow up: What if negative numbers are allowed in the nums array?
- With negative numbers, the problem could have infinite solutions as we can keep using numbers that sum to 0.
- To handle this, we would need to add constraints like limiting the length of combinations.

Example:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Time Complexity: O(target * len(nums))
Space Complexity: O(target)
"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Edge cases
        if not nums or target < 0:
            return 0
        
        # Optimization: Sort nums to potentially break early in some cases
        nums.sort()
        
        # dp[i] represents the number of combinations that sum to i
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: empty combination sums to 0
        
        # For each sum from 1 to target
        for curr_sum in range(1, target + 1):
            # Try to use each number from nums
            for num in nums:
                # If current number is too large, break since nums is sorted
                if num > curr_sum:
                    break
                # Add the number of combinations that sum to (curr_sum - num)
                dp[curr_sum] += dp[curr_sum - num]
        
        return dp[target]


def run_test_cases() -> None:
    """Function to run comprehensive test cases"""
    solution = Solution()
    
    # Test case 1: Basic case
    nums1, target1 = [1, 2, 3], 4
    result1 = solution.combinationSum4(nums1, target1)
    print(f"\nTest Case 1:")
    print(f"nums = {nums1}, target = {target1}")
    print(f"Expected: 7")
    print(f"Got: {result1}")
    print(f"Result: {'PASSED' if result1 == 7 else 'FAILED'}")
    
    # Test case 2: Single number
    nums2, target2 = [1], 1
    result2 = solution.combinationSum4(nums2, target2)
    print(f"\nTest Case 2:")
    print(f"nums = {nums2}, target = {target2}")
    print(f"Expected: 1")
    print(f"Got: {result2}")
    print(f"Result: {'PASSED' if result2 == 1 else 'FAILED'}")
    
    # Test case 3: Impossible target
    nums3, target3 = [2, 4], 7
    result3 = solution.combinationSum4(nums3, target3)
    print(f"\nTest Case 3:")
    print(f"nums = {nums3}, target = {target3}")
    print(f"Expected: 0")
    print(f"Got: {result3}")
    print(f"Result: {'PASSED' if result3 == 0 else 'FAILED'}")
    
    # Test case 4: Large numbers
    nums4, target4 = [10, 20, 30], 60
    result4 = solution.combinationSum4(nums4, target4)
    print(f"\nTest Case 4:")
    print(f"nums = {nums4}, target = {target4}")
    print(f"Expected: 5")
    print(f"Got: {result4}")
    print(f"Result: {'PASSED' if result4 == 5 else 'FAILED'}")
    
    # Test case 5: Empty array
    nums5, target5 = [], 5
    result5 = solution.combinationSum4(nums5, target5)
    print(f"\nTest Case 5:")
    print(f"nums = {nums5}, target = {target5}")
    print(f"Expected: 0")
    print(f"Got: {result5}")
    print(f"Result: {'PASSED' if result5 == 0 else 'FAILED'}")


if __name__ == "__main__":
    run_test_cases()
