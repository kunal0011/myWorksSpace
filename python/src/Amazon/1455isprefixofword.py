class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()

        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1  # 1-based index

        return -1


# Testing
solution = Solution()
sentence = "i love eating burger"
searchWord = "burg"
print("Python Test Result:", solution.isPrefixOfWord(
    sentence, searchWord))  # Output should be 4
