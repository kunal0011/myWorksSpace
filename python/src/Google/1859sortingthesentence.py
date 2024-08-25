class Solution:
    def sortSentence(self, s: str) -> str:
        # Split the sentence into words
        words = s.split()

        # Sort the words based on the numerical index at the end of each word
        sorted_words = sorted(words, key=lambda word: int(word[-1]))

        # Remove the numerical index and join the words into a sentence
        sorted_sentence = " ".join(word[:-1] for word in sorted_words)

        return sorted_sentence


# Example usage
solution = Solution()
s = "is2 sentence4 This1 a3"
print(solution.sortSentence(s))  # Output: "This is a sentence"
