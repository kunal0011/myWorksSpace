"""
LeetCode 76. Minimum Window Substring

Problem Statement:
Given two strings s and t of lengths m and n respectively, return the minimum window substring
of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 105
- s and t consist of uppercase and lowercase English letters.
"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Initialize target character frequency
        target_freq = Counter(t)
        required = len(target_freq)

        # Initialize window
        window_freq = {}
        formed = 0  # Count of characters with required frequency

        # Initialize result
        min_len = float('inf')
        result = ""

        # Initialize sliding window pointers
        left = right = 0

        while right < len(s):
            # Add character to window
            char = s[right]
            window_freq[char] = window_freq.get(char, 0) + 1

            # Check if current character helps form target
            if char in target_freq and window_freq[char] == target_freq[char]:
                formed += 1

            # Try to minimize window
            while left <= right and formed == required:
                # Update result if current window is smaller
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left:right + 1]

                # Remove leftmost character
                char = s[left]
                window_freq[char] -= 1

                # Update formed count if necessary
                if char in target_freq and window_freq[char] < target_freq[char]:
                    formed -= 1

                left += 1

            right += 1

        return result


def explain_min_window(s: str, t: str) -> None:
    """
    Function to explain the minimum window substring process step by step
    """
    print(f"\nFinding minimum window substring")
    print(f"String s: {s}")
    print(f"String t: {t}")
    print("=" * 50)

    if not s or not t:
        print("Empty input string(s)")
        return ""

    target_freq = Counter(t)
    print(f"\nTarget character frequencies: {dict(target_freq)}")
    required = len(target_freq)
    print(f"Number of unique characters required: {required}")

    window_freq = {}
    formed = 0
    min_len = float('inf')
    result = ""
    left = right = 0

    print("\nStarting sliding window process:")
    while right < len(s):
        # Add character to window
        char = s[right]
        window_freq[char] = window_freq.get(char, 0) + 1

        print(f"\nStep: Adding '{char}' at position {right}")
        print(f"Current window: {s[left:right+1]}")
        print(f"Window frequencies: {window_freq}")

        if char in target_freq and window_freq[char] == target_freq[char]:
            formed += 1
            print(
                f"Matched required frequency for '{char}'. Formed: {formed}/{required}")

        # Try to minimize window
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = s[left:right + 1]
                print(
                    f"Found new minimum window: {result} (length: {min_len})")

            char = s[left]
            window_freq[char] -= 1

            print(f"Trying to minimize: removing '{char}' from left")
            if char in target_freq and window_freq[char] < target_freq[char]:
                formed -= 1
                print(
                    f"Lost required frequency for '{char}'. Formed: {formed}/{required}")

            left += 1
            if formed == required:
                print(f"Current valid window: {s[left:right+1]}")

        right += 1

    print(f"\nFinal result: {result}")
    return result


def test_min_window():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "s": "ADOBECODEBANC",
            "t": "ABC",
            "expected": "BANC",
            "description": "Standard case"
        },
        {
            "s": "a",
            "t": "a",
            "expected": "a",
            "description": "Single character"
        },
        {
            "s": "a",
            "t": "aa",
            "expected": "",
            "description": "Impossible case"
        },
        {
            "s": "ADOBECODEBANC",
            "t": "ABBC",
            "expected": "BECODEB",
            "description": "Multiple same characters"
        },
        {
            "s": "ab",
            "t": "b",
            "expected": "b",
            "description": "Target is substring"
        },
        {
            "s": "aaaaaaaaaa",
            "t": "aa",
            "expected": "aa",
            "description": "Repeated characters"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        t = test_case["t"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: s = '{s}', t = '{t}'")

        result = solution.minWindow(s, t)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_min_window()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_min_window("ADOBECODEBANC", "ABC")
        explain_min_window("a", "aa")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
