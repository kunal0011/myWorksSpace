"""
LeetCode 1207: Unique Number of Occurrences

Problem Statement:
Given an array of integers arr, return true if the number of occurrences of each value in the array
is unique, or false otherwise. In other words, each value in the array should appear a unique number
of times.

Logic:
1. Use Counter to count occurrences of each element
2. Convert counts to a set to get unique frequencies
3. Compare lengths:
   - If lengths are equal, all frequencies are unique
   - If lengths differ, some frequencies are repeated
4. Return true if lengths match, false otherwise

Time Complexity: O(n) where n is length of array
Space Complexity: O(k) where k is number of unique elements
"""

from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr):
        # Step 1: Count the occurrences of each element in arr
        count = Counter(arr)

        # Step 2: Get the set of occurrences
        occurrences = set(count.values())

        # Step 3: Compare the length of occurrences with the length of the count dictionary
        return len(occurrences) == len(count)


def test_unique_occurrences():
    solution = Solution()

    # Test case 1: Basic case with unique occurrences
    arr1 = [1, 2, 2, 1, 1, 3]
    result1 = solution.uniqueOccurrences(arr1)
    assert result1 == True, f"Test case 1 failed. Expected True, got {result1}"
    print(f"Test case 1 passed: {arr1} -> {result1}")

    # Test case 2: Non-unique occurrences
    arr2 = [1, 2, 2, 1, 1, 3, 3]
    result2 = solution.uniqueOccurrences(arr2)
    assert result2 == False, f"Test case 2 failed. Expected False, got {result2}"
    print(f"\nTest case 2 passed: {arr2} -> {result2}")

    # Test case 3: Single element
    arr3 = [1]
    result3 = solution.uniqueOccurrences(arr3)
    assert result3 == True, f"Test case 3 failed. Expected True, got {result3}"
    print(f"\nTest case 3 passed: {arr3} -> {result3}")

    # Test case 4: Negative numbers
    arr4 = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    result4 = solution.uniqueOccurrences(arr4)
    assert result4 == True, f"Test case 4 failed. Expected True, got {result4}"
    print(f"\nTest case 4 passed: {arr4} -> {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_unique_occurrences()
