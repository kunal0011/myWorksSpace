"""
LeetCode 456 - 132 Pattern

Problem Statement:
-----------------
Given an array of n integers nums, a 132 pattern is a subsequence of three integers 
nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
Return true if there is a 132 pattern in nums, otherwise, return false.

Key Points:
----------
1. Need to find three numbers in specific order: nums[i] < nums[k] < nums[j]
2. Numbers don't need to be consecutive in the array
3. Order matters: i < j < k (positions in array)
4. Uses stack for efficient pattern finding
5. Scans array from right to left for optimization

Examples:
--------
Input: nums = [1,2,3,4]
Output: false
Explanation: No 132 pattern possible

Input: nums = [3,1,4,2]
Output: true
Explanation: nums[1] = 1, nums[2] = 4, nums[3] = 2 forms a 132 pattern

Input: nums = [-1,3,2,0]
Output: true
Explanation: nums[0] = -1, nums[1] = 3, nums[2] = 2 forms a 132 pattern

Constraints:
-----------
* n == nums.length
* 1 <= n <= 2 * 10^5
* -10^9 <= nums[i] <= 10^9
"""

from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        Find if there exists a 132 pattern in the array.
        
        Algorithm:
        1. Traverse array from right to left
        2. Use stack to maintain potential middle elements (nums[j])
        3. Keep track of largest potential third element (nums[k])
        4. For each element, check if it can be nums[i]
        
        Time Complexity: O(n) where n is length of array
        Space Complexity: O(n) for the stack
        """
        n = len(nums)
        if n < 3:
            return False

        stack = []  # Stack to maintain potential middle elements (nums[j])
        third = float('-inf')  # Tracks potential nums[k] value

        # Traverse right to left
        for i in range(n - 1, -1, -1):
            # If current number is smaller than third, we found a 132 pattern
            # Current number would be nums[i], third is nums[k]
            if nums[i] < third:
                return True

            # Update potential nums[k] by maintaining decreasing stack
            while stack and nums[i] > stack[-1]:
                third = stack.pop()

            # Add current number as potential nums[j]
            stack.append(nums[i])

        return False


def test_find_132_pattern():
    """
    Test driver for finding 132 pattern
    """
    test_cases = [
        (
            [1,2,3,4],
            False  # Strictly increasing sequence
        ),
        (
            [3,1,4,2],
            True  # Basic 132 pattern
        ),
        (
            [-1,3,2,0],
            True  # Pattern with negative number
        ),
        (
            [1,2],
            False  # Too short for pattern
        ),
        (
            [1],
            False  # Single element
        ),
        (
            [3,5,0,3,4],
            True  # Multiple potential patterns
        ),
        (
            [1,0,1,-4,-3],
            False  # No valid pattern despite ups and downs
        ),
        (
            [-2,1,2,-2,1,2],
            True  # Repeating pattern
        ),
        (
            [3,1,4,2,3],
            True  # Multiple valid patterns
        ),
        (
            [1,4,0,-1,-2,-3],
            True  # Decreasing sequence after peak
        )
    ]
    
    solution = Solution()
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution.find132pattern(nums)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input array: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        if result != expected:
            print("Note: For True results, one valid 132 pattern must exist")
            print("      For False results, no valid pattern exists")
        print("-" * 40)

if __name__ == "__main__":
    test_find_132_pattern()
