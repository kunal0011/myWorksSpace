"""
LeetCode 567 - Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Optimized sliding window solution using character frequency counting
        Time Complexity: O(n) where n is the length of s2
        Space Complexity: O(1) since we only store 26 characters at most
        """
        if len(s1) > len(s2):
            return False

        # Create frequency counters for the first window
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Initialize counts for s1 and first window of s2
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
            
        # Check if first window is a permutation
        if s1_count == window_count:
            return True
            
        # Slide the window and update counts
        for i in range(len(s1), len(s2)):
            # Remove count of character going out of window
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            # Add count of character coming into window
            window_count[ord(s2[i]) - ord('a')] += 1
            
            # Check if current window is a permutation
            if s1_count == window_count:
                return True
                
        return False

    def checkInclusion_counter(self, s1: str, s2: str) -> bool:
        """
        Alternative solution using Python's Counter class
        Slightly more readable but potentially less performant
        Time Complexity: O(n) where n is the length of s2
        Space Complexity: O(1) since we only store unique characters
        """
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        window_counter = Counter()
        
        # Initialize first window
        for i in range(len(s1)):
            window_counter[s2[i]] += 1
            
        if window_counter == s1_counter:
            return True
            
        # Slide window
        for i in range(len(s1), len(s2)):
            # Update window counts
            window_counter[s2[i]] += 1
            window_counter[s2[i - len(s1)]] -= 1
            
            # Remove keys with count 0
            if window_counter[s2[i - len(s1)]] == 0:
                del window_counter[s2[i - len(s1)]]
                
            if window_counter == s1_counter:
                return True
                
        return False


def test_check_inclusion():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        
        # Edge cases
        ("a", "a", True),
        ("a", "b", False),
        ("abc", "ab", False),  # s1 longer than s2
        
        # Test cases with repeated characters
        ("aaa", "aaaa", True),
        ("hello", "ooolleoooleh", False),
        
        # Complex test cases
        ("abc", "ccccbbbbaaaa", False),
        ("abc", "bbbca", True),
        ("abc", "cccccbabbbaaaa", True),
        
        # Test cases with all same characters
        ("aaa", "aa", False),
        ("aaa", "aaaa", True),
        
        # Special cases
        ("", "", True),  # Empty strings
        ("ab", "ba", True),  # Exact permutation
        ("abc", "cba", True),  # Reverse permutation
        
        # Longer test cases
        ("abbc", "babcabbcabc", True),
        ("programming", "programmingpro", True)
    ]
    
    print("Running tests for Permutation in String...\n")
    
    for i, (s1, s2, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.checkInclusion(s1, s2)
        result2 = solution.checkInclusion_counter(s1, s2)
        
        print(f"Test Case {i}:")
        print(f"Input: s1 = '{s1}', s2 = '{s2}'")
        print(f"Expected: {expected}")
        print(f"Array Solution: {result1} {'✅' if result1 == expected else '❌'}")
        print(f"Counter Solution: {result2} {'✅' if result2 == expected else '❌'}")
        
        if result1 != expected or result2 != expected:
            print("❌ Test case failed!")
            print(f"Got: {result1} (Array), {result2} (Counter)")
            print(f"Expected: {expected}")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_check_inclusion()
