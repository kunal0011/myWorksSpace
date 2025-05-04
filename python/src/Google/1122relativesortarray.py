"""
LeetCode 1122: Relative Sort Array

Problem Statement:
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Logic:
1. Use Counter to count occurrences of elements in arr1
2. Iterate through arr2:
   - For each number, add it to result list count[num] times
   - Remove processed numbers from Counter
3. Sort remaining numbers (not in arr2) and append to result
4. Return final sorted array

Time Complexity: O(nlogn) where n is length of remaining elements not in arr2
Space Complexity: O(n) for storing counts and result array
"""

from collections import Counter


class Solution:
    def relativeSortArray(self, arr1, arr2):
        # Step 1: Count the occurrences of each element in arr1
        count = Counter(arr1)
        result = []

        # Step 2: Place elements from arr2 in the correct order
        for num in arr2:
            if num in count:
                result.extend([num] * count[num])
                del count[num]

        # Step 3: Sort remaining elements and append them
        remaining = sorted(count.elements())
        result.extend(remaining)

        return result


def test_relative_sort():
    solution = Solution()

    # Test case 1: Basic case
    arr1_1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2_1 = [2, 1, 4, 3, 9, 6]
    result1 = solution.relativeSortArray(arr1_1, arr2_1)
    expected1 = [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    assert result1 == expected1, f"Test case 1 failed. Expected {expected1}, got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: All elements in arr2
    arr1_2 = [1, 2, 3, 4]
    arr2_2 = [2, 4, 1, 3]
    result2 = solution.relativeSortArray(arr1_2, arr2_2)
    expected2 = [2, 4, 1, 3]
    assert result2 == expected2, f"Test case 2 failed. Expected {expected2}, got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Some elements not in arr2
    arr1_3 = [28, 6, 22, 8, 44, 17]
    arr2_3 = [22, 28, 8, 6]
    result3 = solution.relativeSortArray(arr1_3, arr2_3)
    expected3 = [22, 28, 8, 6, 17, 44]
    assert result3 == expected3, f"Test case 3 failed. Expected {expected3}, got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_relative_sort()
