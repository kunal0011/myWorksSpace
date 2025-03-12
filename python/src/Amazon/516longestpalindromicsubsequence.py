"""
LeetCode 516 - Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements
without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Space optimized: we only need two rows of the dp table
        dp = [0] * n
        dp_prev = [0] * n

        # Base case: single characters are palindromes of length 1
        for i in range(n):
            dp[i] = 1

        # Fill the dp table
        for i in range(n-2, -1, -1):
            # Save the previous row
            dp_prev = dp.copy()
            dp[i] = 1  # Reset diagonal element
            
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[j] = dp_prev[j-1] + 2
                else:
                    dp[j] = max(dp_prev[j], dp[j-1])

        return dp[n-1]

    def longestPalindromeSubseq_recursive(self, s: str) -> int:
        """Alternative recursive solution with memoization"""
        memo = {}
        
        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            
            if i > j:
                return 0
            if i == j:
                return 1
                
            if s[i] == s[j]:
                memo[(i, j)] = dp(i+1, j-1) + 2
            else:
                memo[(i, j)] = max(dp(i+1, j), dp(i, j-1))
            
            return memo[(i, j)]
        
        return dp(0, len(s)-1)


def test_longest_palindromic_subseq():
    """Test function to verify both solution approaches"""
    solution = Solution()
    
    test_cases = [
        ("bbbab", 4),
        ("cbbd", 2),
        ("", 0),
        ("a", 1),
        ("aaa", 3),
        ("abcde", 1),
        ("abcba", 5),
        ("abaab", 4),
        ("zkabababak", 7),
        ("character", 4)
    ]
    
    for i, (s, expected) in enumerate(test_cases, 1):
        # Test iterative solution
        result_iter = solution.longestPalindromeSubseq(s)
        # Test recursive solution
        result_recur = solution.longestPalindromeSubseq_recursive(s)
        
        status_iter = "✓" if result_iter == expected else "✗"
        status_recur = "✓" if result_recur == expected else "✗"
        
        print(f"Test {i}:")
        print(f"Input: s = '{s}'")
        print(f"Iterative Solution: {status_iter} Got: {result_iter}")
        print(f"Recursive Solution: {status_recur} Got: {result_recur}")
        print(f"Expected: {expected}\n")


if __name__ == "__main__":
    test_longest_palindromic_subseq()
