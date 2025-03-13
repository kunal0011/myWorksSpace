"""
LeetCode 634 - Find the Derangement of An Array

In combinatorial mathematics, a derangement is a permutation of the elements of a set 
such that no element appears in its original position.

Given a number n, return the number of derangements of an array of size n.
Since the answer may be very large, return it modulo 10^9 + 7.

Example 1:
Input: n = 3
Output: 2
Explanation: Original array: [1,2,3]
The two derangements are [2,3,1] and [3,1,2]

Example 2:
Input: n = 2
Output: 1
Explanation: Original array: [1,2]
The only derangement is [2,1]

Constraints:
1 <= n <= 10^6
"""

class Solution:
    def findDerangement(self, n: int) -> int:
        """
        Optimized iterative solution using dynamic programming
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        MOD = 10**9 + 7
        if n <= 1:
            return 0
        if n == 2:
            return 1
            
        prev2, prev1 = 0, 1  # D(1) = 0, D(2) = 1
        for i in range(3, n + 1):
            curr = ((i - 1) * (prev1 + prev2)) % MOD
            prev2, prev1 = prev1, curr
            
        return prev1

    def findDerangement_recursive(self, n: int) -> int:
        """
        Recursive solution with memoization (for validation)
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        MOD = 10**9 + 7
        memo = {1: 0, 2: 1}
        
        def derange(n):
            if n in memo:
                return memo[n]
            memo[n] = ((n - 1) * (derange(n - 1) + derange(n - 2))) % MOD
            return memo[n]
            
        return derange(n)

def test_find_derangement():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        (1, 0),
        (2, 1),
        (3, 2),
        (4, 9),
        
        # Edge cases
        (5, 44),
        (6, 265),
        
        # Larger numbers
        (10, 1334961),
        (15, 481066515),
        
        # Very large number (testing modulo)
        (20, 895014631),
    ]
    
    print("Running tests for Find Derangement...\n")
    
    for i, (n, expected) in enumerate(test_cases, 1):
        # Test optimized solution
        result = solution.findDerangement(n)
        # Test recursive solution
        result_rec = solution.findDerangement_recursive(n)
        
        print(f"Test Case {i}:")
        print(f"Input: n = {n}")
        print(f"Expected: {expected}")
        print(f"Iterative Solution: {result} {'✅' if result == expected else '❌'}")
        print(f"Recursive Solution: {result_rec} {'✅' if result_rec == expected else '❌'}")
        
        if result != expected:
            print(f"❌ Test case failed!")
            print(f"Got: {result}")
            print(f"Expected: {expected}")
        else:
            print("✅ Test case passed!")
        print()

if __name__ == "__main__":
    test_find_derangement()
