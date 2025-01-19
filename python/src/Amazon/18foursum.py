from typing import List

"""
LeetCode 18. 4Sum

Problem Statement:
Given an array nums of n integers and an integer target, find all unique quadruplets 
in the array that sum to target.

The solution set must not contain duplicate quadruplets.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
- 1 <= nums.length <= 200
- -109 <= nums[i] <= 109
- -109 <= target <= 109

Approach:
1. Sort the array first to handle duplicates and use two pointers
2. Use two loops to fix first two numbers
3. Use two pointers for remaining two numbers
4. Skip duplicates at each level to avoid duplicate quadruplets
5. Time Complexity: O(n³)
6. Space Complexity: O(1) excluding output space
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Sort the array to handle duplicates and use two pointers
        n = len(nums)
        result = []

        for i in range(n - 3):
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicates for j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Use two pointers for the remaining two numbers
                left = j + 1
                right = n - 1

                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if curr_sum == target:
                        result.append(
                            [nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicates for left
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for right
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1

        return result


def test_four_sum():
    """
    Test function to verify the fourSum solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "nums": [1, 0, -1, 0, -2, 2],
            "target": 0,
            "expected": [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
            "description": "Standard case with multiple solutions"
        },
        {
            "nums": [2, 2, 2, 2, 2],
            "target": 8,
            "expected": [[2, 2, 2, 2]],
            "description": "All same numbers"
        },
        {
            "nums": [0, 0, 0, 0],
            "target": 0,
            "expected": [[0, 0, 0, 0]],
            "description": "All zeros"
        },
        {
            "nums": [-3, -2, -1, 0, 0, 1, 2, 3],
            "target": 0,
            "expected": [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2],
                         [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
            "description": "Mix of positive and negative numbers"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        target = test_case["target"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: nums={nums}, target={target}")

        result = solution.fourSum(nums, target)

        # Sort the lists for comparison
        result = sorted(result)
        expected = sorted(expected)

        assert result == expected, f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_four_sum()
        print("\nAll test cases passed successfully! 🎉")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
