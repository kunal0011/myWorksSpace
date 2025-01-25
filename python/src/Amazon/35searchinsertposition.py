from typing import List

"""
LeetCode 35. Search Insert Position

Problem Statement:
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:
- 1 <= nums.length <= 104
- -104 <= nums[i] <= 104
- nums contains distinct values sorted in ascending order
- -104 <= target <= 104

Approach:
1. Use binary search to find insert position
2. Keep track of potential insert position during search
3. Time Complexity: O(log n)
4. Space Complexity: O(1)
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # Handle edge cases where target is outside array bounds
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)

        # Binary search
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


def explain_search_insert(nums: List[int], target: int) -> None:
    """
    Function to explain the search insert process step by step
    """
    print(f"\nFinding insert position for {target} in {nums}")
    print("=" * 50)

    # Handle edge cases
    if target < nums[0]:
        print(f"Target {target} is less than smallest element {nums[0]}")
        print("Insert position: 0")
        return
    if target > nums[-1]:
        print(f"Target {target} is greater than largest element {nums[-1]}")
        print(f"Insert position: {len(nums)}")
        return

    left, right = 0, len(nums) - 1
    step = 1

    while left <= right:
        mid = (left + right) // 2
        print(f"\nStep {step}:")
        print(f"Current window: {nums[left:right+1]}")
        print(f"Indices - left: {left}, mid: {mid}, right: {right}")
        print(
            f"Values - left: {nums[left]}, mid: {nums[mid]}, right: {nums[right]}")

        if nums[mid] == target:
            print(f"Found target at index {mid}!")
            return
        elif nums[mid] < target:
            print(
                f"Target {target} is greater than {nums[mid]}, search right half")
            left = mid + 1
        else:
            print(
                f"Target {target} is less than {nums[mid]}, search left half")
            right = mid - 1

        step += 1

    print(f"\nTarget not found. Insert position: {left}")


def test_search_insert():
    """
    Test function to verify the searchInsert solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "nums": [1, 3, 5, 6],
            "target": 5,
            "expected": 2,
            "description": "Target found in array"
        },
        {
            "nums": [1, 3, 5, 6],
            "target": 2,
            "expected": 1,
            "description": "Target not found, insert in middle"
        },
        {
            "nums": [1, 3, 5, 6],
            "target": 7,
            "expected": 4,
            "description": "Target greater than all elements"
        },
        {
            "nums": [1, 3, 5, 6],
            "target": 0,
            "expected": 0,
            "description": "Target less than all elements"
        },
        {
            "nums": [1],
            "target": 1,
            "expected": 0,
            "description": "Single element array, target found"
        },
        {
            "nums": [1, 3],
            "target": 2,
            "expected": 1,
            "description": "Two elements, insert between"
        },
        {
            "nums": [1, 3, 5, 7, 9],
            "target": 8,
            "expected": 4,
            "description": "Larger array, insert between elements"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: nums = {nums}, target = {target}")

        result = solution.searchInsert(nums, target)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_search_insert()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with examples
        explain_search_insert([1, 3, 5, 6], 5)  # Target found
        explain_search_insert([1, 3, 5, 6], 2)  # Target not found
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
