"""
LeetCode 1910. Remove All Occurrences of a Substring

Problem Statement:
Given two strings s and part, perform the following operation on s until all occurrences of the 
substring part are removed:
- Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

Time Complexity: O(n*m) where n is length of s and m is length of part
Space Complexity: O(n) for string operations
"""


class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Logic:
        # 1. Keep checking if part exists in s
        # 2. If found, remove its leftmost occurrence
        # 3. Continue until no occurrence remains
        # 4. Return final string

        while part in s:
            # Replace the first (leftmost) occurrence of 'part' with empty string
            s = s.replace(part, "", 1)
        return s


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        ("daabcbaabcbc", "abc"),           # Expected: "dab"
        ("axxxxyyyyb", "xy"),              # Expected: "ab"
        ("aabababa", "aba"),               # Expected: "ba"
        ("aaaaaa", "aa"),                  # Expected: ""
        ("abcabcdabcd", "abcd")            # Expected: "abc"
    ]

    for i, (s, part) in enumerate(test_cases):
        print(f"Test case {i + 1}:")
        print(f"Original string: {s}")
        print(f"Substring to remove: {part}")
        result = solution.removeOccurrences(s, part)
        print(f"Result after removals: {result}")

        # Show step-by-step removal process
        temp = s
        step = 1
        while part in temp:
            idx = temp.index(part)
            print(f"Step {step}: Found '{part}' at index {idx}")
            temp = temp.replace(part, "", 1)
            print(f"After removal: {temp}")
            step += 1
        print()
