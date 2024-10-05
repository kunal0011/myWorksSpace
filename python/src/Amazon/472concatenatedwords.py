class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        word_set = set(words)
        concatenated_words = []

        def canForm(word):
            if word in word_set:
                return True
            dp = [False] * (len(word) + 1)
            dp[0] = True  # Empty string can be formed

            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in word_set:
                        dp[i] = True
                        break
            return dp[-1]

        for word in words:
            word_set.remove(word)
            if canForm(word):
                concatenated_words.append(word)
            word_set.add(word)

        return concatenated_words
