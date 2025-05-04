"""
LeetCode 2255 - Count Prefixes of a Given String

Problem Statement:
You are given a string array words and a string s. Count and return the number of strings in words 
that are prefixes of s. A prefix of a string is a substring that occurs at the beginning of the string.
A substring is a contiguous sequence of characters within a string.

Time Complexity: O(n*m) where n is length of words array and m is average length of words
Space Complexity: O(1) as we only use a counter variable
"""


class Solution:
    def countPrefixes(self, words: list[str], s: str) -> int:
        """
        Logic:
        1. Initialize a counter for matching prefixes
        2. For each word in words array:
           - Use startswith() to check if word is prefix of s
           - Increment counter if true
        3. Return final count

        Args:
            words: List of strings to check as prefixes
            s: Target string to check against
        Returns:
            Number of strings in words that are prefixes of s
        """
        count = 0
        for word in words:
            # Check if the word is a prefix of the string s
            if s.startswith(word):
                count += 1
        return count


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'words': ["a", "b", "c", "ab", "bc", "abc"],
            's': "abc",
            'expected': 3
        },
        {
            'words': ["a", "a"],
            's': "aa",
            'expected': 2
        },
        {
            'words': ["xyz", "xz", "z"],
            's': "xyz",
            'expected': 1
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.countPrefixes(test['words'], test['s'])
        status = "PASSED" if result == test['expected'] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: words = {test['words']}, s = {test['s']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}\n")


if __name__ == "__main__":
    main()
