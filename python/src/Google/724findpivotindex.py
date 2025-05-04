"""
LeetCode 724: Find Pivot Index

Problem Statement:
Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left of the index
is equal to the sum of all the numbers strictly to the right of the index.
If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
This also applies to the right edge of the array.
Return the leftmost pivot index. If no such index exists, return -1.

Logic:
1. Calculate total sum of the array
2. Initialize left sum (prefix_sum) as 0
3. For each index i:
   - Calculate right sum = total_sum - prefix_sum - current_element
   - If prefix_sum equals right_sum, we found our pivot
   - Update prefix_sum by adding current element
4. If no pivot found, return -1

Time Complexity: O(n) - one pass to calculate total sum, one pass to find pivot
Space Complexity: O(1) - only using constant extra space
"""

from typing import List


class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        prefix_sum = 0

        for i, num in enumerate(nums):
            # Calculate right sum by subtracting the prefix sum and current element from total sum
            right_sum = total_sum - prefix_sum - num
            if prefix_sum == right_sum:
                return i
            prefix_sum += num

        return -1


def test_pivot_index():
    solution = Solution()

    # Test case 1: Basic case with pivot in middle
    test1 = [1, 7, 3, 6, 5, 6]
    assert solution.pivotIndex(test1) == 3, "Test case 1 failed"
    print("Test case 1: Input:", test1)
    print("Output:", solution.pivotIndex(test1))

    # Test case 2: No pivot exists
    test2 = [1, 2, 3]
    assert solution.pivotIndex(test2) == -1, "Test case 2 failed"
    print("\nTest case 2: Input:", test2)
    print("Output:", solution.pivotIndex(test2))

    # Test case 3: Pivot at beginning
    test3 = [2, 1, -1]
    assert solution.pivotIndex(test3) == 0, "Test case 3 failed"
    print("\nTest case 3: Input:", test3)
    print("Output:", solution.pivotIndex(test3))

    # Test case 4: Pivot at end
    test4 = [-1, 1, 2]
    assert solution.pivotIndex(test4) == 2, "Test case 4 failed"
    print("\nTest case 4: Input:", test4)
    print("Output:", solution.pivotIndex(test4))

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_pivot_index()
