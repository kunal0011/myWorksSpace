class Solution:
    def generateAbbreviations(self, word: str):
        res = []

        def backtrack(pos, current, count):
            # If we've processed all characters in the word
            if pos == len(word):
                # If count is not zero, append it to the result
                if count > 0:
                    current += str(count)
                res.append(current)
                return

            # Option 1: Abbreviate the current character (increase count)
            backtrack(pos + 1, current, count + 1)

            # Option 2: Don't abbreviate, add the count and the character to the result
            if count > 0:
                current += str(count)
            backtrack(pos + 1, current + word[pos], 0)

        backtrack(0, "", 0)
        return res
