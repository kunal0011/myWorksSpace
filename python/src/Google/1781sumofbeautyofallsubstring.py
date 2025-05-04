"""
LeetCode 1781. Sum of Beauty of All Substrings

Problem Statement:
The beauty of a string is the difference between the frequencies of the most frequent and least
frequent characters (the frequency of a character is the number of times it appears in the string).
For example, the beauty of "abaacc" is 2 - 1 = 1, since 'a' appears 3 times and 'b' and 'c' appear once.
Given a string s, return the sum of beauty of all its substrings.

Time Complexity: O(n^2 * k) where n is length of string and k is size of character set
Space Complexity: O(k) where k is size of character set (26 for lowercase letters)
"""


class Solution:
    def beautySum(self, s: str) -> int:
        # Logic:
        # 1. For each possible substring (using two pointers i,j):
        #    - Keep track of character frequencies in current substring
        #    - Find max and min frequencies (excluding zero frequencies)
        #    - Add difference (beauty) to total sum
        # 2. Return total sum of beauty values

        total_beauty = 0

        # Consider each possible starting point for the substring
        for i in range(len(s)):
            # To store the frequency of each character in the current substring
            freq = [0] * 26

            # Consider each possible ending point for the substring
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord('a')] += 1

                max_freq = max(freq)
                min_freq = min(f for f in freq if f > 0)

                # Calculate beauty of the current substring and add it to total_beauty
                total_beauty += (max_freq - min_freq)

        return total_beauty


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        "aabcb",     # Expected: 5
        "aabcbaa",   # Expected: 17
        "abcdef",    # Expected: 0
        "aaac"       # Expected: 3
    ]

    for i, test_str in enumerate(test_cases):
        result = solution.beautySum(test_str)
        print(f"Test case {i + 1}:")
        print(f"String: {test_str}")
        print(f"Sum of beauty: {result}")

        # Print all substrings and their beauty for verification
        print("Substrings and their beauty values:")
        for start in range(len(test_str)):
            for end in range(start + 1, len(test_str)):
                substr = test_str[start:end + 1]
                freq = {}
                for c in substr:
                    freq[c] = freq.get(c, 0) + 1
                if freq:
                    beauty = max(freq.values()) - min(freq.values())
                    print(f"'{substr}': {beauty}")
        print()
