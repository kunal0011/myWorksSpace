"""
LeetCode 392: Is Subsequence

Problem Statement:
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence is a string that can be derived from another string by deleting some or no elements 
without changing the order of the remaining elements.

Time Complexity: O(n) where n is length of string t
Space Complexity: O(1)
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Handle empty string case
        if not s:
            return True
        if not t:
            return False

        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

def test_is_subsequence():
    """
    Test function to verify the solution with various test cases
    """
    solution = Solution()
    
    test_cases = [
        {
            "s": "abc",
            "t": "ahbgdc",
            "expected": True,
            "description": "Basic case with subsequence"
        },
        {
            "s": "axc",
            "t": "ahbgdc",
            "expected": False,
            "description": "Basic case without subsequence"
        },
        {
            "s": "",
            "t": "ahbgdc",
            "expected": True,
            "description": "Empty source string"
        },
        {
            "s": "abc",
            "t": "",
            "expected": False,
            "description": "Empty target string"
        },
        {
            "s": "acb",
            "t": "ahbgdc",
            "expected": False,
            "description": "Wrong order"
        },
        {
            "s": "abc",
            "t": "abc",
            "expected": True,
            "description": "Exact match"
        }
    ]

    for i, test_case in enumerate(test_cases, 1):
        s = test_case["s"]
        t = test_case["t"]
        expected = test_case["expected"]
        description = test_case["description"]

        print(f"\nTest case {i}: {description}")
        print(f"s = '{s}'")
        print(f"t = '{t}'")

        result = solution.isSubsequence(s, t)
        assert result == expected, f"Expected {expected}, got {result}"
        print("✓ Test case passed!")

if __name__ == "__main__":
    test_is_subsequence()
    print("\nAll test cases passed! 🎉")
