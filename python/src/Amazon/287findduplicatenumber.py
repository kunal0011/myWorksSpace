"""
LeetCode 287 - Find the Duplicate Number

Problem Statement:
Given an array nums containing n + 1 integers where each integer is in the range [1, n],
there is only one repeated number in nums. Find this repeated number.
You must solve the problem without modifying the array and using only constant extra space.

Logic:
1. Use Floyd's Tortoise and Hare (Cycle Detection) algorithm
2. Treat array values as pointers to next index
3. Phase 1: Find intersection point using two pointers moving at different speeds
4. Phase 2: Find cycle entrance (duplicate number) by moving both pointers at same speed
5. Time: O(n), Space: O(1)
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the intersection point in the cycle
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: Find the entrance to the cycle
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


def test_find_duplicate():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1,3,4,2,2], 2),         # Standard case
        ([3,1,3,4,2], 3),         # Duplicate at different position
        ([2,2,2,2,2], 2),         # All same numbers
        ([1,1], 1),               # Minimal case
        ([2,5,9,6,9,3,8,9,7,1], 9)  # Larger array
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        result = solution.findDuplicate(nums)
        assert result == expected, f"Test case {i + 1} failed: nums={nums}, expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: nums={nums}, duplicate={result}")

if __name__ == "__main__":
    test_find_duplicate()
    print("All test cases passed!")
