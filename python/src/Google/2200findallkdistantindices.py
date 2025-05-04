"""
LeetCode 2200 - Find All K-Distant Indices in an Array

Problem Statement:
You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an 
index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.
Return a list of all k-distant indices in nums sorted in increasing order.

Time Complexity: O(n*k) where n is length of nums
Space Complexity: O(n) for storing result set
"""


class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        """
        Logic:
        1. For each index j where nums[j] equals key:
           - Find all valid indices i where |i - j| <= k
           - These indices must be within array bounds
           - Add these indices to result set
        2. Convert set to sorted list and return

        Args:
            nums: List of integers
            key: Target value to find
            k: Maximum allowed distance
        Returns:
            Sorted list of k-distant indices
        """
        result = set()

        # Find all indices where nums[j] == key
        for j in range(len(nums)):
            if nums[j] == key:
                # Add all indices i where |i - j| <= k
                for i in range(max(0, j - k), min(len(nums), j + k + 1)):
                    result.add(i)

        # Return the sorted list of indices
        return sorted(result)


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'nums': [3, 4, 9, 1, 3, 9, 5],
            'key': 9,
            'k': 1,
            'expected': [1, 2, 3, 4, 5, 6]
        },
        {
            'nums': [2, 2, 2, 2, 2],
            'key': 2,
            'k': 2,
            'expected': [0, 1, 2, 3, 4]
        },
        {
            'nums': [1, 2, 3, 4, 5],
            'key': 6,
            'k': 1,
            'expected': []
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.findKDistantIndices(
            test['nums'], test['key'], test['k'])
        status = "PASSED" if result == test['expected'] else "FAILED"
        print(f"Test {i}: {status}")
        print(
            f"Input: nums = {test['nums']}, key = {test['key']}, k = {test['k']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}\n")


if __name__ == "__main__":
    main()
