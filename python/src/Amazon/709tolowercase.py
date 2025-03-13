"""
LeetCode 709: To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Constraints:
- 1 <= s.length <= 100
- s consists of printable ASCII characters
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        # Original implementation using ASCII manipulation
        result = []
        for char in s:
            if 'A' <= char <= 'Z':
                result.append(chr(ord(char) + 32))
            else:
                result.append(char)
        return ''.join(result)
    
    def toUpperCase_optimized(self, s: str) -> str:
        # Optimized implementation using built-in method
        return s.lower()

def test_toLowerCase():
    import time
    
    test_cases = [
        ("Hello", "hello"),
        ("LOVELY", "lovely"),
        ("here", "here"),
        ("Al9$", "al9$"),
        ("", ""),
        ("ABC123xyz", "abc123xyz"),
        ("PyThOn", "python")
    ]
    
    sol = Solution()
    
    # Test original implementation
    print("Testing original implementation:")
    start_time = time.time()
    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = sol.toLowerCase(test_input)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Input: {test_input} | Expected: {expected} | Got: {result}")
    orig_time = time.time() - start_time
    
    print("\nTesting optimized implementation:")
    start_time = time.time()
    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = sol.toUpperCase_optimized(test_input)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status} Input: {test_input} | Expected: {expected} | Got: {result}")
    opt_time = time.time() - start_time
    
    print(f"\nPerformance Comparison:")
    print(f"Original implementation: {orig_time:.6f} seconds")
    print(f"Optimized implementation: {opt_time:.6f} seconds")
    print(f"Speed improvement: {(orig_time/opt_time):.2f}x")

if __name__ == "__main__":
    test_toLowerCase()
