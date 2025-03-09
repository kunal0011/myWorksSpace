"""
LeetCode 344: Reverse String

Problem Statement:
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Logic:
1. Use two pointers approach:
   - Initialize left pointer at start (0) and right pointer at end (len-1)
   - While left < right:
     * Swap characters at left and right pointers
     * Move left pointer right (left++)
     * Move right pointer left (right--)
2. Time Complexity: O(n) where n is length of string
3. Space Complexity: O(1) as we only use two pointers
"""

from typing import List

class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        # Use two pointers: one starting from the left, the other from the right
        while left < right:
            # Swap the characters
            s[left], s[right] = s[right], s[left]
            # Move towards the center
            left += 1
            right -= 1

def run_test_cases():
    solution = Solution()
    
    # Test case 1: Example from problem statement
    test1 = list("hello")
    print("Test case 1:")
    print(f"Input: {test1}")
    solution.reverseString(test1)
    print(f"Expected: ['o', 'l', 'l', 'e', 'h']")
    print(f"Got: {test1}")
    print(f"Pass? {test1 == list('olleh')}\n")
    
    # Test case 2: Another example from problem statement
    test2 = list("Hannah")
    print("Test case 2:")
    print(f"Input: {test2}")
    solution.reverseString(test2)
    print(f"Expected: ['h', 'a', 'n', 'n', 'a', 'H']")
    print(f"Got: {test2}")
    print(f"Pass? {test2 == list('hannaH')}\n")
    
    # Test case 3: Single character
    test3 = ['a']
    print("Test case 3:")
    print(f"Input: {test3}")
    solution.reverseString(test3)
    print(f"Expected: ['a']")
    print(f"Got: {test3}")
    print(f"Pass? {test3 == ['a']}\n")
    
    # Test case 4: Empty string
    test4 = []
    print("Test case 4:")
    print(f"Input: {test4}")
    solution.reverseString(test4)
    print(f"Expected: []")
    print(f"Got: {test4}")
    print(f"Pass? {test4 == []}\n")
    
    # Test case 5: Even length string
    test5 = list("abcd")
    print("Test case 5:")
    print(f"Input: {test5}")
    solution.reverseString(test5)
    print(f"Expected: ['d', 'c', 'b', 'a']")
    print(f"Got: {test5}")
    print(f"Pass? {test5 == list('dcba')}")


if __name__ == "__main__":
    run_test_cases()
