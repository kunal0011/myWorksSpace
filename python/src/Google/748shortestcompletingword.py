from collections import Counter
from typing import List


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # Step 1: Extract the relevant letters and count their frequencies
        cleaned_license_plate = [char.lower()
                                 for char in licensePlate if char.isalpha()]
        required_counts = Counter(cleaned_license_plate)

        # Step 2: Find the shortest completing word
        shortest_word = None
        for word in words:
            word_counts = Counter(word.lower())
            if all(word_counts[char] >= required_counts[char] for char in required_counts):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word

        return shortest_word


# Example usage
solution = Solution()
licensePlate1 = "1s3 PSt"
words1 = ["step", "steps", "stripe", "stepple"]

licensePlate2 = "1s3 456"
words2 = ["looks", "pest", "stew", "show"]

print(solution.shortestCompletingWord(licensePlate1, words1))  # Output: "steps"
print(solution.shortestCompletingWord(licensePlate2, words2))  # Output: "pest"
