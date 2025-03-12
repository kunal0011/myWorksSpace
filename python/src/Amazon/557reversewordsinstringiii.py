"""
LeetCode 557 - Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Example 2:
Input: s = "God Ding"
Output: "doG gniD"

Constraints:
- 1 <= s.length <= 5 * 10^4
- s contains printable ASCII characters.
- s does not contain any leading or trailing spaces.
- There is at least one word in s.
- All the words in s are separated by a single space.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Optimized solution using Python's built-in functions and string slicing
        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(n) for the output string
        """
        # Split the string into words, reverse each word, and join back
        return ' '.join(word[::-1] for word in s.split())
    
    def reverseWords_manual(self, s: str) -> str:
        """
        Alternative manual implementation without using built-in split/join
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        def reverse_word(s: str, start: int, end: int) -> str:
            chars = list(s[start:end])
            left, right = 0, len(chars) - 1
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            return ''.join(chars)
        
        result = []
        word_start = 0
        n = len(s)
        
        for i in range(n):
            if s[i] == ' ':
                result.append(reverse_word(s, word_start, i))
                result.append(' ')
                word_start = i + 1
        
        # Handle the last word
        result.append(reverse_word(s, word_start, n))
        return ''.join(result)


def test_reverse_words():
    """
    Test function to verify both solution approaches with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
        ("God Ding", "doG gniD"),
        
        # Edge cases
        ("a", "a"),  # Single character
        ("ab", "ba"),  # Two characters
        ("hello", "olleh"),  # Single word
        
        # Complex test cases
        ("Alice was beginning", "ecilA saw gninnigeb"),
        ("I love programming", "I evol gnimmargorp"),
        ("The quick brown fox", "ehT kciuq nworb xof"),
        
        # Special characters
        ("Hello123 World456!", "321olleH 654dlroW!"),
        ("Test-case", "esac-tseT"),
        
        # Multiple spaces (though not in constraints, good to test)
        ("hello world", "olleh dlrow")
    ]
    
    print("Running tests for Reverse Words in a String III...\n")
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.reverseWords(input_str)
        result2 = solution.reverseWords_manual(input_str)
        
        print(f"Test Case {i}:")
        print(f"Input: '{input_str}'")
        print(f"Expected: '{expected}'")
        print(f"Built-in Solution: '{result1}' {'✅' if result1 == expected else '❌'}")
        print(f"Manual Solution: '{result2}' {'✅' if result2 == expected else '❌'}")
        
        if result1 != expected or result2 != expected:
            print("❌ Test case failed!")
            if result1 != expected:
                print(f"Built-in solution failed. Got: '{result1}', Expected: '{expected}'")
            if result2 != expected:
                print(f"Manual solution failed. Got: '{result2}', Expected: '{expected}'")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_reverse_words()