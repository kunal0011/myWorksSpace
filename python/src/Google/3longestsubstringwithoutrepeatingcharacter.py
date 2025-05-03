"""
LeetCode 3 - Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s: str) -> int:
    # Optimized sliding window solution with O(n) time complexity
    char_index = {}  # stores the last index of each character
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        # If we find a repeating character, move the start pointer
        # to the position after the last occurrence of current character
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        
        char_index[char] = end
    
    return max_length

def test_longest_substring():
    # Test cases
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
        ("au", 2),
        ("dvdf", 3),
        ("aab", 2),
        ("tmmzuxt", 5)
    ]
    
    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = lengthOfLongestSubstring(test_input)
        assert result == expected, f"Test case {i} failed: input='{test_input}', expected={expected}, got={result}"
        print(f"Test case {i} passed: '{test_input}' -> {result}")

if __name__ == "__main__":
    test_longest_substring()
    print("All test cases passed successfully!")