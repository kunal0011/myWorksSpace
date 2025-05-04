"""
LeetCode 1090: Largest Values From Labels

Problem Statement:
There is a set of n items. You are given two integer arrays values and labels where the ith value and the ith label
denote the value and the label of the ith item. You are also given two integers numWanted and useLimit.
Choose a subset of the n items such that:
- The size of the subset is less than or equal to numWanted.
- For each label L, the number of items in the subset with label L is less than or equal to useLimit.
Return the largest possible sum of the subset.

Logic:
1. Sort items by value in descending order (to get largest values first)
2. Use defaultdict to track count of each label used
3. Iterate through sorted items:
   - If label count < useLimit, add value to total
   - Track total items selected
   - Stop when numWanted items are selected
4. Return total sum

Time Complexity: O(nlogn) for sorting
Space Complexity: O(n) for storing sorted items and label counts
"""

from collections import defaultdict
from typing import List


class Solution:
    def largestValsFromLabels(self, values: list[int], labels: list[int], numWanted: int, useLimit: int) -> int:
        items = sorted(zip(values, labels), reverse=True)
        label_count = defaultdict(int)
        total_value = 0
        count = 0

        for value, label in items:
            if label_count[label] < useLimit:
                total_value += value
                label_count[label] += 1
                count += 1
                if count == numWanted:
                    break

        return total_value


def test_largest_vals_from_labels():
    solution = Solution()

    # Test case 1: Basic case
    values1 = [5, 4, 3, 2, 1]
    labels1 = [1, 1, 2, 2, 3]
    result1 = solution.largestValsFromLabels(values1, labels1, 3, 1)
    assert result1 == 9, f"Test case 1 failed. Expected 9, got {result1}"
    print(f"Test case 1 passed: sum = {result1}")

    # Test case 2: Multiple items with same label
    values2 = [5, 4, 3, 2, 1]
    labels2 = [1, 3, 3, 3, 2]
    result2 = solution.largestValsFromLabels(values2, labels2, 3, 2)
    assert result2 == 12, f"Test case 2 failed. Expected 12, got {result2}"
    print(f"\nTest case 2 passed: sum = {result2}")

    # Test case 3: useLimit restricts selection
    values3 = [9, 8, 8, 7, 6]
    labels3 = [0, 0, 0, 1, 1]
    result3 = solution.largestValsFromLabels(values3, labels3, 3, 1)
    assert result3 == 24, f"Test case 3 failed. Expected 24, got {result3}"
    print(f"\nTest case 3 passed: sum = {result3}")

    # Test case 4: numWanted larger than possible selections
    values4 = [2, 2, 2, 2, 2]
    labels4 = [2, 2, 2, 2, 2]
    result4 = solution.largestValsFromLabels(values4, labels4, 5, 2)
    assert result4 == 4, f"Test case 4 failed. Expected 4, got {result4}"
    print(f"\nTest case 4 passed: sum = {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_largest_vals_from_labels()
