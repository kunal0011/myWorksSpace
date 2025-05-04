"""
LeetCode 1200: Minimum Absolute Difference

Problem Statement:
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference
of any two elements. Return a list of pairs in ascending order(with respect to pairs), each pair [a,b] follows:
- a, b are from arr
- a < b
- b - a equals to the minimum absolute difference of any two elements in arr

Logic:
1. Sort the array to make adjacent elements closest to each other
2. Find minimum difference by comparing adjacent elements
3. Collect all pairs that have this minimum difference
4. Return pairs in sorted order (automatically achieved due to initial sort)

Time Complexity: O(nlogn) for sorting
Space Complexity: O(k) where k is number of pairs with minimum difference
"""


class Solution:
    def minimumAbsDifference(self, arr):
        # Step 1: Sort the array
        arr.sort()

        # Step 2: Find the minimum absolute difference
        min_diff = float('inf')
        for i in range(1, len(arr)):
            min_diff = min(min_diff, arr[i] - arr[i-1])

        # Step 3: Collect all pairs with the minimum difference
        result = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_diff:
                result.append([arr[i-1], arr[i]])

        return result


def test_minimum_abs_difference():
    solution = Solution()

    # Test case 1: Basic case
    arr1 = [4, 2, 1, 3]
    result1 = solution.minimumAbsDifference(arr1)
    assert result1 == [[1, 2], [2, 3], [
        3, 4]], f"Test case 1 failed. Expected [[1,2],[2,3],[3,4]], got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: Negative numbers
    arr2 = [3, 8, -10, 23, 19, -4, -14, 27]
    result2 = solution.minimumAbsDifference(arr2)
    assert result2 == [[-14, -10], [19, 23], [23, 27]
                       ], f"Test case 2 failed. Expected [[-14,-10],[19,23],[23,27]], got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Single minimum difference
    arr3 = [1, 3, 6, 10, 15]
    result3 = solution.minimumAbsDifference(arr3)
    assert result3 == [
        [1, 3]], f"Test case 3 failed. Expected [[1,3]], got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: All equal differences
    arr4 = [1, 2, 3, 4]
    result4 = solution.minimumAbsDifference(arr4)
    assert result4 == [[1, 2], [2, 3], [
        3, 4]], f"Test case 4 failed. Expected [[1,2],[2,3],[3,4]], got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_minimum_abs_difference()
