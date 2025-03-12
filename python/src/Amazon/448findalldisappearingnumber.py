"""
LeetCode 448 - Find All Numbers Disappeared in an Array

Problem Statement:
-----------------
Given an array nums of n integers where nums[i] is in the range [1, n], return an array 
of all the integers in the range [1, n] that do not appear in nums.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Key Points:
----------
1. Array elements are in range [1, n] where n is array length
2. Need to find missing numbers in range [1, n]
3. Must use O(1) extra space (can't use hash set/map)
4. Must solve in O(n) time
5. Can modify input array for marking visited numbers

Examples:
--------
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Explanation: 5 and 6 are missing from range [1,8]

Input: nums = [1,1]
Output: [2]
Explanation: 2 is missing from range [1,2]

Constraints:
-----------
* n == nums.length
* 1 <= n <= 10^5
* 1 <= nums[i] <= n
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Find all numbers that are missing from the array using O(1) extra space.
        
        Algorithm:
        1. Use array elements as indices to mark visited numbers
        2. Mark visited by making the number at that index negative
        3. Positive numbers at the end indicate missing indices
        4. Convert positive indices back to numbers by adding 1
        
        Time Complexity: O(n) where n is length of array
        Space Complexity: O(1) extra space (output array not counted)
        """
        # Mark numbers that are present by making their corresponding indices negative
        for num in nums:
            index = abs(num) - 1  # Get 0-based index from number
            nums[index] = -abs(nums[index])  # Mark as visited
            
        # Collect indices where numbers are still positive (missing numbers)
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


def test_find_disappeared_numbers():
    """
    Test driver for finding disappeared numbers in array
    """
    test_cases = [
        (
            [4,3,2,7,8,2,3,1],
            [5,6]  # Basic case with multiple missing numbers
        ),
        (
            [1,1],
            [2]  # Case with duplicate and one missing
        ),
        (
            [1],
            []  # Single element, no missing numbers
        ),
        (
            [1,1,2,2],
            [3,4]  # Multiple duplicates and missing numbers
        ),
        (
            [1,2,3,4],
            []  # No missing numbers
        ),
        (
            [2,2,2,2],
            [1,3,4]  # Same number repeated multiple times
        ),
        (
            [1,2,2,4],
            [3]  # Single missing number in middle
        ),
        (
            [2,3,4,5,6,7,8,8],
            [1]  # Missing first number
        )
    ]
    
    solution = Solution()
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        # Create a copy as the function modifies the input
        nums_copy = nums.copy()
        result = solution.findDisappearedNumbers(nums_copy)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input array: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_find_disappeared_numbers()
