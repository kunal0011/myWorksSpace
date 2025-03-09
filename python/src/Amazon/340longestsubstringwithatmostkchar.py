"""
LeetCode 340: Longest Substring with At Most K Distinct Characters

Problem Statement:
Given a string s and an integer k, return the length of the longest substring of s that contains 
at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

Logic:
1. Use sliding window technique with two pointers (left and right)
2. Maintain a hashmap to store character frequencies in current window
3. For each character (right pointer):
   - Add it to the frequency map
   - While we have more than k distinct characters:
     * Remove characters from the left
     * Update the frequency map
     * Move left pointer forward
   - Update max length if current window is longer
4. Return the maximum length found
"""

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        left = 0
        char_count = {}
        max_len = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len


def run_test_cases():
    solution = Solution()
    
    # Test case 1
    s1 = "eceba"
    k1 = 2
    result1 = solution.lengthOfLongestSubstringKDistinct(s1, k1)
    print(f"Test case 1:")
    print(f"Input: s = '{s1}', k = {k1}")
    print(f"Expected: 3")
    print(f"Got: {result1}")
    print(f"Pass? {result1 == 3}\n")
    
    # Test case 2
    s2 = "aa"
    k2 = 1
    result2 = solution.lengthOfLongestSubstringKDistinct(s2, k2)
    print(f"Test case 2:")
    print(f"Input: s = '{s2}', k = {k2}")
    print(f"Expected: 2")
    print(f"Got: {result2}")
    print(f"Pass? {result2 == 2}\n")
    
    # Test case 3 - Empty string
    s3 = ""
    k3 = 2
    result3 = solution.lengthOfLongestSubstringKDistinct(s3, k3)
    print(f"Test case 3:")
    print(f"Input: s = '{s3}', k = {k3}")
    print(f"Expected: 0")
    print(f"Got: {result3}")
    print(f"Pass? {result3 == 0}\n")
    
    # Test case 4 - k = 0
    s4 = "hello"
    k4 = 0
    result4 = solution.lengthOfLongestSubstringKDistinct(s4, k4)
    print(f"Test case 4:")
    print(f"Input: s = '{s4}', k = {k4}")
    print(f"Expected: 0")
    print(f"Got: {result4}")
    print(f"Pass? {result4 == 0}\n")
    
    # Test case 5 - Longer string with repeating characters
    s5 = "abaccc"
    k5 = 2
    result5 = solution.lengthOfLongestSubstringKDistinct(s5, k5)
    print(f"Test case 5:")
    print(f"Input: s = '{s5}', k = {k5}")
    print(f"Expected: 4")
    print(f"Got: {result5}")
    print(f"Pass? {result5 == 4}")


if __name__ == "__main__":
    run_test_cases()
