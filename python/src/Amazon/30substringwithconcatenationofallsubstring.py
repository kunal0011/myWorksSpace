from typing import List
from collections import Counter, defaultdict

"""
LeetCode 30. Substring with Concatenation of All Words

Problem Statement:
You are given a string s and an array of strings words of the same length.
Return all starting indices of substring(s) in s that is a concatenation of each word
in words exactly once, in any order.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar".

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Explanation: No substring contains all words.

Constraints:
- 1 <= s.length <= 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- s and words[i] consist of lowercase English letters

Approach:
1. Use sliding window with dictionary counting
2. All words are same length, so we can split string into fixed-size chunks
3. Use Counter to track word frequencies
4. Time Complexity: O(N * M * K) where N = len(s), M = len(words[0]), K = len(words)
5. Space Complexity: O(K)
"""


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        result = []

        # Create frequency map of words
        word_freq = Counter(words)

        # Check each possible starting position
        for i in range(len(s) - total_len + 1):
            seen = defaultdict(int)
            valid = True

            # Check each word in the window
            for j in range(word_count):
                start = i + j * word_len
                curr_word = s[start:start + word_len]

                # If word is not in original list
                if curr_word not in word_freq:
                    valid = False
                    break

                # Add word to seen dictionary
                seen[curr_word] += 1

                # If word appears more times than in original list
                if seen[curr_word] > word_freq[curr_word]:
                    valid = False
                    break

            if valid:
                result.append(i)

        return result


def test_find_substring():
    """
    Test function to verify the findSubstring solution with various test cases
    """
    solution = Solution()

    # Test cases
    test_cases = [
        {
            "s": "barfoothefoobarman",
            "words": ["foo", "bar"],
            "expected": [0, 9],
            "description": "Basic case with two words"
        },
        {
            "s": "wordgoodgoodgoodbestword",
            "words": ["word", "good", "best", "word"],
            "expected": [],
            "description": "No valid substring"
        },
        {
            "s": "barfoofoobarthefoobarman",
            "words": ["bar", "foo", "the"],
            "expected": [6, 9, 12],
            "description": "Multiple valid substrings"
        },
        {
            "s": "wordgoodgoodgoodbestword",
            "words": ["word", "good", "best", "good"],
            "expected": [8],
            "description": "Repeated words"
        },
        {
            "s": "aaa",
            "words": ["a", "a"],
            "expected": [0, 1],
            "description": "Single character words"
        },
        {
            "s": "lingmindraboofooowingdingbarrwingmonkeypoundcake",
            "words": ["fooo", "barr", "wing", "ding", "wing"],
            "expected": [13],
            "description": "Longer string with multiple words"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        words = test_case["words"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input: s = '{s}', words = {words}")

        result = solution.findSubstring(s, words)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


def explain_example(s: str, words: List[str]) -> None:
    """
    Function to explain how the algorithm works with a specific example
    """
    print(f"\nExplaining algorithm for:")
    print(f"String: {s}")
    print(f"Words: {words}")

    word_len = len(words[0])
    word_count = len(words)
    total_len = word_len * word_count

    print(f"\nParameters:")
    print(f"Word length: {word_len}")
    print(f"Number of words: {word_count}")
    print(f"Total substring length: {total_len}")

    word_freq = Counter(words)
    print(f"\nWord frequency map: {dict(word_freq)}")

    print("\nChecking windows:")
    for i in range(len(s) - total_len + 1):
        window = s[i:i + total_len]
        words_in_window = [window[j:j + word_len]
                           for j in range(0, total_len, word_len)]
        print(f"\nWindow at index {i}: {window}")
        print(f"Words in window: {words_in_window}")

        # Check if this is a valid concatenation
        window_freq = Counter(words_in_window)
        is_valid = window_freq == word_freq
        print(f"Window frequency: {dict(window_freq)}")
        print(f"Is valid: {is_valid}")


if __name__ == "__main__":
    try:
        test_find_substring()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with an example
        explain_example("barfoothefoobarman", ["foo", "bar"])
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
