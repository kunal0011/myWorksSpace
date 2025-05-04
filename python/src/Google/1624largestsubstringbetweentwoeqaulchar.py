"""
LeetCode 1624. Largest Substring Between Two Equal Characters

Problem Statement:
Given a string s, return the length of the longest substring between two equal characters,
excluding the two characters. If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string.

Time Complexity: O(n) where n is length of string
Space Complexity: O(k) where k is size of character set
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # Logic:
        # 1. Use dictionary to store first occurrence of each character
        # 2. When we find same character again:
        #    - Calculate length between current position and first occurrence
        #    - Update max_length if current length is larger
        # 3. Return -1 if no equal characters found
        
        # Dictionary to store the first occurrence of each character
        first_occurrence = {}
        max_length = -1

        # Traverse the string
        for i, char in enumerate(s):
            # If the character has been seen before
            if char in first_occurrence:
                # Calculate the length of the substring between two equal characters
                current_length = i - first_occurrence[char] - 1
                # Update max_length if the current length is larger
                max_length = max(max_length, current_length)
            else:
                # Store the first occurrence of the character
                first_occurrence[char] = i

        return max_length


# Test driver
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        "abca",         # Expected: 2 (between 'a' and 'a')
        "aa",           # Expected: 0 (empty string between two 'a's)
        "abcd",         # Expected: -1 (no equal characters)
        "cabbac",       # Expected: 4 (between first and last 'c')
        "mgntdygtxrvxjnwksqhxuxtrv"  # Expected: 18
    ]
    
    for i, test_str in enumerate(test_cases):
        result = solution.maxLengthBetweenEqualCharacters(test_str)
        print(f"Test case {i + 1}:")
        print(f"String: {test_str}")
        print(f"Longest substring length: {result}")
        if result >= 0:
            # Find the characters that give this result
            for j in range(len(test_str)):
                for k in range(j+1, len(test_str)):
                    if test_str[j] == test_str[k] and k-j-1 == result:
                        print(f"Found between positions {j} and {k} (char: '{test_str[j]}')")
                        break
        print()
