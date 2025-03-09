"""
LeetCode 338: Counting Bits

Problem Statement:
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0 (0 ones)
1 --> 1 (1 one)
2 --> 10 (1 one)

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0  (0 ones)
1 --> 1  (1 one)
2 --> 10 (1 one)
3 --> 11 (2 ones)
4 --> 100 (1 one)
5 --> 101 (2 ones)

Logic:
1. Use dynamic programming to build the solution
2. Key Observation: For any number i, the number of 1's in its binary representation
   can be calculated using the number of 1's in i/2 plus the least significant bit
3. The relationship is: dp[i] = dp[i >> 1] + (i & 1)
   - i >> 1 gives us i/2 (right shift by 1)
   - i & 1 gives us the least significant bit (1 if odd, 0 if even)
4. This works because:
   - When we right shift by 1, we remove the least significant bit
   - The rest of the bits remain the same, so we can reuse the previously calculated result
"""

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result array
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            # Use the relation countBits(i) = countBits(i // 2) + (i % 2)
            dp[i] = dp[i >> 1] + (i & 1)

        return dp


def run_test_cases():
    solution = Solution()
    
    # Test case 1
    n1 = 2
    expected1 = [0, 1, 1]
    result1 = solution.countBits(n1)
    print(f"Test case 1:")
    print(f"Input: n = {n1}")
    print(f"Expected: {expected1}")
    print(f"Got: {result1}")
    print(f"Pass? {result1 == expected1}\n")
    
    # Test case 2
    n2 = 5
    expected2 = [0, 1, 1, 2, 1, 2]
    result2 = solution.countBits(n2)
    print(f"Test case 2:")
    print(f"Input: n = {n2}")
    print(f"Expected: {expected2}")
    print(f"Got: {result2}")
    print(f"Pass? {result2 == expected2}\n")
    
    # Test case 3 - Edge case with n = 0
    n3 = 0
    expected3 = [0]
    result3 = solution.countBits(n3)
    print(f"Test case 3:")
    print(f"Input: n = {n3}")
    print(f"Expected: {expected3}")
    print(f"Got: {result3}")
    print(f"Pass? {result3 == expected3}\n")
    
    # Test case 4 - Larger number
    n4 = 8
    expected4 = [0, 1, 1, 2, 1, 2, 2, 3, 1]
    result4 = solution.countBits(n4)
    print(f"Test case 4:")
    print(f"Input: n = {n4}")
    print(f"Expected: {expected4}")
    print(f"Got: {result4}")
    print(f"Pass? {result4 == expected4}")


if __name__ == "__main__":
    run_test_cases()
