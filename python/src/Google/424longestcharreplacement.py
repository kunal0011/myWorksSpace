"""
LeetCode 424: Longest Repeating Character Replacement

Problem Statement:
You are given a string s and an integer k. You can choose any character of the string 
and change it to any other uppercase English character. You can perform this operation 
at most k times.

Return the length of the longest substring containing the same letter you can get after 
performing the above operations.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters
- 0 <= k <= s.length
"""


def characterReplacement(s: str, k: int) -> int:
    # Initialize frequency counter and variables
    freq = {}
    max_length = 0
    max_freq = 0
    left = 0

    # Sliding window approach
    for right in range(len(s)):
        # Update frequency of current character
        freq[s[right]] = freq.get(s[right], 0) + 1
        # Update max frequency of any character in current window
        max_freq = max(max_freq, freq[s[right]])

        # Current window size - max frequency = number of characters to be replaced
        # If this exceeds k, shrink window
        window_size = right - left + 1
        if window_size - max_freq > k:
            freq[s[left]] -= 1
            left += 1

        # Update max_length (window_size is now valid)
        max_length = max(max_length, right - left + 1)

    return max_length

# Test driver


def run_tests():
    test_cases = [
        {
            "s": "ABAB",
            "k": 2,
            "expected": 4,
            "explanation": "Replace 2 'A's with 'B's to get 'BBBB'"
        },
        {
            "s": "AABABBA",
            "k": 1,
            "expected": 4,
            "explanation": "Replace 1 character to get 'AABABB' -> 'AABBBB'"
        },
        {
            "s": "AAAA",
            "k": 2,
            "expected": 4,
            "explanation": "Already all same characters"
        },
        {
            "s": "ABCDE",
            "k": 1,
            "expected": 2,
            "explanation": "Can make any two adjacent characters same"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = characterReplacement(test["s"], test["k"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input string: {test['s']}")
        print(f"k: {test['k']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Character Replacement problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Sliding Window Approach:
   - Use two pointers (left, right) to maintain a window
   - Keep track of character frequencies in current window
   - Track maximum frequency of any character in window

2. Key Optimization:
   - Window is valid if: window_size - max_freq <= k
   - This means we can replace all other characters (window_size - max_freq)
     with the most frequent character using k operations

3. Algorithm Steps:
   - Expand window to right, updating frequencies
   - If window becomes invalid (needs more than k replacements), shrink from left
   - Track maximum valid window length seen so far

Time Complexity: O(n) where n is length of string
Space Complexity: O(1) as we only store at most 26 characters in freq map
"""
