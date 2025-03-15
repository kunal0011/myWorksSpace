"""
LeetCode 880: Decoded String at Index

You are given an encoded string s and a target index k. The encoding rule is:
- If a character is a letter, it remains unchanged
- If a character is a digit (2-9), it repeats the string up to that point that many times

Return the kth letter (1-indexed) in the decoded string.

Constraints:
- 2 <= s.length <= 100
- s consists of lowercase English letters and digits 2-9
- s starts with a letter
- 1 <= k <= 10^9
"""

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        
        # Calculate size of decoded string
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1
                
        # Work backwards from k
        for char in reversed(s):
            k %= size  # Get position within current segment
            
            if k == 0 and char.isalpha():
                return char
                
            if char.isdigit():
                size //= int(char)
            else:
                size -= 1

def validate_input(s: str, k: int) -> bool:
    """Validate input according to constraints"""
    if not (2 <= len(s) <= 100):
        return False
    if not s[0].isalpha():
        return False
    if not all(c.isalpha() or (c.isdigit() and '2' <= c <= '9') for c in s):
        return False
    if not 1 <= k <= 10**9:
        return False
    return True

def test_decoded_string():
    """Test function for Decoded String at Index"""
    test_cases = [
        ("leet2code3", 10, "o"),
        ("ha22", 5, "h"),
        ("a2345678999999999999999", 1, "a"),
        ("abc3", 6, "c"),
        ("abc2def3", 14, "e"),
        ("y959q969u3hb22odq595", 222280369, "y")
    ]
    
    solution = Solution()
    
    for i, (s, k, expected) in enumerate(test_cases, 1):
        is_valid = validate_input(s, k)
        
        print(f"\nTest case {i}:")
        print(f"Encoded string: {s}")
        print(f"Target index k: {k}")
        
        if is_valid:
            result = solution.decodeAtIndex(s, k)
            print(f"Expected: {expected}")
            print(f"Result: {result}")
            print(f"Test passed: {'✓' if result == expected else '✗'}")
            
            # Show decoding process for small strings
            if len(s) < 10:
                decoded = ""
                for char in s:
                    if char.isdigit():
                        decoded = decoded * int(char)
                    else:
                        decoded += char
                    print(f"After processing '{char}': {decoded[:20]}{'...' if len(decoded) > 20 else ''}")
        
        print(f"Valid input: {'✓' if is_valid else '✗'}")

if __name__ == "__main__":
    test_decoded_string()
