from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # Convert list to set for O(1) lookups
        memo = {}  # To store the results of substrings

        def backtrack(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                # Base case: empty sentence if we have reached the end
                return [""]

            result = []
            for end in range(index + 1, len(s) + 1):
                word = s[index:end]
                if word in word_set:
                    # Recursively call backtrack for the remaining substring
                    sub_sentences = backtrack(end)
                    for sentence in sub_sentences:
                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)

            memo[index] = result
            return result

        return backtrack(0)
