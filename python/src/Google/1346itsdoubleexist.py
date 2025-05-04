"""
LeetCode 1346: Check If N and Its Double Exist

Problem Statement:
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]

Logic:
1. Use HashSet to store seen numbers
2. For each number x in array:
   - Check if 2*x exists in set
   - If x is even, check if x/2 exists in set
   - Add x to set
3. Return True if found, False otherwise

Time Complexity: O(n)
Space Complexity: O(n)
"""


class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        seen = set()

        for x in arr:
            if 2 * x in seen or (x % 2 == 0 and x // 2 in seen):
                return True
            seen.add(x)

        return False


def test_check_if_exist():
    solution = Solution()

    # Test case 1: Basic case with double
    arr1 = [10, 2, 5, 3]
    result1 = solution.checkIfExist(arr1)
    assert result1 == True, f"Test case 1 failed. Expected True, got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: No doubles
    arr2 = [3, 1, 7, 11]
    result2 = solution.checkIfExist(arr2)
    assert result2 == False, f"Test case 2 failed. Expected False, got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Array with zeros
    arr3 = [7, 1, 14, 11]
    result3 = solution.checkIfExist(arr3)
    assert result3 == True, f"Test case 3 failed. Expected True, got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Empty array
    arr4 = []
    result4 = solution.checkIfExist(arr4)
    assert result4 == False, f"Test case 4 failed. Expected False, got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    # Test case 5: Multiple zeros
    arr5 = [0, 0]
    result5 = solution.checkIfExist(arr5)
    assert result5 == True, f"Test case 5 failed. Expected True, got {result5}"
    print(f"\nTest case 5 passed: {result5}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_check_if_exist()
