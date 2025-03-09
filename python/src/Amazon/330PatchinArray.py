"""
LeetCode 330: Patching Array

Problem Statement:
Given a sorted integer array nums and an integer n, you need to add the minimal number of patches
to make the array cover all numbers in the range [1, n]. A patch is a number that we can add to the array.
An array covers the range [1, n] if for every number x in [1, n], there exists a subset of numbers in the array
whose sum equals x.

Example 1:
Input: nums = [1,3], n = 6
Output: 1
Explanation: Add 2 to make array [1,2,3] cover range [1,6]

Example 2:
Input: nums = [1,5,10], n = 20
Output: 2
Explanation: Add 2 and 4 to make array [1,2,4,5,10] cover range [1,20]

Logic:
1. We use a greedy approach to find the minimal number of patches needed.
2. We maintain a variable current_range that represents the range [1, current_range) that we can already form.
3. For each step:
   - If we can use the current number from array (nums[i] <= current_range), we extend our range.
   - Otherwise, we need to patch the array with current_range itself to maximize our coverage.
4. We continue this process until we can cover all numbers up to n.
"""

from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        i = 0
        current_range = 1  # The smallest number we cannot cover

        while current_range <= n:
            # If nums[i] is within the current range, extend the range
            if i < len(nums) and nums[i] <= current_range:
                current_range += nums[i]
                i += 1
            # Otherwise, we need to patch the array with current_range
            else:
                current_range += current_range
                patches += 1

        return patches


def run_test_cases():
    solution = Solution()
    
    # Test case 1
    nums1 = [1, 3]
    n1 = 6
    result1 = solution.minPatches(nums1, n1)
    print(f"Test case 1: nums = {nums1}, n = {n1}")
    print(f"Expected: 1, Got: {result1}")
    print(f"Pass? {result1 == 1}\n")
    
    # Test case 2
    nums2 = [1, 5, 10]
    n2 = 20
    result2 = solution.minPatches(nums2, n2)
    print(f"Test case 2: nums = {nums2}, n = {n2}")
    print(f"Expected: 2, Got: {result2}")
    print(f"Pass? {result2 == 2}\n")
    
    # Test case 3
    nums3 = [1, 2, 4, 13, 43]
    n3 = 100
    result3 = solution.minPatches(nums3, n3)
    print(f"Test case 3: nums = {nums3}, n = {n3}")
    print(f"Expected: 2, Got: {result3}")
    print(f"Pass? {result3 == 2}\n")


if __name__ == "__main__":
    run_test_cases()
