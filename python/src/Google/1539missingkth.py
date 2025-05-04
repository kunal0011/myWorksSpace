"""
LeetCode 1539. Kth Missing Positive Number

Problem Statement:
Given an array arr of positive integers sorted in strictly increasing order, and an integer k.
Find the kth positive integer that is missing from this array.

Time Complexity: O(n) for linear scan approach, O(log n) for binary search approach
Space Complexity: O(1) as we only use constant extra space
"""

from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Logic:
        # 1. Keep track of current number and array index
        # 2. For each number from 1 onwards:
        #    - If number is missing (not equal to arr[idx]), increment missing count
        #    - If number is present, move to next array element
        #    - When kth missing number is found, return it
        # 3. Handle case where k is larger than missing numbers in array range

        # Start checking from 1
        missing_count = 0
        current = 1
        idx = 0

        # Iterate while we haven't found the kth missing number
        while k > 0:
            # If the current number is not in the array, it's missing
            if idx >= len(arr) or arr[idx] != current:
                missing_count += 1
                # If this is the kth missing number, return it
                if missing_count == k:
                    return current
            else:
                idx += 1
            current += 1

        # Return the kth missing positive number
        return current


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([2, 3, 4, 7, 11], 5),    # Expected: 9
        ([1, 2, 3, 4], 2),       # Expected: 6
        ([2, 3, 4, 7, 11], 1),    # Expected: 1
        ([1, 2, 3, 4], 5),       # Expected: 9
        ([5, 6, 8, 9, 10], 3)     # Expected: 3
    ]

    for i, (arr, k) in enumerate(test_cases):
        result = solution.findKthPositive(arr, k)
        print(f"Test case {i + 1}:")
        print(f"Array: {arr}")
        print(f"k: {k}")
        print(f"Kth missing positive number: {result}")

        # Print all missing numbers up to result for verification
        missing = []
        j = 0
        for num in range(1, result + 1):
            if j < len(arr) and arr[j] == num:
                j += 1
            else:
                missing.append(num)
        print(f"Missing numbers up to result: {missing}")
        print()
