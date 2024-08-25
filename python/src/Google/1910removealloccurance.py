class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Loop until the substring 'part' is no longer found in 's'
        while part in s:
            # Replace the first occurrence of 'part' with an empty string
            s = s.replace(part, "", 1)
        return s


# Example usage
solution = Solution()
s = "daabcbaabcbc"
part = "abc"
print(solution.removeOccurrences(s, part))  # Output: "dab"
