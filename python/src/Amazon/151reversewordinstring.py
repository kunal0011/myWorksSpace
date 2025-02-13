"""
LeetCode 151. Reverse Words in a String

Problem Statement:
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space.

Constraints:
- 1 <= s.length <= 104
- s contains English letters (upper-case and lower-case), digits, and spaces ' '
- There is at least one word in s
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        # Split by spaces, filter out empty strings, and reverse
        words = [word for word in s.split() if word]
        return ' '.join(words[::-1])

    def reverseWordsInPlace(self, s: str) -> str:
        """
        Alternative solution without using split()
        Time complexity: O(n)
        Space complexity: O(n)
        """
        # Convert string to list of characters for in-place operations
        chars = list(s.strip())
        n = len(chars)

        # Remove extra spaces
        i = j = 0
        while j < n:
            while j < n and chars[j] == ' ':
                j += 1
            while j < n and chars[j] != ' ':
                chars[i] = chars[j]
                i += 1
                j += 1
            while j < n and chars[j] == ' ':
                j += 1
            if j < n:
                chars[i] = ' '
                i += 1

        chars = chars[:i]

        # Reverse the entire string
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        # Reverse each word
        reverse(chars, 0, len(chars) - 1)
        start = 0
        for end in range(len(chars)):
            if chars[end] == ' ':
                reverse(chars, start, end - 1)
                start = end + 1
            elif end == len(chars) - 1:
                reverse(chars, start, end)

        return ''.join(chars)


def test_reverse_words():
    """Test function with various test cases."""
    solution = Solution()

    test_cases = [
        {
            "s": "the sky is blue",
            "expected": "blue is sky the",
            "description": "Basic case with single spaces"
        },
        {
            "s": "  hello world  ",
            "expected": "world hello",
            "description": "Leading and trailing spaces"
        },
        {
            "s": "a good   example",
            "expected": "example good a",
            "description": "Multiple spaces between words"
        },
        {
            "s": "hello",
            "expected": "hello",
            "description": "Single word"
        },
        {
            "s": "   spaces   everywhere   ",
            "expected": "everywhere spaces",
            "description": "Multiple spaces everywhere"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.reverseWords(test_case["s"])
        result2 = solution.reverseWordsInPlace(test_case["s"])

        assert result1 == test_case["expected"], \
            f'Test case {i} failed (method 1). Expected "{test_case["expected"]}", got "{result1}"'
        assert result2 == test_case["expected"], \
            f'Test case {i} failed (method 2). Expected "{test_case["expected"]}", got "{result2}"'

        print(f'Test case {i} passed: {test_case["description"]}')

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_reverse_words()
