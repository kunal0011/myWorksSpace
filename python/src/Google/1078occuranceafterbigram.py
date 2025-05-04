"""
LeetCode 1078: Occurrences After Bigram

Problem Statement:
Given two strings first and second, consider occurrences in some text of the form "first second third",
where second comes immediately after first, and third comes immediately after second.
Return an array of all the words third for each occurrence of "first second third".

Logic:
1. Split text into array of words
2. Iterate through words with window of size 3:
   - Check if current word is first
   - Check if next word is second
   - If both true, append third word to result
3. Return array of third words found

Time Complexity: O(n) where n is number of words in text
Space Complexity: O(m) where m is number of matching occurrences
"""

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split()
        result = []

        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])

        return result


def test_find_occurrences():
    solution = Solution()

    # Test case 1: Basic case
    text1 = "alice is a good girl she is a good student"
    first1 = "a"
    second1 = "good"
    result1 = solution.findOcurrences(text1, first1, second1)
    assert result1 == [
        "girl", "student"], f"Test case 1 failed. Expected ['girl', 'student'], got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: No occurrences
    text2 = "we will we will rock you"
    first2 = "alice"
    second2 = "bob"
    result2 = solution.findOcurrences(text2, first2, second2)
    assert result2 == [], f"Test case 2 failed. Expected [], got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Multiple same occurrences
    text3 = "we we we we"
    first3 = "we"
    second3 = "we"
    result3 = solution.findOcurrences(text3, first3, second3)
    assert result3 == [
        "we", "we"], f"Test case 3 failed. Expected ['we', 'we'], got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Single occurrence
    text4 = "alice is running"
    first4 = "alice"
    second4 = "is"
    result4 = solution.findOcurrences(text4, first4, second4)
    assert result4 == [
        "running"], f"Test case 4 failed. Expected ['running'], got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_find_occurrences()
