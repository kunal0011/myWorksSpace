"""
Problem 15: 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
- nums[0] + nums[2] + nums[4] = (-1) + 1 + (-1) = -1
- nums[1] + nums[2] + nums[3] = 0 + 1 + 2 = 3

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Logic:
1. Sort the array first (helps in skipping duplicates and efficient search)
2. Iterate through array with first pointer (i)
3. Use two pointers (left and right) for remaining elements
4. Skip duplicates at all three positions to avoid duplicate triplets
5. Move pointers based on sum comparison with 0

Time Complexity: O(n²) - one loop and two pointers
Space Complexity: O(1) - excluding the space needed for output
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort array to handle duplicates and for two-pointer technique
        nums.sort()
        result = []
        n = len(nums)

        # Iterate through array for first number
        for i in range(n - 2):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers for remaining elements
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    # Found a triplet
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif current_sum < 0:
                    # Sum too small, increase left pointer
                    left += 1
                else:
                    # Sum too large, decrease right pointer
                    right -= 1

        return result


def test_three_sum():
    solution = Solution()

    # Test cases: (input_array, expected_result, description)
    test_cases = [
        (
            [-1, 0, 1, 2, -1, -4],
            [[-1, -1, 2], [-1, 0, 1]],
            "Standard case with multiple solutions"
        ),
        (
            [0, 0, 0],
            [[0, 0, 0]],
            "All zeros"
        ),
        (
            [],
            [],
            "Empty array"
        ),
        (
            [1, 2, -2, -1],
            [],
            "No solutions"
        ),
        (
            [-2, 0, 1, 1, 2],
            [[-2, 0, 2], [-2, 1, 1]],
            "Multiple solutions with duplicates"
        ),
        (
            [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
            [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2],
             [-2, -2, 4], [-2, 0, 2], [-2, 1, 1]],
            "Complex case with many duplicates"
        )
    ]

    print("\nRunning 3Sum Tests:")
    print("=" * 50)

    passed = 0
    total = len(test_cases)

    for i, (nums, expected, desc) in enumerate(test_cases, 1):
        result = solution.threeSum(nums)
        # Sort both result and expected for comparison
        result_sorted = sorted([sorted(x) for x in result])
        expected_sorted = sorted([sorted(x) for x in expected])
        status = "PASS" if result_sorted == expected_sorted else "FAIL"
        color = "\033[92m" if status == "PASS" else "\033[91m"

        print(f"\nTest Case {i}: {desc}")
        print(f"Input Array: {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Status: {color}{status}\033[0m")

        if result_sorted == expected_sorted:
            passed += 1

    print("\n" + "=" * 50)
    print(f"\nTest Summary:")
    print(f"Total Tests: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    success_rate = (passed / total) * 100
    print(f"Success Rate: {success_rate:.2f}%")


def visualize_algorithm():
    """
    Demonstrates how the algorithm works with a simple example
    """
    example = [-1, 0, 1, 2, -1, -4]
    print("\nAlgorithm Visualization:")
    print("=" * 50)
    print(f"Original array: {example}")

    # Sort array
    sorted_array = sorted(example)
    print(f"Sorted array: {sorted_array}")

    print("\nStep-by-step process:")
    print("1. Iterate through array with first pointer (i)")
    print("2. For each i, use two pointers (left and right) for remaining elements")
    print("3. Compare sum with 0 and move pointers accordingly")
    print("4. Skip duplicates to avoid duplicate triplets")

    # Show example iteration
    print("\nExample iteration:")
    print(f"i = 0, num[i] = {sorted_array[0]}")
    print(f"left = 1, right = {len(sorted_array)-1}")
    print(f"Looking for sum = {-sorted_array[0]}")


if __name__ == "__main__":
    test_three_sum()
    print("\n")
    visualize_algorithm()
