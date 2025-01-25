from typing import List

"""
LeetCode 53. Maximum Subarray

Problem Statement:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize current sum and maximum sum
        current_sum = max_sum = nums[0]

        # Track the start and end indices of the maximum subarray
        start = end = current_start = 0

        # Iterate through the array starting from second element
        for i in range(1, len(nums)):
            # If current_sum becomes negative, start fresh from current element
            if current_sum < 0:
                current_sum = nums[i]
                current_start = i
            else:
                current_sum += nums[i]

            # Update maximum sum if current sum is larger
            if current_sum > max_sum:
                max_sum = current_sum
                start = current_start
                end = i

        return max_sum, start, end


def explain_max_subarray(nums: List[int]) -> None:
    """
    Function to explain the maximum subarray finding process step by step
    """
    print(f"\nFinding maximum subarray in: {nums}")
    print("=" * 50)

    current_sum = max_sum = nums[0]
    start = end = current_start = 0

    print(f"Initial state:")
    print(f"Current sum: {current_sum}")
    print(f"Max sum: {max_sum}")
    print(f"Current subarray: {nums[current_start:1]}\n")

    for i in range(1, len(nums)):
        prev_sum = current_sum

        if current_sum < 0:
            current_sum = nums[i]
            current_start = i
            print(f"Current sum negative, starting fresh at index {i}")
        else:
            current_sum += nums[i]
            print(f"Adding nums[{i}] = {nums[i]} to current sum")

        print(f"Index {i}: {nums[i]}")
        print(f"Previous sum: {prev_sum} -> New sum: {current_sum}")
        print(f"Current subarray: {nums[current_start:i+1]}")

        if current_sum > max_sum:
            max_sum = current_sum
            start = current_start
            end = i
            print(f"New maximum sum found: {max_sum}")
            print(f"Maximum subarray: {nums[start:end+1]}\n")
        else:
            print("No new maximum found\n")

    print(f"Final result:")
    print(f"Maximum sum: {max_sum}")
    print(f"Maximum subarray: {nums[start:end+1]}")
    print(f"Start index: {start}")
    print(f"End index: {end}")


def test_max_subarray():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
            "expected": 6,
            "description": "Basic case with negative numbers"
        },
        {
            "nums": [1],
            "expected": 1,
            "description": "Single element"
        },
        {
            "nums": [5, 4, -1, 7, 8],
            "expected": 23,
            "description": "All positive except one"
        },
        {
            "nums": [-1, -2, -3, -4],
            "expected": -1,
            "description": "All negative numbers"
        },
        {
            "nums": [1, 2, 3, 4],
            "expected": 10,
            "description": "All positive numbers"
        },
        {
            "nums": [-2, 1],
            "expected": 1,
            "description": "Two elements"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        nums = test_case["nums"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: nums = {nums}")

        max_sum, start, end = solution.maxSubArray(nums.copy())

        assert max_sum == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {max_sum}"
        print(f"✓ Test case {i} passed!")
        print(f"Maximum sum: {max_sum}")
        print(f"Maximum subarray: {nums[start:end+1]}")


if __name__ == "__main__":
    try:
        test_max_subarray()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        explain_max_subarray([5, 4, -1, 7, 8])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
