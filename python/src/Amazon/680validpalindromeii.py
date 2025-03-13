"""
LeetCode 680: Valid Palindrome II

Problem Statement:
Given a string s, return true if the s can be made a palindrome after deleting at most one character from it.
A string is palindrome if it reads the same forward and backward.

Key insights:
1. Use two pointers moving from both ends
2. When mismatch found, try skipping either character once
3. Time complexity: O(n), Space complexity: O(1)
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(left: int, right: int) -> bool:
            """Check if substring s[left:right+1] is palindrome"""
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try skipping either character
                return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
            left += 1
            right -= 1
            
        return True

def test_valid_palindrome():
    solution = Solution()
    
    # Test cases: [input_string, expected_result, description]
    test_cases = [
        ("aba", True, "Already palindrome"),
        ("abca", True, "Can be palindrome by removing 'c'"),
        ("abc", False, "Cannot be palindrome with one deletion"),
        ("", True, "Empty string"),
        ("a", True, "Single character"),
        ("aa", True, "Two same characters"),
        ("deeee", True, "Multiple same characters"),
        ("raceacar", True, "Remove middle character"),
        ("abcddcba", True, "Perfect palindrome"),
        ("abcdefdba", False, "Cannot be palindrome"),
        ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True, 
         "Long palindrome with one character removal"),
    ]
    
    for i, (s, expected, description) in enumerate(test_cases, 1):
        result = solution.validPalindrome(s)
        assert result == expected, \
            f"Test {i} failed: {description}\nInput: {s}\nExpected: {expected}, Got: {result}"
        print(f"\nTest {i}: {description}")
        print(f"Input string: {s}")
        print(f"Expected: {expected}, Got: {result}")
        print("-" * 50)

if __name__ == "__main__":
    test_valid_palindrome()
