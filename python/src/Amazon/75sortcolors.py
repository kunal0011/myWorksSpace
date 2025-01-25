"""
LeetCode 75. Sort Colors

Problem Statement:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects
of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:
- n == nums.length
- 1 <= n <= 300
- nums[i] is either 0, 1, or 2
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Dutch National Flag algorithm
        """
        # Initialize pointers
        left = curr = 0  # left pointer for 0s
        right = len(nums) - 1  # right pointer for 2s

        while curr <= right:
            if nums[curr] == 0:
                # Swap with left pointer and move both pointers
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] == 2:
                # Swap with right pointer and only move right pointer
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                # Current element is 1, just move current pointer
                curr += 1


def print_array_with_pointers(nums: list[int], left: int = None, curr: int = None,
                              right: int = None) -> None:
    """Helper function to print array with pointers"""
    print("\nArray state:", end=" ")
    for i in range(len(nums)):
        # Add pointer indicators
        pointers = []
        if i == left:
            pointers.append("l")
        if i == curr:
            pointers.append("c")
        if i == right:
            pointers.append("r")

        # Print number with pointers
        if pointers:
            print(f"{nums[i]}({','.join(pointers)})", end=" ")
        else:
            print(nums[i], end=" ")
    print()


def explain_sort_colors(nums: list[int]) -> None:
    """
    Function to explain the Dutch National Flag sorting process step by step
    """
    print("\nSorting colors using Dutch National Flag algorithm")
    print("=" * 50)
    print("0 = Red, 1 = White, 2 = Blue")

    # Create a copy for demonstration
    nums_copy = nums.copy()
    left = curr = 0
    right = len(nums) - 1

    print("\nInitial array:")
    print_array_with_pointers(nums_copy, left, curr, right)

    iteration = 1
    while curr <= right:
        print(f"\nIteration {iteration}:")
        print(f"Current element (at {curr}): {nums_copy[curr]}")

        if nums_copy[curr] == 0:
            print(f"Found 0 (Red) at position {curr}")
            print(f"Swapping with left pointer at position {left}")
            nums_copy[left], nums_copy[curr] = nums_copy[curr], nums_copy[left]
            left += 1
            curr += 1
        elif nums_copy[curr] == 2:
            print(f"Found 2 (Blue) at position {curr}")
            print(f"Swapping with right pointer at position {right}")
            nums_copy[curr], nums_copy[right] = nums_copy[right], nums_copy[curr]
            right -= 1
        else:
            print(
                f"Found 1 (White) at position {curr}, moving current pointer")
            curr += 1

        print_array_with_pointers(nums_copy, left, curr, right)
        iteration += 1

    print("\nFinal sorted array:")
    print(nums_copy)


def test_sort_colors():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "nums": [2, 0, 2, 1, 1, 0],
            "expected": [0, 0, 1, 1, 2, 2],
            "description": "Standard case"
        },
        {
            "nums": [2, 0, 1],
            "expected": [0, 1, 2],
            "description": "Three different colors"
        },
        {
            "nums": [0],
            "expected": [0],
            "description": "Single element"
        },
        {
            "nums": [1, 1, 1, 1],
            "expected": [1, 1, 1, 1],
            "description": "All same color"
        },
        {
            "nums": [2, 2, 1, 1, 0, 0],
            "expected": [0, 0, 1, 1, 2, 2],
            "description": "Already grouped"
        },
        {
            "nums": [1, 2, 0, 1, 2, 0],
            "expected": [0, 0, 1, 1, 2, 2],
            "description": "Mixed colors"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"].copy()
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: {nums}")

        solution.sortColors(nums)

        assert nums == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {nums}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_sort_colors()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_sort_colors([2, 0, 2, 1, 1, 0])
        explain_sort_colors([2, 0, 1])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
