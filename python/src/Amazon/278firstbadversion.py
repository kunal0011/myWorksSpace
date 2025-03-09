"""
LeetCode 278 - First Bad Version

Problem Statement:
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Logic:
1. Use binary search to minimize API calls
2. For each mid point:
   - If it's bad, look in left half (including mid)
   - If it's good, look in right half (after mid)
3. When left == right, we've found the first bad version
"""

def isBadVersion(version: int) -> bool:
    # Mock implementation for testing
    BAD_VERSION = 4  # First bad version for testing
    return version >= BAD_VERSION


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid  # The first bad version is at mid or before mid
            else:
                left = mid + 1  # The first bad version is after mid

        return left  # Or return right, as left == right


def test_first_bad_version():
    solution = Solution()
    
    # Test cases with different scenarios
    test_cases = [
        (5, 4),    # Bad versions: [4, 5]
        (1, 1),    # Single version, it's bad
        (10, 4),   # Multiple bad versions
    ]
    
    for i, (n, expected) in enumerate(test_cases):
        result = solution.firstBadVersion(n)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: n={n}, first bad version={result}")

if __name__ == "__main__":
    test_first_bad_version()
    print("All test cases passed!")
