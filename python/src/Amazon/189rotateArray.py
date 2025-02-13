from typing import List


class Solution:
    """
    LeetCode 189 - Rotate Array

    Problem Statement:
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
    Must be done in-place with O(1) extra space.

    Example:
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Solution Logic:
        1. First normalize k by taking k % n to handle cases where k > length of array
        2. Use the reverse technique to rotate array:
           - Reverse the entire array
           - Reverse first k elements
           - Reverse remaining n-k elements

        Time Complexity: O(n)
        Space Complexity: O(1)

        Args:
            nums: List of integers to rotate
            k: Number of positions to rotate right
        """
        n = len(nums)
        k = k % n  # Normalize k

        def reverse(start: int, end: int) -> None:
            """Helper function to reverse array elements from start to end indices"""
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        # Three-step array rotation
        reverse(0, n - 1)    # Reverse entire array
        reverse(0, k - 1)    # Reverse first k elements
        reverse(k, n - 1)    # Reverse remaining elements


def run_tests():
    """Test driver for the rotate array solution"""
    solution = Solution()

    # Test cases
    test_cases = [
        {
            'nums': [1, 2, 3, 4, 5, 6, 7],
            'k': 3,
            'expected': [5, 6, 7, 1, 2, 3, 4]
        },
        {
            'nums': [-1, -100, 3, 99],
            'k': 2,
            'expected': [3, 99, -1, -100]
        },
        {
            'nums': [1],
            'k': 0,
            'expected': [1]
        },
        {
            'nums': [1, 2],
            'k': 3,
            'expected': [2, 1]
        }
    ]

    for i, test in enumerate(test_cases, 1):
        nums = test['nums'].copy()
        solution.rotate(nums, test['k'])
        result = nums == test['expected']
        print(f"Test {i}:")
        print(f"Input: nums = {test['nums']}, k = {test['k']}")
        print(f"Output: {nums}")
        print(f"Expected: {test['expected']}")
        print(f"Result: {'✓ PASS' if result else '✗ FAIL'}\n")


if __name__ == "__main__":
    run_tests()
