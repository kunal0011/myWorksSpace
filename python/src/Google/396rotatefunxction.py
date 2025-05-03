"""
LeetCode 396 - Rotate Function

You are given an integer array nums of length n.
Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:
- F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
Return the maximum value of F(0), F(1), ..., F(n-1).

Example 1:
Input: nums = [4,3,2,6]
Output: 26
Explanation:
F(0) = 0*4 + 1*3 + 2*2 + 3*6 = 0 + 3 + 4 + 18 = 25
F(1) = 0*6 + 1*4 + 2*3 + 3*2 = 0 + 4 + 6 + 6 = 16
F(2) = 0*2 + 1*6 + 2*4 + 3*3 = 0 + 6 + 8 + 9 = 23
F(3) = 0*3 + 1*2 + 2*6 + 3*4 = 0 + 2 + 12 + 12 = 26

Example 2:
Input: nums = [100]
Output: 0
"""

def maxRotateFunction(nums: list[int]) -> int:
    # Optimized O(n) solution using mathematical pattern
    n = len(nums)
    if n <= 1:
        return 0
    
    # Calculate F(0)
    array_sum = sum(nums)
    current_sum = sum(i * num for i, num in enumerate(nums))
    max_sum = current_sum
    
    # F(k) = F(k-1) + sum(array) - n * nums[n-k]
    for i in range(1, n):
        current_sum = current_sum + array_sum - (n * nums[n-i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def test_rotate_function():
    # Test cases
    test_cases = [
        ([4, 3, 2, 6], 26),
        ([100], 0),
        ([1, 2, 3, 4, 5], 40),
        ([1, 1, 1], 2),
        ([-8, 5, -10, 1, 4], 30)
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = maxRotateFunction(nums)
        assert result == expected, f"Test case {i} failed: expected {expected}, got {result}"
        print(f"Test case {i} passed: {nums} -> {result}")

if __name__ == "__main__":
    test_rotate_function()
    print("All test cases passed successfully!")