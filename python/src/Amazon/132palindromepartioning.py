class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # Create a DP table to check palindromes
        is_palindrome = [[False] * n for _ in range(n)]

        # Initialize min cuts table
        min_cuts = [float('inf')] * n

        for end in range(n):
            for start in range(end + 1):
                # Check if the current substring is a palindrome
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start + 1][end - 1]):
                    is_palindrome[start][end] = True
                    # If the entire substring from 0 to end is a palindrome, no cut is needed
                    if start == 0:
                        min_cuts[end] = 0
                    else:
                        # Otherwise, update the minimum cuts needed
                        min_cuts[end] = min(
                            min_cuts[end], min_cuts[start - 1] + 1)

        return min_cuts[-1]
