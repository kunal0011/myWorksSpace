"""
LeetCode 438: Find All Anagrams in a String

Problem Statement:
Given two strings s and p, return an array of all the start indices of p's anagrams in s.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters
"""


def findAnagrams(s: str, p: str) -> list[int]:
    if len(s) < len(p):
        return []

    result = []
    p_count = {}
    window = {}

    # Count characters in pattern
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1

    # Initialize first window
    for i in range(len(p)):
        window[s[i]] = window.get(s[i], 0) + 1

    # Check first window
    if window == p_count:
        result.append(0)

    # Slide window
    for i in range(len(p), len(s)):
        # Remove leftmost character
        window[s[i - len(p)]] -= 1
        if window[s[i - len(p)]] == 0:
            del window[s[i - len(p)]]

        # Add new character
        window[s[i]] = window.get(s[i], 0) + 1

        # Check if current window is anagram
        if window == p_count:
            result.append(i - len(p) + 1)

    return result

# Test driver


def run_tests():
    test_cases = [
        {
            "s": "cbaebabacd",
            "p": "abc",
            "expected": [0, 6],
            "explanation": "The substrings starting at index 0 and 6 are 'cba' and 'bac'"
        },
        {
            "s": "abab",
            "p": "ab",
            "expected": [0, 1, 2],
            "explanation": "The substrings starting at index 0, 1, and 2 are 'ab', 'ba', and 'ab'"
        },
        {
            "s": "aaaaaaaaaa",
            "p": "aaaa",
            "expected": [0, 1, 2, 3, 4, 5, 6],
            "explanation": "Multiple overlapping anagrams"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = findAnagrams(test["s"], test["p"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"String s: {test['s']}")
        print(f"Pattern p: {test['p']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Find All Anagrams problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Sliding Window with Dictionary Approach:
   - Use two dictionaries to track character frequencies
   - One for pattern p and one for current window in s
   - Window size equals length of pattern p

2. Key Optimizations:
   - Direct dictionary comparison for anagram check
   - Maintain window count by adding/removing single characters
   - Delete keys when count becomes 0 to ensure exact matches

3. Algorithm Steps:
   - Initialize pattern frequency count
   - Create first window and check if it's an anagram
   - Slide window one character at a time:
     * Remove leftmost character
     * Add rightmost character
     * Compare window frequencies with pattern

Time Complexity: O(n) where n is length of string s
Space Complexity: O(k) where k is size of character set (26 for lowercase letters)
"""
