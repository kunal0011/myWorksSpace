from typing import List

"""
LeetCode 33. Search in Rotated Sorted Array

Problem Statement:
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot 
index k (1 <= k < nums.length) such that the resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index 
of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Constraints:
- 1 <= nums.length <= 5000
- -104 <= nums[i] <= 104
- All values of nums are unique
- nums is possibly rotated
- -104 <= target <= 104

Approach:
1. Use modified binary search
2. Determine which half of array is sorted
3. Check if target lies in sorted half
4. Time Complexity: O(log n)
5. Space Complexity: O(1)
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


def explain_search(nums: List[int], target: int) -> None:
    """
    Function to explain the search process step by step
    """
    print(f"\nSearching for {target} in {nums}")
    print("=" * 50)

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

        if nums[left] <= nums[mid]:
            print("Left half is sorted")
            if nums[left] <= target < nums[mid]:
                print(f"Target {target} lies in left sorted half")
                right = mid - 1
            else:
                print(f"Target {target} lies in right half")
                left = mid + 1
        else:
            print("Right half is sorted")
            if nums[mid] < target <= nums[right]:
                print(f"Target {target} lies in right sorted half")
                left = mid + 1
            else:
                print(f"Target {target} lies in left half")
                right = mid - 1

        step += 1

    print("\nTarget not found!")


def test_search():
    """
    Test function to verify the search solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 0,
            "expected": 4,
            "description": "Basic case with target in second half"
        },
        {
            "nums": [4, 5, 6, 7, 0, 1, 2],
            "target": 3,
            "expected": -1,
            "description": "Target not in array"
        },
        {
            "nums": [1],
            "target": 0,
            "expected": -1,
            "description": "Single element array, target not found"
        },
        {
            "nums": [1],
            "target": 1,
            "expected": 0,
            "description": "Single element array, target found"
        },
        {
            "nums": [3, 1],
            "target": 1,
            "expected": 1,
            "description": "Two elements, target in second position"
        },
        {
            "nums": [5, 1, 3],
            "target": 5,
            "expected": 0,
            "description": "Three elements, target at start"
        },
        {
            "nums": [4, 5, 6, 7, 8, 1, 2, 3],
            "target": 8,
            "expected": 4,
            "description": "Larger array, target at pivot-1"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: nums = {nums}, target = {target}")

        result = solution.search(nums, target)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_search()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with an example
        explain_search([4, 5, 6, 7, 0, 1, 2], 0)
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
