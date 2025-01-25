"""
LeetCode 58. Length of Last Word

Problem Statement:
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:
- 1 <= s.length <= 10^4
- s consists of only English letters and spaces ' '
- There will be at least one word in s
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Trim trailing spaces and find last space
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        length = 0
        # Count characters until we hit a space or the start
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


def explain_last_word_length(s: str) -> None:
    """
    Function to explain the process of finding the length of the last word
    """
    print(f"\nFinding length of last word in: '{s}'")
    print("=" * 50)

    # Visual representation of the string with position markers
    print("String with position markers:")
    for i, char in enumerate(s):
        print(char if char != ' ' else '␣', end='')
    print()
    for i in range(len(s)):
        print(i % 10, end='')
    print("\n")

    i = len(s) - 1
    print(f"Starting from the end (index {i})")

    # Skip trailing spaces
    while i >= 0 and s[i] == ' ':
        print(f"Skipping space at index {i}")
        i -= 1

    if i < 0:
        print("No word found!")
        return 0

    print(f"\nFound last character at index {i}: '{s[i]}'")

    # Count word length
    length = 0
    start_index = i
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1

    last_word = s[i+1:start_index+1]
    print(f"\nLast word: '{last_word}'")
    print(f"Length: {length}")

    return length


def test_length_of_last_word():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()

    test_cases = [
        {
            "s": "Hello World",
            "expected": 5,
            "description": "Basic case"
        },
        {
            "s": "   fly me   to   the moon  ",
            "expected": 4,
            "description": "Multiple spaces"
        },
        {
            "s": "luffy is still joyboy",
            "expected": 6,
            "description": "No trailing spaces"
        },
        {
            "s": "a",
            "expected": 1,
            "description": "Single character"
        },
        {
            "s": "a ",
            "expected": 1,
            "description": "Single character with space"
        },
        {
            "s": "day    ",
            "expected": 3,
            "description": "Multiple trailing spaces"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nRunning test case {i}: {description}")
        print(f"Input string: '{s}'")

        result = solution.lengthOfLastWord(s)

        assert result == expected, \
            f"\nTest case {i} failed!\nExpected: {expected}\nGot: {result}"
        print(f"✓ Test case {i} passed!")


if __name__ == "__main__":
    try:
        test_length_of_last_word()
        print("\nAll test cases passed successfully! 🎉")

        # Explain with detailed examples
        explain_last_word_length("Hello World")
        explain_last_word_length("   fly me   to   the moon  ")
    except AssertionError as e:
        print(f"Test failed! {str(e)}")
