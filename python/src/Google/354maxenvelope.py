"""
LeetCode 354 - Russian Doll Envelopes

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the 
width and height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope 
are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Example:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
"""

from bisect import bisect_left
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        Find the maximum number of envelopes that can be nested.
        
        Approach:
        1. Sort by width ascending and height descending (for same width)
        2. Find longest increasing subsequence of heights
        
        Time: O(nlogn) - sorting + LIS with binary search
        Space: O(n) - to store dp array
        
        Args:
            envelopes: List of [width, height] pairs
        Returns:
            Maximum number of nested envelopes possible
        """
        if not envelopes:
            return 0
            
        # Sort by width ascending, height descending for optimal LIS
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Extract heights for LIS
        heights = [h for _, h in envelopes]
        
        def length_of_LIS(nums: List[int]) -> int:
            """Find length of Longest Increasing Subsequence using binary search."""
            dp = []  # dp[i] represents smallest ending number for LIS of length i+1
            for num in nums:
                pos = bisect_left(dp, num)
                if pos == len(dp):
                    dp.append(num)
                else:
                    dp[pos] = num
            return len(dp)
            
        return length_of_LIS(heights)


def test_max_envelopes():
    """Test function for Russian Doll Envelopes solution"""
    solution = Solution()
    
    # Test case 1: Example from problem statement
    test1 = [[5,4],[6,4],[6,7],[2,3]]
    assert solution.maxEnvelopes(test1) == 3, "Test case 1 failed"
    print("Test case 1 passed: Maximum 3 nested envelopes possible")
    
    # Test case 2: Empty input
    test2 = []
    assert solution.maxEnvelopes(test2) == 0, "Test case 2 failed"
    print("Test case 2 passed: Empty input returns 0")
    
    # Test case 3: No nesting possible
    test3 = [[1,1],[1,1],[1,1]]
    assert solution.maxEnvelopes(test3) == 1, "Test case 3 failed"
    print("Test case 3 passed: No nesting possible")
    
    # Test case 4: Complex nesting
    test4 = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
    result = solution.maxEnvelopes(test4)
    print(f"Test case 4 passed: Maximum {result} nested envelopes possible")
    
    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_max_envelopes()
