"""
LeetCode 316 - Remove Duplicate Letters

Problem Statement:
Given a string s, remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Logic:
1. Use stack to build result and track used characters
2. For each character:
   - While stack not empty and:
     - Current char is smaller than stack top
     - Stack top appears later in string
     -> Pop from stack
   - If character not used, push to stack
3. Time: O(n), Space: O(1) since only lowercase letters
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # Count frequency of each character
        last_occurrence = {c: i for i, c in enumerate(s)}
        used = set()
        stack = []
        
        for i, c in enumerate(s):
            if c not in used:
                # Pop characters that are greater and appear later
                while stack and c < stack[-1] and i < last_occurrence[stack[-1]]:
                    used.remove(stack.pop())
                stack.append(c)
                used.add(c)
        
        return ''.join(stack)


def test_remove_duplicate_letters():
    solution = Solution()
    
    # Test cases
    test_cases = [
        ("bcabc", "abc"),       # Standard case
        ("cbacdcbc", "acdb"),   # Complex case with multiple duplicates
        ("abc", "abc"),         # No duplicates
        ("aaa", "a"),           # All same characters
        ("", ""),               # Empty string
        ("zyxwvutsrqponmlkjihgfedcba", "zyxwvutsrqponmlkjihgfedcba"),  # Already in reverse order
        ("bbcaac", "bac")       # Multiple duplicates with ordering
    ]
    
    for i, (s, expected) in enumerate(test_cases):
        result = solution.removeDuplicateLetters(s)
        assert result == expected, \
            f"Test case {i + 1} failed: input='{s}', expected='{expected}', got='{result}'"
        print(f"Test case {i + 1} passed:")
        print(f"Input: '{s}'")
        print(f"Output: '{result}'")
        print(f"Expected: '{expected}'\n")

if __name__ == "__main__":
    test_remove_duplicate_letters()
    print("All test cases passed!")
