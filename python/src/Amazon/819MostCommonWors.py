import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # Step 1: Preprocess the paragraph - remove punctuation and make everything lowercase
        words = re.findall(r'\w+', paragraph.lower())

        # Step 2: Create a set of banned words for fast lookup
        banned_set = set(banned)

        # Step 3: Count the frequency of each word, excluding banned words
        word_count = Counter(word for word in words if word not in banned_set)

        # Step 4: Find the most common word
        return word_count.most_common(1)[0][0]


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    paragraph1 = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned1 = ["hit"]
    print(sol.mostCommonWord(paragraph1, banned1))  # Expected output: "ball"

    # Test case 2
    paragraph2 = "a."
    banned2 = []
    print(sol.mostCommonWord(paragraph2, banned2))  # Expected output: "a"
