from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)
        length = 0
        odd_found = False

        for count in char_count.values():
            if count % 2 == 0:
                length += count  # Add even counts directly
            else:
                length += count - 1  # Add the largest even part of odd counts
                odd_found = True  # Remember that we found an odd count

        if odd_found:
            length += 1  # Add one more for the center of the palindrome

        return length


# Example usage:
solution = Solution()
print(solution.longestPalindrome("abccccdd"))  # Expected output: 7
print(solution.longestPalindrome("a"))          # Expected output: 1
print(solution.longestPalindrome("aaabbbccc"))  # Expected output: 7
