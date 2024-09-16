class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Keep removing the substring 'part' from 's' until it no longer appears
        while part in s:
            s = s.replace(part, '', 1)  # Replace only one occurrence at a time
        return s


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    s = "daabcbaabcbc"
    part = "abc"
    print("Final string:", solution.removeOccurrences(
        s, part))  # Expected output: "dab"
