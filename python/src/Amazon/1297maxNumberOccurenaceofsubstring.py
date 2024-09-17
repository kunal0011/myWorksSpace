from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # Dictionary to count occurrences of substrings
        substring_count = defaultdict(int)

        # Traverse the string with a sliding window of size minSize
        for i in range(len(s) - minSize + 1):
            # Get the substring of length minSize
            substring = s[i:i + minSize]

            # Count the number of unique characters in this substring
            unique_chars = set(substring)

            # Only count the substring if it has <= maxLetters unique characters
            if len(unique_chars) <= maxLetters:
                substring_count[substring] += 1

        # Return the maximum frequency of any valid substring
        return max(substring_count.values(), default=0)


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    s1 = "aababcaab"
    maxLetters1 = 2
    minSize1 = 3
    maxSize1 = 4
    result1 = sol.maxFreq(s1, maxLetters1, minSize1, maxSize1)
    assert result1 == 2, f"Test case 1 failed: {result1}"

    # Test case 2
    s2 = "aaaa"
    maxLetters2 = 1
    minSize2 = 3
    maxSize2 = 3
    result2 = sol.maxFreq(s2, maxLetters2, minSize2, maxSize2)
    assert result2 == 2, f"Test case 2 failed: {result2}"

    # Test case 3
    s3 = "abcde"
    maxLetters3 = 2
    minSize3 = 3
    maxSize3 = 3
    result3 = sol.maxFreq(s3, maxLetters3, minSize3, maxSize3)
    assert result3 == 0, f"Test case 3 failed: {result3}"

    print("All test cases passed!")
