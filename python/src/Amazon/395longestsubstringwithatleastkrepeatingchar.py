"""
LeetCode 395: Longest Substring with At Least K Repeating Characters

Problem Statement:
Given a string s and an integer k, return the length of the longest substring in which 
every character appears at least k times.

Example:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Time Complexity: O(N * unique_chars), where N is string length, unique_chars is max 26 
Space Complexity: O(unique_chars) for frequency counter
"""

from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Base cases
        if not s or len(s) < k:
            return 0
        if k <= 1:
            return len(s)
            
        # Count character frequencies
        char_count = Counter(s)
        
        # Check if all characters appear at least k times
        for i, char in enumerate(s):
            if char_count[char] < k:
                # Split string at the character that appears less than k times
                # and recursively solve for each substring
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i+1:], k)
                return max(left, right)
                
        # If we reach here, all characters appear at least k times
        return len(s)
        
    def longestSubstringIterative(self, s: str, k: int) -> int:
        """
        Alternative iterative solution using sliding window for each unique count
        """
        if not s or len(s) < k:
            return 0
        if k <= 1:
            return len(s)
            
        max_len = 0
        # Try all possible numbers of unique characters
        for unique_target in range(1, len(set(s)) + 1):
            counts = {}
            left = 0
            curr_unique = 0  # Count of unique chars in current window
            at_least_k = 0   # Count of chars that appear at least k times
            
            for right in range(len(s)):
                # Expand window
                if s[right] not in counts:
                    curr_unique += 1
                counts[s[right]] = counts.get(s[right], 0) + 1
                if counts[s[right]] == k:
                    at_least_k += 1
                    
                # Shrink window if too many unique chars
                while curr_unique > unique_target:
                    if counts[s[left]] == k:
                        at_least_k -= 1
                    counts[s[left]] -= 1
                    if counts[s[left]] == 0:
                        curr_unique -= 1
                        del counts[s[left]]
                    left += 1
                    
                # Update result if all chars appear at least k times
                if curr_unique == unique_target and curr_unique == at_least_k:
                    max_len = max(max_len, right - left + 1)
                    
        return max_len

def test_longest_substring():
    """
    Test function to verify both implementations with various test cases
    """
    solution = Solution()
    
    test_cases = [
        {
            "s": "aaabb",
            "k": 3,
            "expected": 3,
            "description": "Basic case with repeating characters"
        },
        {
            "s": "ababbc",
            "k": 2,
            "expected": 5,
            "description": "Multiple valid substrings"
        },
        {
            "s": "aaabbb",
            "k": 3,
            "expected": 6,
            "description": "Entire string is valid"
        },
        {
            "s": "weitong",
            "k": 2,
            "expected": 0,
            "description": "No valid substrings"
        },
        {
            "s": "bbaaacbd",
            "k": 3,
            "expected": 3,
            "description": "Multiple splits needed"
        },
        {
            "s": "",
            "k": 1,
            "expected": 0,
            "description": "Empty string"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        k = test_case["k"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"Input: s = '{s}', k = {k}")
        
        # Test recursive solution
        result1 = solution.longestSubstring(s, k)
        assert result1 == expected, f"Recursive solution failed. Expected {expected}, got {result1}"
        
        # Test iterative solution
        result2 = solution.longestSubstringIterative(s, k)
        assert result2 == expected, f"Iterative solution failed. Expected {expected}, got {result2}"
        
        print(f"✓ Both solutions passed! Output: {result1}")

if __name__ == "__main__":
    test_longest_substring()
    print("\nAll test cases passed! 🎉")
