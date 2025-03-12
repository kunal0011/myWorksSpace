"""
LeetCode 583 - Delete Operation for Two Strings

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
In one step, you can delete exactly one character from either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
- 1 <= word1.length, word2.length <= 500
- word1 and word2 consist of only lowercase English letters
"""

from functools import lru_cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Optimized bottom-up DP solution
        Time Complexity: O(m*n) where m and n are lengths of the strings
        Space Complexity: O(m*n)
        """
        m, n = len(word1), len(word2)
        
        # dp[i][j] represents minimum steps needed for word1[0:i] and word2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize first row and column
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        # Fill dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + 1,  # Delete from word1
                                dp[i][j-1] + 1)  # Delete from word2
        
        return dp[m][n]
    
    def minDistance_space_optimized(self, word1: str, word2: str) -> int:
        """
        Space optimized solution using 1D DP array
        Time Complexity: O(m*n)
        Space Complexity: O(min(m,n))
        """
        # Make word1 the shorter string for space optimization
        if len(word1) > len(word2):
            word1, word2 = word2, word1
            
        m, n = len(word1), len(word2)
        prev_row = list(range(n + 1))
        curr_row = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr_row[0] = i
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    curr_row[j] = prev_row[j-1]
                else:
                    curr_row[j] = min(prev_row[j], curr_row[j-1]) + 1
            prev_row = curr_row[:]
            
        return curr_row[n]
    
    def minDistance_recursive(self, word1: str, word2: str) -> int:
        """
        Top-down recursive solution with memoization
        Time Complexity: O(m*n)
        Space Complexity: O(m*n) for memoization
        """
        @lru_cache(None)
        def solve(i: int, j: int) -> int:
            # Base cases
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            
            # If characters match, no deletion needed
            if word1[i] == word2[j]:
                return solve(i + 1, j + 1)
            
            # Try deleting from either string
            return min(solve(i + 1, j), solve(i, j + 1)) + 1
        
        return solve(0, 0)


def test_min_distance():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ("sea", "eat", 2),           # Example 1
        ("leetcode", "etco", 4),     # Example 2
        
        # Edge cases
        ("a", "b", 2),              # Different single characters
        ("", "a", 1),               # Empty string and non-empty string
        ("a", "", 1),               # Non-empty string and empty string
        ("", "", 0),                # Both empty strings
        
        # Test cases with same characters in different order
        ("abc", "cba", 4),          # All characters different positions
        ("abcde", "cdeab", 6),      # Cyclic permutation
        
        # Test cases with repeating characters
        ("aaa", "aa", 1),           # Repeating characters
        ("aaaa", "aa", 2),          # More repeating characters
        
        # Longer test cases
        ("intention", "execution", 8),
        ("zoologicoarchaeologist", "zoogeologist", 10),
        
        # Test cases with common subsequences
        ("abcdef", "acf", 3),       # Common subsequence
        ("abcdef", "xyz", 9),       # No common characters
        
        # Special patterns
        ("aabbcc", "abc", 3),       # Duplicates in first string
        ("abc", "aabbcc", 3),       # Duplicates in second string
    ]
    
    print("Running tests for Delete Operation for Two Strings...\n")
    
    for i, (word1, word2, expected) in enumerate(test_cases, 1):
        # Test all three implementations
        result1 = solution.minDistance(word1, word2)
        result2 = solution.minDistance_space_optimized(word1, word2)
        result3 = solution.minDistance_recursive(word1, word2)
        
        print(f"Test Case {i}:")
        print(f"Input: word1 = '{word1}', word2 = '{word2}'")
        print(f"Expected: {expected}")
        print(f"DP Solution: {result1} {'✅' if result1 == expected else '❌'}")
        print(f"Space Optimized: {result2} {'✅' if result2 == expected else '❌'}")
        print(f"Recursive Solution: {result3} {'✅' if result3 == expected else '❌'}")
        
        if result1 != expected or result2 != expected or result3 != expected:
            print("❌ Test case failed!")
            if result1 != expected:
                print(f"DP solution failed. Got: {result1}")
            if result2 != expected:
                print(f"Space optimized solution failed. Got: {result2}")
            if result3 != expected:
                print(f"Recursive solution failed. Got: {result3}")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_min_distance()