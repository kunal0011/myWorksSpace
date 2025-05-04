"""
LeetCode 748: Shortest Completing Word

Problem Statement:
Given a string licensePlate and an array of strings words, find the shortest completing word in words.
A completing word is a word that contains all the letters in licensePlate (ignoring numbers and spaces).
Letters in licensePlate are case insensitive. If there are multiple shortest completing words, return the first one.

Logic:
1. Clean the license plate:
   - Convert to lowercase
   - Remove non-alphabetic characters
   - Create character frequency counter
2. For each word in words:
   - Convert to lowercase
   - Create character frequency counter
   - Check if word contains all chars from license plate
3. Track shortest valid word found so far
4. Return shortest word that completes the license plate

Time Complexity: O(n * k) where n is number of words and k is average word length
Space Complexity: O(1) since character counter is bounded by alphabet size
"""

from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Step 1: Clean license plate and create character frequency
        license_chars = Counter(char.lower()
                                for char in licensePlate if char.isalpha())

        shortest_word = None
        shortest_length = float('inf')

        # Step 2: Check each word
        for word in words:
            word_lower = word.lower()

            # Check if word contains all required characters
            is_valid = True
            word_counter = Counter(word_lower)

            for char, count in license_chars.items():
                if word_counter[char] < count:
                    is_valid = False
                    break

            # Update shortest word if current word is valid and shorter
            if is_valid and len(word) < shortest_length:
                shortest_word = word
                shortest_length = len(word)

        return shortest_word


def test_shortest_completing_word():
    solution = Solution()

    # Test case 1: Basic case
    plate1 = "1s3 PSt"
    words1 = ["step", "steps", "stripe", "stepple"]
    result1 = solution.shortestCompletingWord(plate1, words1)
    assert result1 == "steps", f"Test case 1 failed. Expected 'steps', got {result1}"
    print(f"Test case 1 passed: plate={plate1}, result={result1}")

    # Test case 2: Multiple valid words, return shortest
    plate2 = "1s3 456"
    words2 = ["looks", "pest", "stew", "show"]
    result2 = solution.shortestCompletingWord(plate2, words2)
    assert result2 == "pest", f"Test case 2 failed. Expected 'pest', got {result2}"
    print(f"Test case 2 passed: plate={plate2}, result={result2}")

    # Test case 3: Case insensitive matching
    plate3 = "GrC"
    words3 = ["car", "racing", "gRaCe"]
    result3 = solution.shortestCompletingWord(plate3, words3)
    assert result3 == "grace", f"Test case 3 failed. Expected 'grace', got {result3}"
    print(f"Test case 3 passed: plate={plate3}, result={result3}")

    # Test case 4: Same length words, return first match
    plate4 = "Ah71752"
    words4 = ["heart", "house", "happy"]
    result4 = solution.shortestCompletingWord(plate4, words4)
    assert result4 == "heart", f"Test case 4 failed. Expected 'heart', got {result4}"
    print(f"Test case 4 passed: plate={plate4}, result={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_shortest_completing_word()
