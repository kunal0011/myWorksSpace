"""
LeetCode 917: Reverse Only Letters

Given a string s, reverse the string according to the following rules:
- All the characters that are not English letters remain in the same position.
- All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Constraints:
- 1 <= s.length <= 100
- s consists of characters with ASCII values in [33, 122]
- s does not contain '\"' or '\\'
"""

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # Convert to list for O(1) character updates
        chars = list(s)
        left, right = 0, len(s) - 1
        
        while left < right:
            # Find leftmost letter
            while left < right and not chars[left].isalpha():
                left += 1
            # Find rightmost letter
            while left < right and not chars[right].isalpha():
                right -= 1
            # Swap letters
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
            
        return ''.join(chars)

def validate_string(s: str) -> bool:
    """Validate string according to constraints"""
    if not 1 <= len(s) <= 100:
        return False
    return all(33 <= ord(c) <= 122 for c in s) and '"\\' not in s

def test_reverse_letters():
    """Test function for Reverse Only Letters"""
    test_cases = [
        ("ab-cd", "dc-ba"),
        ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),
        ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntseT!"),
        ("7_28]", "7_28]"),
        ("?6C40E", "?6E40C"),
        ("abcde", "edcba")
    ]
    
    solution = Solution()
    
    for i, (s, expected) in enumerate(test_cases, 1):
        is_valid = validate_string(s)
        result = solution.reverseOnlyLetters(s)
        
        print(f"\nTest case {i}:")
        print(f"Input string: {s}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result == expected else '✗'}")
        
        # Additional analysis
        letters = [c for c in s if c.isalpha()]
        non_letters = [c for c in s if not c.isalpha()]
        
        print("\nCharacter analysis:")
        print(f"Total length: {len(s)}")
        print(f"Letters: {len(letters)} ({', '.join(letters)})")
        print(f"Non-letters: {len(non_letters)} ({', '.join(non_letters)})")
        
        # Verify letter positions are reversed but non-letters stay
        result_letters = [c for c in result if c.isalpha()]
        result_non_letters = [c for c in result if not c.isalpha()]
        print("\nVerification:")
        print(f"Letters reversed: {'✓' if result_letters == letters[::-1] else '✗'}")
        print(f"Non-letters unchanged: {'✓' if result_non_letters == non_letters else '✗'}")

if __name__ == "__main__":
    test_reverse_letters()
