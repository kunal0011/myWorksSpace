"""
LeetCode 1446. Consecutive Characters

Problem Statement:
The power of the string is the maximum length of a non-empty substring that contains only one unique character.
Given a string s, return the power of s.

Time Complexity: O(n) where n is the length of string
Space Complexity: O(1) as we only use two variables
"""


class Solution:
    def maxPower(self, s: str) -> int:
        # Logic:
        # 1. Keep track of current consecutive character count (current_len)
        # 2. Keep track of maximum consecutive count seen so far (max_len)
        # 3. Iterate through string:
        #    - If current char matches previous, increment current_len
        #    - If different, update max_len if needed and reset current_len
        # 4. Final check for last sequence

        # Initialize max_len and current_len
        max_len = 1
        current_len = 1

        # Iterate over the string starting from the second character
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current_len += 1
            else:
                # Update the max_len and reset current_len
                max_len = max(max_len, current_len)
                current_len = 1

        # Final check to ensure we account for the last sequence
        return max(max_len, current_len)


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        "leetcode",          # Expected output: 2 (ee)
        "abbcccddddeeeeedcba",  # Expected output: 5 (eeeee)
        "triplepillooooow",  # Expected output: 5 (ooooo)
        "hooraaaaaaaaaaay",  # Expected output: 11 (aaaaaaaaaaa)
        "tourist"            # Expected output: 1 (each character appears once)
    ]

    for i, test_case in enumerate(test_cases):
        result = solution.maxPower(test_case)
        print(f"Test case {i + 1}:")
        print(f"Input string: {test_case}")
        print(f"Maximum power: {result}")
        print()
