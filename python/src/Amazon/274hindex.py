"""
LeetCode 274 - H-Index

Problem Statement:
Given an array of integers citations where citations[i] is the number of citations a researcher
received for their ith paper, return the researcher's h-index.

The h-index is defined as the maximum value of h such that the given researcher has published 
at least h papers that have each been cited at least h times.

Logic:
1. Sort the citations in descending order
2. Iterate through the sorted array
3. At each index i, if citations[i] >= i + 1, update h-index
4. When we find citations[i] < i + 1, we break as we can't get a larger h-index
"""

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break
        return h_index


def test_h_index():
    # Test cases
    test_cases = [
        ([3, 0, 6, 1, 5], 3),  # Example 1
        ([1, 3, 1], 1),        # Example 2
        ([0], 0),              # Single paper with no citations
        ([100], 1),            # Single paper with many citations
        ([], 0),               # Empty array
        ([10, 10, 10], 3)      # All papers with same citations
    ]
    
    solution = Solution()
    for i, (citations, expected) in enumerate(test_cases):
        result = solution.hIndex(citations)
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: citations={citations}, h-index={result}")

if __name__ == "__main__":
    test_h_index()
    print("All test cases passed!")
