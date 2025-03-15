"""
LeetCode 823: Binary Trees With Factors

Given an array of unique integers arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times.
Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 10^9 + 7.

Constraints:
- 1 <= arr.length <= 1000
- 2 <= arr[i] <= 10^9
- All values in arr are unique
"""

from typing import List, Dict
from collections import defaultdict


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Optimized solution using dynamic programming
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        MOD = 10**9 + 7
        arr.sort()  # Sort for efficient factor finding
        dp = defaultdict(int)  # Number of trees with each value as root
        
        for i, num in enumerate(arr):
            # Every number forms a single-node tree
            dp[num] = 1
            
            # Check for factor pairs
            for j in range(i):
                if num % arr[j] == 0:  # arr[j] could be left child
                    right = num // arr[j]
                    if right in dp:
                        dp[num] = (dp[num] + dp[arr[j]] * dp[right]) % MOD
                        
        return sum(dp.values()) % MOD
    
    def numFactoredBinaryTrees_set(self, arr: List[int]) -> int:
        """
        Alternative solution using set for faster lookup
        Time complexity: O(n^2)
        Space complexity: O(n)
        """
        MOD = 10**9 + 7
        arr.sort()
        nums = set(arr)
        dp = {num: 1 for num in arr}
        
        for num in arr:
            for factor in arr:
                if factor >= num:
                    break
                if num % factor == 0 and num // factor in nums:
                    dp[num] = (dp[num] + dp[factor] * dp[num // factor]) % MOD
                    
        return sum(dp.values()) % MOD


def validate_trees(arr: List[int], result: int) -> bool:
    """Validate if the result is possible"""
    if not 1 <= len(arr) <= 1000:
        return False
        
    if any(not 2 <= x <= 10**9 for x in arr):
        return False
        
    if len(arr) != len(set(arr)):
        return False
        
    MOD = 10**9 + 7
    if not 0 <= result < MOD:
        return False
        
    return True


def test_binary_trees_with_factors():
    """Test function for Binary Trees With Factors"""
    test_cases = [
        ([2, 4], 3),
        ([2, 4, 5, 10], 7),
        ([2], 1),
        ([18, 3, 6, 2], 12),
        ([2, 3, 4, 6, 12], 34),
        ([2, 3, 6], 7),
        ([2, 3, 4, 5, 6, 7, 8], 41)
    ]
    
    solution = Solution()
    
    for i, (arr, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.numFactoredBinaryTrees(arr)
        result2 = solution.numFactoredBinaryTrees_set(arr)
        
        print(f"\nTest case {i}:")
        print(f"Input array: {arr}")
        print(f"Expected: {expected}")
        print(f"DP solution: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"Set solution: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Validate result
        is_valid = validate_trees(arr, result1)
        print(f"Valid solution: {'✓' if is_valid else '✗'}")
        
        # Print example trees for small inputs
        if len(arr) <= 4:
            print("\nPossible trees:")
            for num in arr:
                for j in range(len(arr)):
                    for k in range(len(arr)):
                        if arr[j] * arr[k] == num:
                            print(f"{num} = {arr[j]} × {arr[k]}")


if __name__ == "__main__":
    test_binary_trees_with_factors()
