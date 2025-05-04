"""
LeetCode 792: Number of Matching Subsequences

Problem Statement:
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order
of the remaining characters.

Logic:
1. Use a dictionary of deques to group words by their first character
2. For each character in s:
   - Process all words waiting for that character
   - For each such word:
     * If it's the last character, increment count
     * Otherwise, move remaining substring to bucket of its new first character
3. This approach avoids checking each word character by character against s
4. Instead, words "follow along" as we iterate through s

Time Complexity: O(N + sum(len(word_i))) where N is length of s
Space Complexity: O(k) where k is total length of all words
"""

from collections import defaultdict, deque
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Create a dictionary to hold the words in the form of a deque
        waiting = defaultdict(deque)

        # Populate the dictionary with words, grouped by their first character
        for word in words:
            waiting[word[0]].append(word)

        # Result variable to count subsequences
        count = 0

        # Iterate over each character in the string s
        for char in s:
            # Get the deque of words that are waiting for this character
            current_words = waiting[char]
            # Reset the entry in the dictionary
            waiting[char] = deque()

            # Process each word
            while current_words:
                word = current_words.popleft()
                # Move to the next character in the word
                if len(word) == 1:
                    # If this is the last character, it means the whole word is a subsequence
                    count += 1
                else:
                    # Otherwise, move the remaining part of the word to the next bucket
                    waiting[word[1]].append(word[1:])

        return count

def test_matching_subsequences():
    solution = Solution()
    
    # Test case 1: Basic case
    s1 = "abcde"
    words1 = ["a", "bb", "acd", "ace"]
    result1 = solution.numMatchingSubseq(s1, words1)
    assert result1 == 3, f"Test case 1 failed. Expected 3, got {result1}"
    print(f"Test case 1 passed: s={s1}, words={words1}, result={result1}")
    
    # Test case 2: Repeated characters
    s2 = "dsahjpjauf"
    words2 = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
    result2 = solution.numMatchingSubseq(s2, words2)
    assert result2 == 2, f"Test case 2 failed. Expected 2, got {result2}"
    print(f"\nTest case 2 passed: s={s2}, words={words2}, result={result2}")
    
    # Test case 3: Empty words array
    s3 = "abc"
    words3 = []
    result3 = solution.numMatchingSubseq(s3, words3)
    assert result3 == 0, f"Test case 3 failed. Expected 0, got {result3}"
    print(f"\nTest case 3 passed: s={s3}, words={words3}, result={result3}")
    
    # Test case 4: No matching subsequences
    s4 = "abc"
    words4 = ["def", "ghi"]
    result4 = solution.numMatchingSubseq(s4, words4)
    assert result4 == 0, f"Test case 4 failed. Expected 0, got {result4}"
    print(f"\nTest case 4 passed: s={s4}, words={words4}, result={result4}")
    
    print("\nAll test cases passed!")

if __name__ == "__main__":
    test_matching_subsequences()
