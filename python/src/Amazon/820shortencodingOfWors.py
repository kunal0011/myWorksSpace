class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        # Sort words by length in descending order
        words = sorted(set(words), key=lambda w: -len(w))
        encoding = ""

        for word in words:
            if word + '#' not in encoding:
                encoding += word + '#'

        return len(encoding)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    words1 = ["time", "me", "bell"]
    # Expected output: 10 ("time#bell#")
    print(sol.minimumLengthEncoding(words1))

    # Test case 2
    words2 = ["t"]
    print(sol.minimumLengthEncoding(words2))  # Expected output: 2 ("t#")
