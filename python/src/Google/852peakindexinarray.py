"""
LeetCode 852: Peak Index in a Mountain Array

Problem Statement:
An array arr is a mountain array if the following properties hold:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
  * arr[0] < arr[1] < ... < arr[i-1] < arr[i]
  * arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Return the index i such that arr[i] is the peak element.

Logic:
1. Use binary search to find the peak efficiently
2. For any middle element:
   - If mid element < next element: peak is to the right
   - If mid element > next element: peak is to the left or at mid
3. When low and high converge, we've found the peak

Time Complexity: O(log n) using binary search
Space Complexity: O(1) constant space
"""

from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1

        while low < high:
            mid = (low + high) // 2
            if arr[mid] < arr[mid + 1]:
                # Peak is to the right of mid
                low = mid + 1
            else:
                # Peak is to the left of mid, or it is mid
                high = mid

        return low


def test_peak_index():
    solution = Solution()

    # Test case 1: Basic mountain array
    arr1 = [0, 2, 4, 7, 6, 3, 1]
    result1 = solution.peakIndexInMountainArray(arr1)
    assert result1 == 3, f"Test case 1 failed. Expected 3, got {result1}"
    print(f"Test case 1 passed: arr={arr1}, peak_index={result1}")

    # Test case 2: Peak at end of ascending
    arr2 = [0, 1, 2, 3, 4, 1]
    result2 = solution.peakIndexInMountainArray(arr2)
    assert result2 == 4, f"Test case 2 failed. Expected 4, got {result2}"
    print(f"\nTest case 2 passed: arr={arr2}, peak_index={result2}")

    # Test case 3: Peak at start of descending
    arr3 = [0, 10, 8, 6, 4, 2]
    result3 = solution.peakIndexInMountainArray(arr3)
    assert result3 == 1, f"Test case 3 failed. Expected 1, got {result3}"
    print(f"\nTest case 3 passed: arr={arr3}, peak_index={result3}")

    # Test case 4: Minimum length mountain
    arr4 = [1, 2, 1]
    result4 = solution.peakIndexInMountainArray(arr4)
    assert result4 == 1, f"Test case 4 failed. Expected 1, got {result4}"
    print(f"\nTest case 4 passed: arr={arr4}, peak_index={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_peak_index()
