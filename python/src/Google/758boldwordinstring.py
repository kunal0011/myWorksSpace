from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n

        # Step 1: Mark the bold intervals
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)

        # Step 2: Construct the result string with <b> tags
        result = []
        i = 0
        while i < n:
            if bold[i]:
                result.append("<b>")
                while i < n and bold[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(s[i])
                i += 1

        return "".join(result)


# Example usage
solution = Solution()
s1 = "abcxyz123"
words1 = ["abc", "123"]

s2 = "aaabbcc"
words2 = ["aaa", "aab", "bc"]

print(solution.addBoldTag(s1, words1))  # Output: "<b>abc</b>xyz<b>123</b>"
print(solution.addBoldTag(s2, words2))  # Output: "<b>aaabbc</b>c"
