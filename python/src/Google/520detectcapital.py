"""
LeetCode 520 - Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:
1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Time Complexity: O(n) where n is the length of the word
Space Complexity: O(1)
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # Optimized solution: Check length first to handle edge cases
        n = len(word)
        if n <= 1:
            return True

        # If first letter is lowercase, all following letters must be lowercase
        if word[0].islower():
            return word[1:].islower()

        # If second letter is uppercase, all letters must be uppercase
        if n >= 2 and word[1].isupper():
            return word[2:].isupper()

        # If second letter is lowercase, all following letters must be lowercase
        return word[1:].islower()


def run_test_cases():
    solution = Solution()
    test_cases = [
        "USA",          # True (all capitals)
        "FlaG",        # False (mixed capitals)
        "leetcode",    # True (all lowercase)
        "Google",      # True (first letter capital)
        "a",           # True (single letter)
        "mL",          # False (wrong capitalization)
    ]

    for word in test_cases:
        result = solution.detectCapitalUse(word)
        print(f'Input: "{word}" -> Output: {result}')


if __name__ == "__main__":
    run_test_cases()
