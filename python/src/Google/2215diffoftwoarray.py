"""
LeetCode 2215 - Find the Difference of Two Arrays

Problem Statement:
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
- answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
- answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
The integers in the lists may be returned in any order.

Time Complexity: O(n + m) where n and m are lengths of nums1 and nums2
Space Complexity: O(n + m) for storing sets
"""


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        """
        Logic:
        1. Convert both input arrays to sets for O(1) lookup
        2. Use set difference operation to find:
           - Elements in nums1 but not in nums2
           - Elements in nums2 but not in nums1
        3. Convert results back to lists and return

        Args:
            nums1: First list of integers
            nums2: Second list of integers
        Returns:
            List containing two lists of distinct integers
        """
        # Convert both lists to sets to get unique elements
        set1 = set(nums1)
        set2 = set(nums2)

        # Find elements in set1 but not in set2
        distinct_nums1 = list(set1 - set2)

        # Find elements in set2 but not in set1
        distinct_nums2 = list(set2 - set1)

        # Return the result as a list of two lists
        return [distinct_nums1, distinct_nums2]


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'nums1': [1, 2, 3],
            'nums2': [2, 4, 6],
            'expected': [[1, 3], [4, 6]]
        },
        {
            'nums1': [1, 2, 3, 3],
            'nums2': [1, 1, 2, 2],
            'expected': [[3], []]
        },
        {
            'nums1': [1, 2, 3, 4, 5],
            'nums2': [6, 7, 8, 9, 10],
            'expected': [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.findDifference(test['nums1'], test['nums2'])
        # Sort lists for consistent comparison
        result = [sorted(x) for x in result]
        expected = [sorted(x) for x in test['expected']]
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: nums1 = {test['nums1']}, nums2 = {test['nums2']}")
        print(f"Output: {result}")
        print(f"Expected: {expected}\n")


if __name__ == "__main__":
    main()
