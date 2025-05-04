"""
LeetCode 1160: Find Words That Can Be Formed by Characters

Problem Statement:
You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once).
Return the sum of lengths of all good strings in words.

Logic:
1. Use Counter to count frequency of characters in chars string
2. For each word in words:
   - Count frequency of characters in current word
   - Check if we can form word using chars (all counts should be <= chars counts)
   - If word can be formed, add its length to total
3. Return total length of good words

Time Complexity: O(n * k) where n is total chars in words, k is length of chars
Space Complexity: O(1) since we only store 26 lowercase letters at most
"""

from collections import Counter


class Solution:
    def countCharacters(self, words, chars):
        # Step 1: Count the occurrences of each character in chars
        chars_count = Counter(chars)
        total_length = 0

        # Step 2: Check each word in words
        for word in words:
            word_count = Counter(word)
            can_form = True

            # Step 3: Compare character counts
            for ch in word_count:
                if word_count[ch] > chars_count.get(ch, 0):
                    can_form = False
                    break

            # Step 4: If the word can be formed, add its length to the total
            if can_form:
                total_length += len(word)

        return total_length


def test_count_characters():
    solution = Solution()

    # Test case 1: Basic case
    words1 = ["cat", "bt", "hat", "tree"]
    chars1 = "atach"
    result1 = solution.countCharacters(words1, chars1)
    assert result1 == 6, f"Test case 1 failed. Expected 6, got {result1}"
    print(f"Test case 1 passed: total length = {result1}")

    # Test case 2: No possible words
    words2 = ["hello", "world", "leetcode"]
    chars2 = "welldonehoneyr"
    result2 = solution.countCharacters(words2, chars2)
    assert result2 == 10, f"Test case 2 failed. Expected 10, got {result2}"
    print(f"\nTest case 2 passed: total length = {result2}")

    # Test case 3: Single character words
    words3 = ["a", "b", "c"]
    chars3 = "abc"
    result3 = solution.countCharacters(words3, chars3)
    assert result3 == 3, f"Test case 3 failed. Expected 3, got {result3}"
    print(f"\nTest case 3 passed: total length = {result3}")

    # Test case 4: Empty words array
    words4 = []
    chars4 = "abc"
    result4 = solution.countCharacters(words4, chars4)
    assert result4 == 0, f"Test case 4 failed. Expected 0, got {result4}"
    print(f"\nTest case 4 passed: total length = {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_count_characters()
