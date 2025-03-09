"""
LeetCode 242 - Valid Anagram

Problem Statement:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Solution Logic:
1. Use Counter to get character frequency maps
2. Compare the frequency maps
3. Alternative approaches:
   - Sort both strings and compare
   - Manual character count using dictionary
4. Time: O(n), Space: O(1) since alphabet is fixed size
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


def test_anagram():
    solution = Solution()
    
    # Test Case 1: Valid anagram
    s1, t1 = "anagram", "nagaram"
    print("Test 1: Valid anagram")
    print(f"s = {s1}, t = {t1}")
    print(f"Is anagram: {solution.isAnagram(s1, t1)}")  # Expected: True
    
    # Test Case 2: Not anagram (different lengths)
    s2, t2 = "rat", "car"
    print("\nTest 2: Different lengths")
    print(f"s = {s2}, t = {t2}")
    print(f"Is anagram: {solution.isAnagram(s2, t2)}")  # Expected: False
    
    # Test Case 3: Empty strings
    s3, t3 = "", ""
    print("\nTest 3: Empty strings")
    print(f"s = {s3}, t = {t3}")
    print(f"Is anagram: {solution.isAnagram(s3, t3)}")  # Expected: True
    
    # Test Case 4: Same characters, different frequencies
    s4, t4 = "aacc", "ccac"
    print("\nTest 4: Different frequencies")
    print(f"s = {s4}, t = {t4}")
    print(f"Is anagram: {solution.isAnagram(s4, t4)}")  # Expected: False

if __name__ == "__main__":
    test_anagram()
