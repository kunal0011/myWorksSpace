"""
LeetCode 2022. Convert 1D Array Into 2D Array

Problem Statement:
You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. 
You are tasked with creating a 2-dimensional (2D) array with m rows and n columns using all the 
elements from original. The elements from indices 0 to n - 1 (inclusive) of original should form 
the first row of the constructed 2D array, the elements from indices n to 2n - 1 (inclusive) should 
form the second row of the constructed 2D array, and so on.
Return the resulting array. If it's impossible to construct such array, return an empty array.

Time Complexity: O(m*n) where m and n are dimensions of the output array
Space Complexity: O(m*n) for storing the result array
"""

from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Logic:
        # 1. Check if total elements match m*n, if not return empty array
        # 2. Use array slicing to create rows:
        #    - Start from 0, step by n
        #    - Each slice becomes a row of length n
        # 3. Return resulting 2D array

        if m * n != len(original):
            return []

        result = []
        for i in range(0, len(original), n):
            result.append(original[i:i + n])

        return result


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ([1, 2, 3, 4], 2, 2),              # Expected: [[1,2],[3,4]]
        ([1, 2, 3], 1, 3),                # Expected: [[1,2,3]]
        ([1, 2], 1, 1),                  # Expected: [] (impossible)
        ([1, 2, 3, 4, 5, 6], 2, 3),          # Expected: [[1,2,3],[4,5,6]]
        # Expected: [[1,2],[3,4],[5,6],[7,8]]
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, 2)
    ]

    for i, (original, m, n) in enumerate(test_cases):
        result = solution.construct2DArray(original, m, n)
        print(f"Test case {i + 1}:")
        print(f"Original array: {original}")
        print(f"Target dimensions: {m}x{n}")
        print(f"Result array:")
        if result:
            for row in result:
                print(row)
        else:
            print("Empty array (impossible to construct)")

        # Verify dimensions and elements
        if result:
            print("Verification:")
            print(f"Expected dimensions: {m}x{n}")
            print(f"Actual dimensions: {len(result)}x{len(result[0])}")
            # Flatten result and compare with original
            flattened = [num for row in result for num in row]
            print(f"Elements match original: {flattened == original}")
        print()
