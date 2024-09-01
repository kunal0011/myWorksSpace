class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0

        # Iterate through each word in the list
        for word in words:
            # Check if the word starts with the given prefix
            if word.startswith(pref):
                count += 1

        return count
