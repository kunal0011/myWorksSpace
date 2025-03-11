"""
LeetCode 396: Rotate Function

Problem Statement:
You are given an integer array nums of length n.
Assume arr_k to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:
- F(k) = 0 * arr_k[0] + 1 * arr_k[1] + ... + (n - 1) * arr_k[n - 1]
Return the maximum value of F(0), F(1), ..., F(n-1).

Example 1:
Input: nums = [4,3,2,6]
Output: 26
Explanation:
F(0) = 0*4 + 1*3 + 2*2 + 3*6 = 0 + 3 + 4 + 18 = 25
F(1) = 0*6 + 1*4 + 2*3 + 3*2 = 0 + 4 + 6 + 6 = 16
F(2) = 0*2 + 1*6 + 2*4 + 3*3 = 0 + 6 + 8 + 9 = 23
F(3) = 0*3 + 1*2 + 2*6 + 3*4 = 0 + 2 + 12 + 12 = 26

Time Complexity: O(n), where n is the length of nums
Space Complexity: O(1), only using constant extra space
"""

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        n = len(nums)
        array_sum = sum(nums)
        current_sum = sum(i * num for i, num in enumerate(nums))
        max_sum = current_sum
        
        # For each rotation, we can calculate next F(k) using:
        # F(k) = F(k-1) + sum(nums) - n * nums[n-k]
        for i in range(1, n):
            current_sum += array_sum - n * nums[n-i]
            max_sum = max(max_sum, current_sum)
            
        return max_sum

def test_rotate_function():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()
    
    test_cases = [
        {
            "nums": [4, 3, 2, 6],
            "expected": 26,
            "description": "Basic case with positive numbers"
        },
        {
            "nums": [100],
            "expected": 0,
            "description": "Single element array"
        },
        {
            "nums": [1, 2, 3, 4, 5],
            "expected": 40,
            "description": "Sequence of increasing numbers"
        },
        {
            "nums": [-2, -3, -4],
            "expected": -17,
            "description": "Negative numbers"
        },
        {
            "nums": [0, 0, 0],
            "expected": 0,
            "description": "Array of zeros"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input: nums = {nums}")
        
        result = solution.maxRotateFunction(nums)
        assert result == expected, f"Expected {expected}, but got {result}"
        print(f"✓ Test case passed! Output: {result}")

if __name__ == "__main__":
    test_rotate_function()
    print("\nAll test cases passed! 🎉")
