"""
LeetCode 451 - Sort Characters By Frequency

Problem Statement:
-----------------
Given a string s, sort it in decreasing order based on the frequency of the characters.
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Key Points:
----------
1. Sort characters by frequency in descending order
2. If frequencies are equal, any order is acceptable
3. Case sensitive ('A' != 'a')
4. Can return any valid answer if multiple exist
5. Must handle special characters and spaces

Examples:
--------
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' should appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Constraints:
-----------
* 1 <= s.length <= 5 * 10^5
* s consists of uppercase and lowercase English letters and digits
"""

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Sort string characters by their frequency in descending order.
        
        Algorithm:
        1. Count frequency of each character using Counter
        2. Sort characters by frequency (descending)
        3. Build result string by repeating each char by its frequency
        
        Time Complexity: O(n log k) where n is string length, k is unique chars
        Space Complexity: O(k) for Counter and sorted list
        """
        # Count character frequencies
        char_freq = Counter(s)
        
        # Sort characters by frequency in descending order
        # Using negative frequency for descending sort
        sorted_chars = sorted(char_freq, key=lambda x: (-char_freq[x], x))
        
        # Build result by repeating each char by its frequency
        return ''.join(char * char_freq[char] for char in sorted_chars)


def test_frequency_sort():
    """
    Test driver for character frequency sorting
    """
    test_cases = [
        (
            "tree",
            ["eert", "eetr"]  # Multiple valid answers
        ),
        (
            "cccaaa",
            ["cccaaa", "aaaccc"]  # Equal frequencies
        ),
        (
            "Aabb",
            ["bbAa", "bbaA", "bbAa"]  # Case sensitive sorting
        ),
        (
            "2a554442f544asfasssffasss",
            # Multiple valid answers for complex case
            ["sssssssffffff44444aaaa2552"]
        ),
        (
            "loveleetcode",
            ["eeeeoollvtcd"]  # Mix of different frequencies
        ),
        (
            "12345",
            ["12345", "54321", "23451"]  # All frequencies = 1
        ),
        (
            "aaa",
            ["aaa"]  # Single character repeated
        ),
        (
            "    *",
            ["    *", "*    "]  # Special characters and spaces
        )
    ]
    
    solution = Solution()
    
    for i, (input_str, valid_outputs) in enumerate(test_cases, 1):
        result = solution.frequencySort(input_str)
        
        # Verify frequencies match with any valid output
        is_valid = False
        for valid in valid_outputs:
            if sorted(Counter(result).items()) == sorted(Counter(valid).items()):
                is_valid = True
                break
                
        status = "PASSED" if is_valid else "FAILED"
        print(f"Test case {i}: {status}")
        print(f"Input string: {input_str}")
        print(f"Got: {result}")
        print(f"Valid outputs: {valid_outputs}")
        
        # Additional validation for character grouping
        char_groups = {}
        prev_char = result[0]
        curr_count = 1
        is_grouped = True
        
        for c in result[1:]:
            if c == prev_char:
                curr_count += 1
            else:
                char_groups[prev_char] = curr_count
                prev_char = c
                curr_count = 1
        char_groups[prev_char] = curr_count
        
        # Check if same characters are grouped together
        freq_count = Counter(input_str)
        is_grouped = all(char_groups[char] == freq_count[char] for char in char_groups)
        
        if not is_grouped:
            print("Warning: Characters are not properly grouped!")
        print("-" * 40)

if __name__ == "__main__":
    test_frequency_sort()
