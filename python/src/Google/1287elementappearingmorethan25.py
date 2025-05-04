"""
LeetCode 1287: Element Appearing More Than 25% In Sorted Array

Problem Statement:
Given a sorted array arr of integers, find the integer that appears more than 25% of the time.
Return any integer that appears more than n/4 times in the array, where n is the array length.

Logic:
1. Since array is sorted, if an element appears >25%, it must appear consecutively
2. Use sliding window approach:
   - Count consecutive occurrences of each element
   - If count exceeds n/4, we found our answer
3. Linear scan is sufficient due to sorted property

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        threshold = n // 4

        # Iterate through the array and check for frequency
        i = 0
        while i < n:
            count = 1
            # Count the number of times arr[i] appears consecutively
            while i + 1 < n and arr[i] == arr[i + 1]:
                count += 1
                i += 1

            if count > threshold:
                return arr[i]

            i += 1

        return -1


def test_find_special_integer():
    solution = Solution()

    # Test case 1: Basic case
    arr1 = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    result1 = solution.findSpecialInteger(arr1)
    assert result1 == 6, f"Test case 1 failed. Expected 6, got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: Element at start
    arr2 = [1, 1, 1, 1, 2, 3, 4, 5]
    result2 = solution.findSpecialInteger(arr2)
    assert result2 == 1, f"Test case 2 failed. Expected 1, got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Element at end
    arr3 = [1, 2, 3, 4, 4, 4, 4]
    result3 = solution.findSpecialInteger(arr3)
    assert result3 == 4, f"Test case 3 failed. Expected 4, got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Single element array
    arr4 = [1]
    result4 = solution.findSpecialInteger(arr4)
    assert result4 == 1, f"Test case 4 failed. Expected 1, got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_find_special_integer()
