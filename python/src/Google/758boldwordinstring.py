"""
LeetCode 758: Bold Words in String

Problem Statement:
Given a string s and a list of strings words, return a bold-tagged string. Any substring of s that is equal to any word in words 
should be wrapped in "<b>" and "</b>" tags.
If two such substrings overlap, they should be wrapped together by only one pair of closed bold tag.
If two substrings are consecutive, they should be wrapped together by only one pair of closed bold tags.

Logic:
1. Create a boolean array to mark characters that should be bold
2. For each word in words:
   - Find all occurrences of the word in s using find()
   - Mark all characters of found occurrences as bold
3. Build result string:
   - Traverse the string
   - Add opening tag when entering bold region
   - Add closing tag when exiting bold region
   - Handle overlapping and consecutive bold regions

Time Complexity: O(N * M * K) where N = len(s), M = number of words, K = average word length
Space Complexity: O(N) for the boolean array
"""

from typing import List


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        bold = [False] * n

        # Step 1: Mark the bold intervals
        for word in words:
            start = s.find(word)
            while start != -1:
                for i in range(start, start + len(word)):
                    bold[i] = True
                start = s.find(word, start + 1)

        # Step 2: Construct the result string with <b> tags
        result = []
        i = 0
        while i < n:
            if bold[i]:
                result.append("<b>")
                while i < n and bold[i]:
                    result.append(s[i])
                    i += 1
                result.append("</b>")
            else:
                result.append(s[i])
                i += 1

        return "".join(result)


def test_bold_words():
    solution = Solution()

    # Test case 1: Basic case with non-overlapping words
    s1 = "abcxyz123"
    words1 = ["abc", "123"]
    result1 = solution.addBoldTag(s1, words1)
    expected1 = "<b>abc</b>xyz<b>123</b>"
    assert result1 == expected1, f"Test case 1 failed. Expected {expected1}, got {result1}"
    print(
        f"Test case 1 passed:\nInput: s = {s1}, words = {words1}\nOutput: {result1}")

    # Test case 2: Overlapping words
    s2 = "aaabbcc"
    words2 = ["aaa", "aab", "bc"]
    result2 = solution.addBoldTag(s2, words2)
    expected2 = "<b>aaabbc</b>c"
    assert result2 == expected2, f"Test case 2 failed. Expected {expected2}, got {result2}"
    print(
        f"\nTest case 2 passed:\nInput: s = {s2}, words = {words2}\nOutput: {result2}")

    # Test case 3: No matching words
    s3 = "xyz"
    words3 = ["abc"]
    result3 = solution.addBoldTag(s3, words3)
    expected3 = "xyz"
    assert result3 == expected3, f"Test case 3 failed. Expected {expected3}, got {result3}"
    print(
        f"\nTest case 3 passed:\nInput: s = {s3}, words = {words3}\nOutput: {result3}")

    # Test case 4: Empty string
    s4 = ""
    words4 = ["abc"]
    result4 = solution.addBoldTag(s4, words4)
    expected4 = ""
    assert result4 == expected4, f"Test case 4 failed. Expected {expected4}, got {result4}"
    print(
        f"\nTest case 4 passed:\nInput: s = {s4}, words = {words4}\nOutput: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_bold_words()
