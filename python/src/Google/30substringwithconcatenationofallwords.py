"""
LeetCode 30 - Substring with Concatenation of All Words

Problem:
You are given a string s and an array of strings words (all of the same length).
Return all starting indices of substring(s) in s that is a concatenation of each 
word in words exactly once, in any order.

Key Points:
- All words in 'words' have the same length
- Words can be used in any order
- Each word must be used exactly once
- The substring must contain all words concatenated together

Example:
    Input: s = "barfoothefoobarman", words = ["foo","bar"]
    Output: [0,9]
    Explanation: Substrings at index 0 and 9:
    "barfoo" is concatenation of "bar" and "foo"
    "foobar" is concatenation of "foo" and "bar"

Time Complexity: O(N * K) where:
- N is the length of string s
- K is the length of each word
Space Complexity: O(M) where M is the total length of all words
"""

from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        """
        Finds all starting indices where all words from the list appear exactly once.
        Uses sliding window approach with Counter for optimization.
        
        Algorithm:
        1. For each possible starting position (0 to word_length):
           - Use sliding window to check concatenations
           - Maintain word frequency count in current window
           - Move window when word count exceeds target
        
        Optimization:
        - Uses Counter to track word frequencies
        - Skips invalid windows when unknown word is found
        - Resets window when word count exceeds target
        
        Time: O(N * K) - N is string length, K is word length
        Space: O(M) - M is total length of all words
        """
        if not s or not words:
            return []

        word_length = len(words[0])
        num_words = len(words)
        substring_length = word_length * num_words

        # Create a frequency counter for the words
        word_count = Counter(words)
        result = []

        # Iterate over every possible starting position
        for i in range(word_length):
            left = i
            right = i
            current_count = Counter()

            while right + word_length <= len(s):
                # Extract the current word from the string
                word = s[right:right + word_length]

                # Move the right pointer to the next word
                right += word_length

                if word in word_count:
                    current_count[word] += 1

                    # If the count exceeds the expected count, move the left pointer
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_length]
                        current_count[left_word] -= 1
                        left += word_length

                    # Check if the current window matches the word count
                    if right - left == substring_length:
                        result.append(left)
                else:
                    # If the word is not in the list, reset the window
                    current_count.clear()
                    left = right

        return result


def test_findSubstring():
    solution = Solution()
    
    # Test Case 1: Basic test with two words
    s1 = "barfoothefoobarman"
    words1 = ["foo", "bar"]
    assert solution.findSubstring(s1, words1) == [0, 9]
    
    # Test Case 2: Multiple occurrences
    s2 = "wordgoodgoodgoodbestword"
    words2 = ["word","good","best","word"]
    assert solution.findSubstring(s2, words2) == []
    
    # Test Case 3: Overlapping matches
    s3 = "abaababbaba"
    words3 = ["ab","ba","ba"]
    assert sorted(solution.findSubstring(s3, words3)) == [1, 3]
    
    # Test Case 4: Empty inputs
    assert solution.findSubstring("", []) == []
    assert solution.findSubstring("abc", []) == []
    
    # Test Case 5: Single word
    s5 = "aaa"
    words5 = ["a"]
    assert solution.findSubstring(s5, words5) == [0, 1, 2]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_findSubstring()
