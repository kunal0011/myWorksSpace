"""
LeetCode 459: Repeated Substring Pattern

Problem Statement:
Given a string s, check if it can be constructed by taking a substring of it and 
appending multiple copies of the substring together.

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters
"""


def repeatedSubstringPattern(s: str) -> bool:
    if not s:
        return False

    n = len(s)
    # Concatenate string with itself and remove first and last characters
    doubled = s + s
    # Check if s is present in the middle of doubled[1:-1]
    return s in doubled[1:-1]


def repeatedSubstringPattern_alternate(s: str) -> bool:
    """
    Alternative implementation using the direct approach of checking all possible
    substring lengths. This is included to help understand the logic.
    """
    n = len(s)
    for i in range(1, n//2 + 1):
        if n % i == 0:  # Length must be divisible by pattern length
            pattern = s[:i]
            if pattern * (n//i) == s:
                return True
    return False

# Test driver


def run_tests():
    test_cases = [
        {
            "s": "abab",
            "expected": True,
            "explanation": "It's the concatenation of 'ab' with itself"
        },
        {
            "s": "aba",
            "expected": False,
            "explanation": "Cannot be constructed by repeating a substring"
        },
        {
            "s": "abcabcabc",
            "expected": True,
            "explanation": "It's the concatenation of 'abc' three times"
        },
        {
            "s": "aaaa",
            "expected": True,
            "explanation": "It's the concatenation of 'a' four times"
        },
        {
            "s": "abaababaab",
            "expected": True,
            "explanation": "It's the concatenation of 'abaab' two times"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        # Test main solution
        result = repeatedSubstringPattern(test["s"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"String: {test['s']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}")

        # Verify both implementations give same result
        alt_result = repeatedSubstringPattern_alternate(test["s"])
        if alt_result != result:
            print("Warning: Alternative implementation gave different result!")
        print()


if __name__ == "__main__":
    print("Running test cases for Repeated Substring Pattern problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Optimal Solution (Using String Concatenation):
   - Key insight: If s can be built from repeated pattern p,
     then s will be found in (s + s)[1:-1]
   - This works because:
     * Concatenating s with itself gives us all possible rotations
     * Removing first and last characters ensures we don't match the whole string
   - Time Complexity: O(n)
   - Space Complexity: O(n)

2. Alternative Solution (Direct Pattern Checking):
   - Try all possible substring lengths that divide string length
   - For each length, check if that substring repeated creates the string
   - Time Complexity: O(n^2)
   - Space Complexity: O(n)

3. Why the Optimal Solution Works:
   - If s = "abab", then s + s = "abababab"
   - Removing first and last chars: "bababa"
   - Original s = "abab" is found in this substring
   - This property only holds for strings with repeated patterns
"""
