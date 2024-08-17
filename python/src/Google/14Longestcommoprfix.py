from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Assume the first string is the common prefix initially
        prefix = strs[0]

        for i in range(len(prefix)):
            for string in strs:
                # Check if the current index is within the bounds of the string
                if i >= len(string) or string[i] != prefix[i]:
                    # Mismatch found or index is out of bounds
                    return prefix[:i]

        return prefix
