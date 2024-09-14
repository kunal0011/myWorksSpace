from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Convert list of indices to set for fast lookup
        space_set = set(spaces)

        # Build the result string with spaces
        result = []
        for i in range(len(s)):
            if i in space_set:
                result.append(' ')
            result.append(s[i])

        return ''.join(result)


# Example usage
sol = Solution()
# Output: "this is a very long string"
print(sol.addSpaces("thisisaverylongstring", [4, 7, 9, 15, 19]))
