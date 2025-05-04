"""
LeetCode 2007. Find Original Array From Doubled Array

Problem Statement:
An integer array original is transformed into a doubled array changed by appending twice the value 
of every element in original, and then randomly shuffling the resulting array. Given an array changed, 
return original if changed is a doubled array. If changed is not a doubled array, return an empty array. 
The elements in original may be returned in any order.

Time Complexity: O(nlogn) where n is length of array
Space Complexity: O(n) for frequency map and result array
"""

from collections import Counter
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # Logic:
        # 1. If length is odd, can't be a doubled array
        # 2. Sort the array to process smaller numbers first
        # 3. Use frequency map to track available numbers
        # 4. For each number x:
        #    - If x is used (freq=0), skip
        #    - If 2x doesn't exist or used up, invalid
        #    - Add x to original, decrease freq of x and 2x
        # 5. Return original array if valid

        if len(changed) % 2 != 0:
            return []

        changed.sort()
        freq_map = Counter(changed)
        original = []

        for x in changed:
            if freq_map[x] == 0:
                continue
            if freq_map[2 * x] == 0:
                return []

            original.append(x)
            freq_map[x] -= 1
            freq_map[2 * x] -= 1

        return original


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [1, 3, 4, 2, 6, 8],           # Expected: [1,3,4]
        [6, 3, 0, 1],               # Expected: []
        [1],                     # Expected: []
        [2, 1],                   # Expected: [1]
        [0, 0, 0, 0],              # Expected: [0,0]
        [4, 4, 16, 16, 2, 2, 8, 8]     # Expected: [2,2,4,4]
    ]

    for i, changed in enumerate(test_cases):
        result = solution.findOriginalArray(changed)
        print(f"Test case {i + 1}:")
        print(f"Input array: {changed}")
        print(f"Original array: {result}")

        # Verify the result
        if result:
            # Create doubled array from result
            doubled = []
            for x in result:
                doubled.extend([x, 2*x])
            doubled.sort()
            changed.sort()
            print(f"Verification:")
            print(f"Sorted input: {changed}")
            print(f"Doubled result: {doubled}")
            print(f"Valid: {doubled == changed}")
        print()
