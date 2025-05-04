"""
LeetCode 740: Delete and Earn

Problem Statement:
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:
- Pick any nums[i] and delete it to earn nums[i] points
- After deleting nums[i], you must delete every element equal to nums[i] - 1 and nums[i] + 1
Return the maximum number of points you can earn by applying the above operation some number of times.

Logic:
1. Create a frequency counter for all numbers in the array
2. Convert problem to House Robber-like problem:
   - For each number n, we can either:
     a) Take n: earn n * frequency[n] points but can't take n-1
     b) Skip n: move to next number
3. Use Dynamic Programming:
   - dp[i] represents max points up to number i
   - For each number i:
     dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)
   where dp[i-1] represents skipping i
   and dp[i-2] + count[i] * i represents taking i

Time Complexity: O(n) where n is the maximum number in array
Space Complexity: O(n) for the dp array
"""

from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Step 1: Convert the list to a frequency map
        count = Counter(nums)
        max_num = max(nums)

        # Step 2: Initialize the dp array
        dp = [0] * (max_num + 1)

        # Step 3: Fill the dp array
        dp[1] = count[1] * 1
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)

        return dp[max_num]


def test_delete_and_earn():
    solution = Solution()

    # Test case 1: Basic case
    nums1 = [3, 4, 2]
    result1 = solution.deleteAndEarn(nums1)
    assert result1 == 6, f"Test case 1 failed. Expected 6, got {result1}"
    print(f"Test case 1 passed: nums = {nums1}, result = {result1}")

    # Test case 2: Multiple occurrences
    nums2 = [2, 2, 3, 3, 3, 4]
    result2 = solution.deleteAndEarn(nums2)
    assert result2 == 9, f"Test case 2 failed. Expected 9, got {result2}"
    print(f"Test case 2 passed: nums = {nums2}, result = {result2}")

    # Test case 3: Empty array
    nums3 = []
    result3 = solution.deleteAndEarn(nums3)
    assert result3 == 0, f"Test case 3 failed. Expected 0, got {result3}"
    print(f"Test case 3 passed: nums = {nums3}, result = {result3}")

    # Test case 4: Single element
    nums4 = [1]
    result4 = solution.deleteAndEarn(nums4)
    assert result4 == 1, f"Test case 4 failed. Expected 1, got {result4}"
    print(f"Test case 4 passed: nums = {nums4}, result = {result4}")

    # Test case 5: Non-consecutive numbers
    nums5 = [2, 4, 6, 8]
    result5 = solution.deleteAndEarn(nums5)
    assert result5 == 20, f"Test case 5 failed. Expected 20, got {result5}"
    print(f"Test case 5 passed: nums = {nums5}, result = {result5}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_delete_and_earn()
