from typing import List


class Solution:
    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        n = len(target)

        # Filter out dictionary words with the same length as target
        dictionary = [word for word in dictionary if len(word) == n]

        # If no conflicting words, return the full abbreviation (target itself)
        if not dictionary:
            return str(n)

        # Helper function to get the bitmask for the word
        def getBitMask(word):
            bitmask = 0
            for i in range(n):
                if target[i] != word[i]:
                    bitmask |= 1 << (n - 1 - i)
            return bitmask

        # Get bitmasks for all dictionary words
        dictMasks = [getBitMask(word) for word in dictionary]

        # Function to check if an abbreviation with the bitmask is valid (no conflicts)
        def valid(mask):
            for dm in dictMasks:
                if dm & mask == 0:
                    return False
            return True

        # Generate all possible abbreviations and return the minimum valid one
        def dfs(start, curLen, mask):
            if start == n:
                return (curLen, mask)
            res = dfs(start + 1, curLen + 1, mask)
            for end in range(start + 1, n + 1):
                newMask = mask | ((1 << (n - start)) - (1 << (n - end)))
                res = min(res, dfs(end, curLen + 1, newMask))
            return res

        return dfs(0, 0, 0)
