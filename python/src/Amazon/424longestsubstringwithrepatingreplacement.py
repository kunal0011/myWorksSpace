"""
LeetCode 424 - Longest Repeating Character Replacement

Problem Statement:
-----------------
You are given a string s and an integer k. You can choose any character of the string 
and change it to any other uppercase English character. You can perform this operation 
at most k times.

Return the length of the longest substring containing the same letter after performing 
the above operations.

Key Points:
----------
1. We can change at most k characters in a substring
2. All characters in the input string are uppercase English letters
3. The goal is to find the longest substring that can become all same characters
4. Uses sliding window technique with character frequency counting

Examples:
--------
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
-----------
* 1 <= s.length <= 10^5
* s consists of only uppercase English letters
* 0 <= k <= s.length
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the longest substring containing same characters after at most k replacements.
        
        Algorithm:
        1. Use sliding window approach with left and right pointers
        2. Keep track of character frequencies in current window
        3. Track maximum frequency of any character in current window
        4. If window size - max frequency > k, shrink window
        5. Update max length when valid window is found
        
        Time Complexity: O(n) where n is length of string
        Space Complexity: O(1) as we store at most 26 characters
        """
        max_len = 0        # Length of longest valid substring
        max_count = 0      # Maximum frequency of any character in current window
        count = {}         # Dictionary to store character frequencies
        left = 0          # Left pointer of sliding window

        for right in range(len(s)):
            # Add new character to frequency count
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            # Current window size minus max frequency tells us how many characters
            # need to be replaced. If this exceeds k, shrink window
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # Update maximum length of valid window
            max_len = max(max_len, right - left + 1)

        return max_len


def test_character_replacement():
    """
    Test driver for the longest repeating character replacement problem
    """
    test_cases = [
        ("ABAB", 2, 4),           # Can make all 'A's or all 'B's
        ("AABABBA", 1, 4),        # Can make "BBBB" in the middle
        ("AAAA", 2, 4),           # Already all same characters
        ("ABCD", 1, 2),           # Can make any two adjacent chars same
        ("AABABBA", 0, 2),        # No replacements allowed
        ("A", 1, 1),              # Single character
        ("AAAB", 0, 3),           # Longest existing same-char substring
        ("ABBB", 2, 4),           # Can make all 'B's
        ("ABCDE", 5, 5),          # Can replace all characters
    ]
    
    solution = Solution()
    
    for i, (s, k, expected) in enumerate(test_cases, 1):
        result = solution.characterReplacement(s, k)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input: s = {s}, k = {k}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("-" * 40)

if __name__ == "__main__":
    test_character_replacement()
