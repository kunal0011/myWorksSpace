"""
LeetCode 442 - Find All Duplicates in an Array

Problem Statement:
-----------------
Given an integer array nums of length n where all the integers of nums are in the 
range [1, n] and each integer appears once or twice, return an array of all the 
integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

Key Points:
----------
1. Array elements are in range [1, n] where n is array length
2. Each number appears once or twice (not more)
3. Must use O(1) extra space (can't use hash set/map)
4. Must solve in O(n) time (can't sort)
5. Can modify input array (used for marking visited numbers)

Examples:
--------
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Explanation: 2 and 3 appear twice in the array.

Input: nums = [1,1,2]
Output: [1]
Explanation: 1 appears twice in the array.

Constraints:
-----------
* n == nums.length
* 1 <= n <= 10^5
* 1 <= nums[i] <= n
* Each element in nums appears once or twice
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """
        Find all integers that appear twice in the array using O(1) extra space.
        
        Algorithm:
        1. Use array elements as indices (subtract 1 as array is 0-based)
        2. For each number, mark its corresponding index negative
        3. If we find a negative number at an index, that index+1 is a duplicate
        4. This works because each number is in range [1,n] and appears 1 or 2 times
        
        Time Complexity: O(n) where n is length of array
        Space Complexity: O(1) extra space (output array not counted)
        """
        result = []
        
        for num in nums:
            # Get the index this number represents (0-based)
            index = abs(num) - 1
            
            # If number at this index is negative, we've seen this number before
            if nums[index] < 0:
                result.append(index + 1)
            else:
                # Mark as visited by making it negative
                nums[index] = -nums[index]
                
        return result


def test_find_duplicates():
    """
    Test driver for finding duplicates in array
    """
    test_cases = [
        (
            [4,3,2,7,8,2,3,1],
            [2,3]  # Basic case with two duplicates
        ),
        (
            [1,1,2],
            [1]  # Single duplicate
        ),
        (
            [1],
            []  # No duplicates, single element
        ),
        (
            [1,2,3,4],
            []  # No duplicates
        ),
        (
            [1,1,1,1],
            [1]  # Not a valid input as per constraints, but should handle it
        ),
        (
            [2,2],
            [2]  # Minimal case with duplicate
        ),
        (
            [5,4,3,2,1,5,4,3,2,1],
            [1,2,3,4,5]  # All elements appear twice
        ),
        (
            [1,2,3,4,5,6,7,8,9,10,5,6],
            [5,6]  # Large array with duplicates at end
        )
    ]
    
    solution = Solution()
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        # Create a copy of nums as the function modifies the input
        nums_copy = nums.copy()
        result = sorted(solution.findDuplicates(nums_copy))  # Sort for consistent comparison
        expected = sorted(expected)  # Sort expected result too
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input array: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_find_duplicates()
