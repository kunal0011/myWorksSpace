"""
LeetCode 598 - Range Addition II

You are given an m x n matrix M initialized with all 0's and an array of operations ops, 
where ops[i] = [ai, bi] means M[x][y] should be incremented by 1 for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: After performing these operations:
- Op[0] = [2,2]: Adds 1 to cells in range (0,0) to (1,1)
- Op[1] = [3,3]: Adds 1 to cells in range (0,0) to (2,2)
Maximum value (2) occurs in 4 cells: (0,0), (0,1), (1,0), (1,1)

Example 2:
Input: m = 3, n = 3, ops = [[2,2],[3,3],[1,1]]
Output: 1
Explanation: Maximum value (3) only occurs in cell (0,0)

Constraints:
- 1 <= m, n <= 4 * 10^4
- 0 <= ops.length <= 10^4
- ops[i].length == 2
- 1 <= ai <= m
- 1 <= bi <= n
"""

from typing import List
from time import time


class Solution:
    def maxCount(self, m: int, n: int, operations: List[List[int]]) -> int:
        """
        Optimized solution for finding the count of maximum integers after range additions.
        
        Logic:
        - Each operation increases values in a rectangle from (0,0) to (ai-1, bi-1)
        - The maximum value will be in the intersection of all rectangles
        - We just need to find the smallest ai and bi among all operations
        
        Time Complexity: O(k) where k is the number of operations
        Space Complexity: O(1)
        """
        if not operations:
            return m * n

        # Initialize min_a and min_b to maximum possible values
        min_a = m
        min_b = n

        # Find the intersection point by getting minimum of all coordinates
        for a, b in operations:
            min_a = min(min_a, a)
            min_b = min(min_b, b)

        return min_a * min_b


def test_maxCount():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        (3, 3, [[2,2], [3,3]], 4),
        (3, 3, [[2,2], [3,3], [1,1]], 1),
        
        # Edge cases
        (1, 1, [], 1),
        (3, 3, [], 9),
        (2, 2, [[2,2]], 4),
        
        # Large dimension cases
        (10000, 10000, [[1,1]], 1),
        (5, 5, [[5,5], [4,4], [3,3]], 9),
        
        # Complex cases
        (4, 4, [[4,4], [3,3], [2,2], [1,1]], 1),
        (3, 4, [[2,3], [3,2]], 4),
    ]
    
    print("Running tests for Range Addition II...\n")
    
    for i, (m, n, ops, expected) in enumerate(test_cases, 1):
        start_time = time()
        result = solution.maxCount(m, n, ops)
        end_time = time()
        
        print(f"Test Case {i}:")
        print(f"Input: m = {m}, n = {n}, ops = {ops}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Time taken: {(end_time - start_time)*1000:.2f} ms")
        
        if result == expected:
            print("✅ Test case passed!")
        else:
            print("❌ Test case failed!")
        print()


if __name__ == "__main__":
    test_maxCount()
