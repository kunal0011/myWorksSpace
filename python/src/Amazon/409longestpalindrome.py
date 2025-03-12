"""
LeetCode 409: Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length
of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) since we only store at most 52 characters (26 lowercase + 26 uppercase)
"""
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Find the length of longest palindrome that can be formed using characters in s.
        
        Args:
            s: Input string containing uppercase and lowercase English letters
        Returns:
            Length of the longest possible palindrome
        """
        # Count frequency of each character
        char_count = Counter(s)
        
        # Initialize result and odd_count flag
        length = 0
        has_odd = False
        
        # Process each character count
        for count in char_count.values():
            # Add even counts directly
            length += (count // 2) * 2
            # Check if we have any odd count
            if count % 2:
                has_odd = True
        
        # If we found any character with odd count, we can use one at center
        return length + (1 if has_odd else 0)


def run_test_cases():
    """Test driver with various test cases"""
    solution = Solution()
    
    # Test cases: (input string, expected output)
    test_cases = [
        ("abccccdd", 7),          # Example 1: can form "dccaccd"
        ("a", 1),                 # Single character
        ("", 0),                  # Empty string
        ("AA", 2),                # Same uppercase chars
        ("aA", 1),                # Case sensitive
        ("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth", 983),  # Long string
        ("racecar", 7),           # Already a palindrome
        ("zzzzzz", 6),           # All same characters
        ("aabbccddee", 10)       # All pairs
    ]
    
    passed = 0
    total = len(test_cases)
    
    print("\nRunning test cases for Longest Palindrome:")
    print("=" * 50)
    
    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = solution.longestPalindrome(test_input)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test case {i}:")
        print(f"Input: {test_input[:50] + '...' if len(test_input) > 50 else test_input}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Status: {status}")
        print("-" * 30)
        
        if status == "PASSED":
            passed += 1
    
    print(f"\nSummary: {passed}/{total} test cases passed")


if __name__ == "__main__":
    run_test_cases()