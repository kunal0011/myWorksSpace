from typing import List

"""
LeetCode 26. Remove Duplicates from Sorted Array

Problem Statement:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should 
be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do 
the following things:
- Change the array nums such that the first k elements of nums contain the unique elements 
  in the order they were present in nums initially.
- Return k.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements being 0, 1, 2, 3, and 4.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order

Approach:
1. Use two pointers: slow and fast
2. Fast pointer scans for unique elements
3. Slow pointer keeps track of position to place next unique element
4. Time Complexity: O(n)
5. Space Complexity: O(1)
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Initialize the pointer for placing next unique element
        slow = 1

        # Scan through array starting from second element
        for fast in range(1, len(nums)):
            # If we find a new unique element
            if nums[fast] != nums[fast - 1]:
                # Place it at the slow pointer position
                nums[slow] = nums[fast]
                slow += 1

        return slow


def test_remove_duplicates():
    """
    Test function to verify the removeDuplicates solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "input": [1, 1, 2],
            "expected_k": 2,
            "expected_array": [1, 2],
            "description": "Basic case with one duplicate"
        },
        {
            "input": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            "expected_k": 5,
            "expected_array": [0, 1, 2, 3, 4],
            "description": "Multiple duplicates"
        },
        {
            "input": [1],
            "expected_k": 1,
            "expected_array": [1],
            "description": "Single element"
        },
        {
            "input": [1, 1, 1, 1, 1],
            "expected_k": 1,
            "expected_array": [1],
            "description": "All elements same"
        },
        {
            "input": [1, 2, 3, 4, 5],
            "expected_k": 5,
            "expected_array": [1, 2, 3, 4, 5],
            "description": "No duplicates"
        },
        {
            "input": [-3, -3, -2, -1, -1, 0, 0, 0, 2],
            "expected_k": 5,
            "expected_array": [-3, -2, -1, 0, 2],
            "description": "Negative numbers with duplicates"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["input"].copy()  # Create a copy to preserve original
        expected_k = test_case["expected_k"]
        expected_array = test_case["expected_array"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input array: {nums}")

        # Get result
        k = solution.removeDuplicates(nums)
        result_array = nums[:k]

        # Verify length
        assert k == expected_k, \
            f"\nTest case {i} failed!\nExpected length: {expected_k}\nGot: {k}"

        # Verify array contents
        assert result_array == expected_array, \
            f"\nTest case {i} failed!\nExpected array: {expected_array}\nGot: {result_array}"

        print(f"✓ Test case {i} passed!")
        print(f"  Modified array (first {k} elements): {result_array}")


if __name__ == "__main__":
    try:
        test_remove_duplicates()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
