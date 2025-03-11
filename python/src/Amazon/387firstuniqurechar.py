"""
LeetCode 387: First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation: The first non-repeating character is 'l' at index 0.

Example 2:
Input: s = "loveleetcode"
Output: 2
Explanation: The first non-repeating character is 'v' at index 2.

Example 3:
Input: s = "aabb"
Output: -1
Explanation: There are no non-repeating characters, so return -1.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) since we store at most 26 characters
"""

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Find the index of first non-repeating character using a counter.
        
        Args:
            s (str): Input string
            
        Returns:
            int: Index of first unique character, or -1 if none exists
        """
        # Create counter for character frequencies
        # Using Counter is more efficient than manual dictionary creation
        char_count = Counter(s)
        
        # Find first character with count 1
        # Enumerate gives us both index and character
        for idx, char in enumerate(s):
            if char_count[char] == 1:
                return idx
        
        return -1
    
    def firstUniqChar_alternative(self, s: str) -> int:
        """
        Alternative implementation using array for better memory usage.
        This might be faster for very large strings with small alphabet.
        
        Args:
            s (str): Input string
            
        Returns:
            int: Index of first unique character, or -1 if none exists
        """
        # Initialize count array for lowercase English letters
        count = [0] * 26
        
        # Count frequencies
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Find first unique character
        for idx, char in enumerate(s):
            if count[ord(char) - ord('a')] == 1:
                return idx
        
        return -1


def run_test_cases() -> None:
    """Function to run comprehensive test cases"""
    solution = Solution()
    
    # Test case 1: Basic case
    test_cases = [
        ("leetcode", 0, "First character 'l' is unique"),
        ("loveleetcode", 2, "First unique character 'v' is at index 2"),
        ("aabb", -1, "No unique characters"),
        ("", -1, "Empty string"),
        ("cc", -1, "All characters repeated"),
        ("dddccdbba", 8, "Last character is unique"),
        ("aadadaad", -1, "Multiple repeated characters"),
        ("z", 0, "Single character"),
        ("zz", -1, "Single repeated character"),
        ("abcdefg", 0, "All unique characters")
    ]
    
    # Test both implementations
    implementations = [
        (solution.firstUniqChar, "Counter implementation"),
        (solution.firstUniqChar_alternative, "Array implementation")
    ]
    
    for impl_func, impl_name in implementations:
        print(f"\nTesting {impl_name}:")
        for s, expected, description in test_cases:
            result = impl_func(s)
            print(f"\nTest Case: {description}")
            print(f"Input: {s}")
            print(f"Expected: {expected}")
            print(f"Got: {result}")
            print(f"Result: {'PASSED' if result == expected else 'FAILED'}")
    
    # Performance comparison test
    print("\nPerformance Test with long string:")
    long_string = "abcdefghijklmnopqrstuvwxyz" * 10000
    
    # Test Counter implementation
    from time import time
    start = time()
    solution.firstUniqChar(long_string)
    counter_time = time() - start
    
    # Test Array implementation
    start = time()
    solution.firstUniqChar_alternative(long_string)
    array_time = time() - start
    
    print(f"Counter implementation time: {counter_time:.4f} seconds")
    print(f"Array implementation time: {array_time:.4f} seconds")


if __name__ == "__main__":
    run_test_cases()