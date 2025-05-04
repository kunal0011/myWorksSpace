"""
LeetCode 1331: Rank Transform of an Array

Problem Statement:
Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
- Rank is an integer starting from 1
- The larger the element, the larger the rank
- If two elements are equal, their rank must be the same
- Rank should be as small as possible

Logic:
1. Create set of unique elements and sort them
2. Create rank map using enumeration:
   - Each unique element maps to its position + 1
   - This ensures equal elements get same rank
3. Transform original array using rank map

Time Complexity: O(nlogn) for sorting
Space Complexity: O(n) for rank map
"""


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        # Step 1: Sort the unique elements
        sorted_unique = sorted(set(arr))

        # Step 2: Create a rank map (element -> rank)
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique)}

        # Step 3: Replace each element with its rank
        return [rank_map[num] for num in arr]


def test_array_rank_transform():
    solution = Solution()

    # Test case 1: Basic array
    arr1 = [40, 10, 20, 30]
    result1 = solution.arrayRankTransform(arr1)
    expected1 = [4, 1, 2, 3]
    assert result1 == expected1, f"Test case 1 failed. Expected {expected1}, got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: Array with duplicates
    arr2 = [100, 100, 100]
    result2 = solution.arrayRankTransform(arr2)
    expected2 = [1, 1, 1]
    assert result2 == expected2, f"Test case 2 failed. Expected {expected2}, got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Empty array
    arr3 = []
    result3 = solution.arrayRankTransform(arr3)
    assert result3 == [], f"Test case 3 failed. Expected [], got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Negative numbers
    arr4 = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    result4 = solution.arrayRankTransform(arr4)
    expected4 = [5, 3, 4, 2, 8, 6, 7, 1, 3]
    assert result4 == expected4, f"Test case 4 failed. Expected {expected4}, got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_array_rank_transform()
