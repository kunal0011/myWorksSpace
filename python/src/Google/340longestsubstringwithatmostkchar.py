"""
LeetCode 340 - Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest substring of s 
that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(k) where k is the number of distinct characters allowed
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or not s:
            return 0

        # Dictionary to store the count of characters in the current window
        char_count = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Add the current character to the dictionary
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # If the number of distinct characters exceeds k, shrink the window
            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            # Update the maximum length of the substring
            max_len = max(max_len, right - left + 1)

        return max_len

def test_longest_substring_k_distinct():
    # Test cases
    test_cases = [
        ("eceba", 2),
        ("aa", 1),
        ("", 1),
        ("abcabcabc", 2),
        ("aaaaaaa", 1),
        ("abaccc", 2)
    ]
    
    expected_outputs = [3, 2, 0, 4, 7, 4]
    
    solution = Solution()
    for i, ((s, k), expected) in enumerate(zip(test_cases, expected_outputs)):
        result = solution.lengthOfLongestSubstringKDistinct(s, k)
        print(f"Test case {i + 1}:")
        print(f"Input: s = '{s}', k = {k}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}\n")

if __name__ == "__main__":
    test_longest_substring_k_distinct()
