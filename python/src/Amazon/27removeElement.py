from typing import List

"""
LeetCode 27. Remove Element

Problem Statement:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which
are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted,
you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which
  are not equal to val. The remaining elements are not important as well as the size of nums.
- Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements containing 0, 1, 3, 0, and 4.

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100

Approach:
1. Use two pointers: left and right
2. Move elements not equal to val to the left
3. Time Complexity: O(n)
4. Space Complexity: O(1)
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0  # Position to place next non-val element

        # Iterate through array
        for right in range(len(nums)):
            # If current element is not val, place it at left pointer
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1

        return left


def test_remove_element():
    """
    Test function to verify the removeElement solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "nums": [3, 2, 2, 3],
            "val": 3,
            "expected_k": 2,
            "expected_nums": [2, 2],
            "description": "Basic case with multiple occurrences"
        },
        {
            "nums": [0, 1, 2, 2, 3, 0, 4, 2],
            "val": 2,
            "expected_k": 5,
            "expected_nums": [0, 1, 3, 0, 4],
            "description": "Longer array with multiple occurrences"
        },
        {
            "nums": [],
            "val": 1,
            "expected_k": 0,
            "expected_nums": [],
            "description": "Empty array"
        },
        {
            "nums": [1],
            "val": 1,
            "expected_k": 0,
            "expected_nums": [],
            "description": "Single element equal to val"
        },
        {
            "nums": [1],
            "val": 2,
            "expected_k": 1,
            "expected_nums": [1],
            "description": "Single element not equal to val"
        },
        {
            "nums": [1, 1, 1],
            "val": 1,
            "expected_k": 0,
            "expected_nums": [],
            "description": "All elements equal to val"
        },
        {
            "nums": [1, 2, 3, 4],
            "val": 5,
            "expected_k": 4,
            "expected_nums": [1, 2, 3, 4],
            "description": "No elements equal to val"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"].copy()  # Create a copy to preserve original
        val = test_case["val"]
        expected_k = test_case["expected_k"]
        expected_nums = test_case["expected_nums"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: nums = {nums}, val = {val}")

        # Get result
        k = solution.removeElement(nums, val)
        result_nums = sorted(nums[:k])  # Sort because order doesn't matter
        expected_nums = sorted(expected_nums)  # Sort for comparison

        # Verify length
        assert k == expected_k, \
            f"\nTest case {i} failed!\nExpected length: {expected_k}\nGot: {k}"

        # Verify array contents
        assert result_nums == expected_nums, \
            f"\nTest case {i} failed!\nExpected first {k} elements (sorted): {expected_nums}\nGot: {result_nums}"

        print(f"✓ Test case {i} passed!")
        print(f"  Modified array (first {k} elements): {nums[:k]}")


if __name__ == "__main__":
    try:
        test_remove_element()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
