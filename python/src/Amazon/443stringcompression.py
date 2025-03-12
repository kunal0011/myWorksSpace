"""
LeetCode 443 - String Compression

Problem Statement:
-----------------
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:
- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string s should not be returned separately, but instead, be stored in the 
input character array chars. Note that group lengths that are 10 or longer will be split 
into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

Key Points:
----------
1. Must modify input array in-place
2. Return the new length of modified array
3. Handle groups of consecutive characters
4. Numbers > 9 must be split into individual digits
5. Use O(1) extra space

Examples:
--------
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of chars should be: ["a","2","b","2","c","3"]

Input: chars = ["a"]
Output: Return 1, and the first character of chars should be: ["a"]

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of chars should be: ["a","b","1","2"]

Constraints:
-----------
* 1 <= chars.length <= 2000
* chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol
"""

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Compress the input array in-place and return the new length.
        
        Algorithm:
        1. Use two pointers: read (for reading groups) and write (for writing compressed result)
        2. Count consecutive characters using read pointer
        3. Write character and count (if > 1) using write pointer
        4. Handle multi-digit counts by converting to string
        
        Time Complexity: O(n) where n is length of input array
        Space Complexity: O(1) as we modify array in-place
        """
        write = 0  # Position to write compressed characters
        read = 0   # Position to read original characters

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count consecutive occurrences of current character
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write


def test_compress():
    """
    Test driver for string compression problem
    """
    test_cases = [
        (
            ["a","a","b","b","c","c","c"],
            6,
            ["a","2","b","2","c","3"]  # Expected first 6 chars
        ),
        (
            ["a"],
            1,
            ["a"]  # Single character case
        ),
        (
            ["a","b","b","b","b","b","b","b","b","b","b","b","b"],
            4,
            ["a","b","1","2"]  # Case with double-digit count
        ),
        (
            ["a","a","a","b","b","a","a"],
            6,
            ["a","3","b","2","a","2"]  # Multiple groups of same character
        ),
        (
            ["a","b","c"],
            3,
            ["a","b","c"]  # No compression needed
        ),
        (
            ["a","a","a","a","a","a","a","a","a","a"],
            3,
            ["a","1","0"]  # Exactly 10 characters
        ),
        (
            ["#","#","#","$","$","@"],
            5,
            ["#","3","$","2","@"]  # Special characters
        ),
        (
            ["A","A","A","A","B","B","B"],
            5,
            ["A","4","B","3"]  # Uppercase letters
        )
    ]
    
    solution = Solution()
    
    for i, (input_chars, expected_len, expected_chars) in enumerate(test_cases, 1):
        # Create a copy as the function modifies input
        chars = input_chars.copy()
        result_len = solution.compress(chars)
        
        # Verify length and content
        is_length_correct = result_len == expected_len
        is_content_correct = chars[:result_len] == expected_chars
        status = "PASSED" if is_length_correct and is_content_correct else "FAILED"
        
        print(f"Test case {i}: {status}")
        print(f"Input: {input_chars}")
        print(f"Expected length: {expected_len}")
        print(f"Got length: {result_len}")
        print(f"Expected first {expected_len} chars: {expected_chars}")
        print(f"Got first {result_len} chars: {chars[:result_len]}")
        print("-" * 40)

if __name__ == "__main__":
    test_compress()
