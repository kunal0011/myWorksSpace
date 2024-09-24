from typing import List


class Solution:
    def partition(self, s: str):
        result = []

        # Helper function to check if a string is a palindrome
        def is_palindrome(substring: str) -> bool:
            return substring == substring[::-1]

        # Backtracking function to find all partitions
        def backtrack(start: int, path: List[int]):
            # If we reach the end of the string, add the current partition to the result
            if start == len(s):
                result.append(path[:])
                return

            # Try all possible partitions by expanding the end index
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrome(substring):
                    path.append(substring)        # Choose
                    backtrack(end, path)          # Explore
                    path.pop()                    # Unchoose

        # Start backtracking from the first character
        backtrack(0, [])
        return result
