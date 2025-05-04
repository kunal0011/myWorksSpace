"""
LeetCode 1859. Sorting the Sentence

Problem Statement:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each word consists of lowercase and uppercase English letters and a single digit from 1-9 that indicates its position.
The digits do not appear in order. You need to sort the words and remove the digits to restore the original sentence.
Return the restored sentence.

Time Complexity: O(nlogn) where n is number of words
Space Complexity: O(n) for storing words
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        # Logic:
        # 1. Split sentence into words
        # 2. Sort words based on the digit at end (word[-1])
        # 3. Remove digits and join words with spaces

        # Split the sentence into words
        words = s.split()

        # Sort the words based on the numerical index at the end of each word
        sorted_words = sorted(words, key=lambda word: int(word[-1]))

        # Remove the numerical index and join the words into a sentence
        sorted_sentence = " ".join(word[:-1] for word in sorted_words)

        return sorted_sentence


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        "is2 sentence4 This1 a3",               # Expected: "This is a sentence"
        "Myself2 Me1 I4 and3",                  # Expected: "Me Myself and I"
        "Love3 Coding4 I2 Love1",               # Expected: "Love I Love Coding"
        "This4 combination3 random1 is2",       # Expected: "random is combination This"
    ]

    for i, test_str in enumerate(test_cases):
        result = solution.sortSentence(test_str)
        print(f"Test case {i + 1}:")
        print(f"Scrambled sentence: {test_str}")
        print(f"Restored sentence: {result}")

        # Show word positions for verification
        words = test_str.split()
        positions = [(word[:-1], int(word[-1])) for word in words]
        print("Word positions:")
        for word, pos in sorted(positions, key=lambda x: x[1]):
            print(f"  Position {pos}: {word}")
        print()
