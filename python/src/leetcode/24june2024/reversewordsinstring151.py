class Solution:
    def reverseWords(self, s: str) -> str:
        # Split the string by whitespace and filter out empty strings
        words = s.split()

        # Reverse the list of words
        words.reverse()

        # Join the words into a single string with single space separator
        return ' '.join(words)


sol = Solution()
print(sol.reverseWords("the sky is blue"))      # Output: "blue is sky the"
print(sol.reverseWords("  hello world  "))      # Output: "world hello"
print(sol.reverseWords("a good   example"))    # Output: "example good a"
