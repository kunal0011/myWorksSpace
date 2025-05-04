"""
LeetCode 2114 - Maximum Number of Words Found in Sentences

Problem Statement:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
You are given an array of strings sentences, where each sentences[i] represents a single sentence.
Return the maximum number of words in any single sentence.

Time Complexity: O(n * m) where n is number of sentences and m is average sentence length
Space Complexity: O(1) as we only use a single variable
"""


class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        """
        Logic:
        1. Initialize max_words to track maximum word count
        2. For each sentence:
           - Split the sentence by spaces to get list of words
           - Update max_words if current sentence has more words
        3. Return the maximum count found

        Args:
            sentences: List of strings where each string is a sentence
        Returns:
            Maximum number of words found in any sentence
        """
        max_words = 0

        for sentence in sentences:
            words = sentence.split()
            max_words = max(max_words, len(words))

        return max_words


# Test driver
def main():
    # Test cases
    test_cases = [
        {
            'sentences': ["alice and bob love leetcode", "i think so too", "this is great thanks very much"],
            'expected': 6
        },
        {
            'sentences': ["please wait", "continue to fight", "continue to win"],
            'expected': 3
        },
        {
            'sentences': ["hello world", "hello worlddd", "hello"],
            'expected': 2
        }
    ]

    solution = Solution()

    for i, test in enumerate(test_cases, 1):
        result = solution.mostWordsFound(test['sentences'])
        status = "PASSED" if result == test['expected'] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Input: sentences = {test['sentences']}")
        print(f"Output: {result}")
        print(f"Expected: {test['expected']}\n")


if __name__ == "__main__":
    main()
