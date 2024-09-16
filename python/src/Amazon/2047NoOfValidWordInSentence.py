import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        def is_valid(word: str) -> bool:
            # Check if the word matches the valid word conditions
            return bool(re.match(r"^[a-z]*([a-z]-[a-z])?[a-z]*[!.,]?$", word))

        words = sentence.split()
        valid_count = 0

        for word in words:
            if is_valid(word):
                valid_count += 1

        return valid_count


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    sentence = "cat and  dog"
    print("Valid Words Count:", solution.countValidWords(
        sentence))  # Expected output: 3
