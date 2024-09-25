class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result = []

        # Iterate over each word and check if it's a substring of any other word
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break  # No need to check further if it's already a substring

        return result
