"""
LeetCode 442: Find All Duplicates in an Array

Problem Statement:
Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

Constraints:
- n == nums.length
- 1 <= n <= 10^5
- 1 <= nums[i] <= n
- Each element in nums appears once or twice
"""


def findDuplicates(nums: list[int]) -> list[int]:
    result = []

    # Use array indices as hash table
    # Mark presence of number by making nums[num-1] negative
    for num in nums:
        # Get the absolute value since number might be marked negative
        index = abs(num) - 1
        if nums[index] > 0:
            # First occurrence: mark it negative
            nums[index] = -nums[index]
        else:
            # Second occurrence: already negative, so add to result
            result.append(abs(num))

    return result

# Test driver


def run_tests():
    test_cases = [
        {
            "nums": [4, 3, 2, 7, 8, 2, 3, 1],
            "expected": [2, 3],
            "explanation": "2 and 3 appear twice"
        },
        {
            "nums": [1, 1, 2],
            "expected": [1],
            "explanation": "1 appears twice"
        },
        {
            "nums": [1],
            "expected": [],
            "explanation": "No duplicates"
        },
        {
            "nums": [1, 2, 3, 4, 5, 6, 7, 8],
            "expected": [],
            "explanation": "All numbers appear once"
        },
        {
            "nums": [1, 1, 2, 2, 3, 3, 4, 4],
            "expected": [1, 2, 3, 4],
            "explanation": "All numbers appear twice"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        # Make a copy of input array as it will be modified
        nums = test["nums"].copy()
        result = findDuplicates(nums)
        # Sort results for consistent comparison
        result.sort()
        expected = sorted(test["expected"])
        status = "PASSED" if result == expected else "FAILED"

        print(f"Test {i}: {status}")
        print(f"Input array: {test['nums']}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Find All Duplicates in an Array problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Key Insight:
   - Given constraints: numbers are from 1 to n
   - We can use array indices as a hash table
   - Each number can be mapped to index (num-1)

2. Algorithm Steps:
   - For each number num in array:
     * Calculate index = abs(num) - 1
     * If nums[index] is positive:
       - First occurrence, mark it negative
     * If nums[index] is negative:
       - Second occurrence, add abs(num) to result

3. Time and Space Complexity:
   - Time: O(n) - single pass through array
   - Space: O(1) - modifies input array in-place
   - Additional space only used for output array

Note: This solution modifies the input array but meets the O(1) space requirement.
The array can be restored if needed by taking absolute values of all elements.
"""
