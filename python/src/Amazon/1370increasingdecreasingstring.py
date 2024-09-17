from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        # Count the frequency of each character
        char_count = Counter(s)
        result = []

        while len(result) < len(s):
            # Pick characters in increasing order
            for char in sorted(char_count):
                if char_count[char] > 0:
                    result.append(char)
                    char_count[char] -= 1

            # Pick characters in decreasing order
            for char in sorted(char_count, reverse=True):
                if char_count[char] > 0:
                    result.append(char)
                    char_count[char] -= 1

        return ''.join(result)


# Testing
solution = Solution()
s = "aaaabbbbcccc"
print("Python Test Result:", solution.sortString(s))  # Output: "abccbaabccba"
