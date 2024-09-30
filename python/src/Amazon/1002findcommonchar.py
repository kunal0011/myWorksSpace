from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        # Initialize the character frequency with the first word
        min_freq = Counter(words[0])

        # For each word, update the min_freq to keep the minimum frequency of each character
        for word in words[1:]:
            word_freq = Counter(word)
            for char in min_freq:
                min_freq[char] = min(min_freq[char], word_freq[char])

        # Now, construct the result based on the minimum frequencies
        result = []
        for char, count in min_freq.items():
            result.extend([char] * count)

        return result

# Testing the implementation


def test_common_chars():
    solution = Solution()

    # Test case 1
    words1 = ["bella", "label", "roller"]
    # Expected output: ['e', 'l', 'l']
    result1 = solution.commonChars(words1)
    print(f"Test 1 - Result: {result1}, Expected: ['e', 'l', 'l']")

    # Test case 2
    words2 = ["cool", "lock", "cook"]
    # Expected output: ['c', 'o']
    result2 = solution.commonChars(words2)
    print(f"Test 2 - Result: {result2}, Expected: ['c', 'o']")

    # Test case 3
    words3 = ["a", "b", "c"]
    # Expected output: [] (No common characters)
    result3 = solution.commonChars(words3)
    print(f"Test 3 - Result: {result3}, Expected: []")


# Run the test
test_common_chars()
