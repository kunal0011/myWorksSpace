"""
LeetCode 944: Delete Columns to Make Sorted

Problem Statement:
You are given an array of n strings strs, all of the same length.
The strings can be arranged such that there is one on each line, forming a grid.
For example, strs = ["abc", "bce", "cae"] can be arranged as:
abc
bce
cae
You want to delete the columns that are not sorted lexicographically.
Return the number of columns that you will delete.

Logic:
1. For each column in the grid:
   - Check if characters in that column are sorted
   - If any character is less than previous character, column needs deletion
2. Count number of columns that need deletion
3. We only need to compare adjacent characters in each column

Time Complexity: O(n*m) where n is number of strings and m is length of each string
Space Complexity: O(1) as we only use constant extra space
"""

from typing import List

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        num_columns = len(strs[0])
        num_deletions = 0

        # Check each column
        for col in range(num_columns):
            for row in range(1, len(strs)):
                # If the current column is not sorted, mark the column for deletion
                if strs[row][col] < strs[row - 1][col]:
                    num_deletions += 1
                    break

        return num_deletions

def test_min_deletion_size():
    solution = Solution()
    
    # Test case 1: Basic case
    strs1 = ["cba","daf","ghi"]
    result1 = solution.minDeletionSize(strs1)
    assert result1 == 1, f"Test case 1 failed. Expected 1, got {result1}"
    print(f"Test case 1 passed: strs={strs1}, deletions={result1}")
    
    # Test case 2: No deletions needed
    strs2 = ["abc", "bcd", "cde"]
    result2 = solution.minDeletionSize(strs2)
    assert result2 == 0, f"Test case 2 failed. Expected 0, got {result2}"
    print(f"\nTest case 2 passed: strs={strs2}, deletions={result2}")
    
    # Test case 3: All columns need deletion
    strs3 = ["zyx","wvu","tsr"]
    result3 = solution.minDeletionSize(strs3)
    assert result3 == 3, f"Test case 3 failed. Expected 3, got {result3}"
    print(f"\nTest case 3 passed: strs={strs3}, deletions={result3}")
    
    # Test case 4: Single character strings
    strs4 = ["a","b","c"]
    result4 = solution.minDeletionSize(strs4)
    assert result4 == 0, f"Test case 4 failed. Expected 0, got {result4}"
    print(f"\nTest case 4 passed: strs={strs4}, deletions={result4}")
    
    print("\nAll test cases passed!")

if __name__ == "__main__":
    test_min_deletion_size()
