"""
LeetCode 567 - Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Logic:
1. Use sliding window technique with Counter (hash map)
2. Create frequency counter for s1 and initial window of s2 (length = len(s1))
3. Slide window through s2:
   - Add new character to window
   - Remove leftmost character from window
   - Compare window frequencies with s1 frequencies
4. If frequencies match at any point, we found a permutation

Time Complexity: O(n) where n is length of s2
Space Complexity: O(k) where k is size of character set (26 for lowercase letters)
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)

        if len_s1 > len_s2:
            return False

        # Frequency counter for s1
        s1_count = Counter(s1)
        # Initial window counter for the first len_s1 characters of s2
        window_count = Counter(s2[:len_s1])

        if s1_count == window_count:
            return True

        # Slide the window across s2
        for i in range(len_s1, len_s2):
            # Include a new character to the window
            window_count[s2[i]] += 1
            # Remove the leftmost character from the window
            left_char = s2[i - len_s1]
            window_count[left_char] -= 1
            # Remove the character count from the window if it becomes zero
            if window_count[left_char] == 0:
                del window_count[left_char]

            # Compare window with s1_count
            if s1_count == window_count:
                return True

        return False


def run_test_cases():
    solution = Solution()
    test_cases = [
        {
            "s1": "ab",
            "s2": "eidbaooo",
            "expected": True,
            "explanation": "'ba' is a permutation of 'ab' and is a substring of s2"
        },
        {
            "s1": "ab",
            "s2": "eidboaoo",
            "expected": False,
            "explanation": "s2 does not contain any permutation of s1"
        },
        {
            "s1": "adc",
            "s2": "dcda",
            "expected": True,
            "explanation": "'cda' is a permutation of 'adc'"
        },
        {
            "s1": "hello",
            "s2": "world",
            "expected": False,
            "explanation": "No permutation of 'hello' in 'world'"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = solution.checkInclusion(test["s1"], test["s2"])
        print(f"\nTest Case {i}:")
        print(f"s1: {test['s1']}")
        print(f"s2: {test['s2']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}")


if __name__ == "__main__":
    run_test_cases()
