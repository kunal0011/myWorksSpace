"""
LeetCode 1170: Compare Strings by Frequency of the Smallest Character

Problem Statement:
Let f(s) be the frequency of the lexicographically smallest character in a non-empty string s.
For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c',
which has a frequency of 2.
You are given an array queries of strings, and an array words of strings.
For each query queries[i], count the number of words in words where f(word) > f(queries[i]).
Return an integer array answer, where each answer[i] is the answer to the ith query.

Logic:
1. Create helper function f(s) to find frequency of smallest character
2. Sort word frequencies for efficient comparison using binary search
3. For each query:
   - Calculate f(query)
   - Use binary search to find count of words with greater frequency
4. Return array of counts

Time Complexity: O(N * M * log M) where N = length of queries, M = length of words
Space Complexity: O(M) for storing word frequencies
"""

from bisect import bisect_right


class Solution:
    def numSmallerByFrequency(self, queries, words):
        def f(s):
            return s.count(min(s))

        # Step 1: Calculate the frequency of the smallest character for each word in words
        word_frequencies = sorted(f(word) for word in words)

        # Step 2: Calculate the result for each query
        result = []
        for query in queries:
            query_freq = f(query)
            # Use bisect_right to find the position where query_freq would fit in word_frequencies
            # Count how many words have a greater frequency
            result.append(len(word_frequencies) -
                          bisect_right(word_frequencies, query_freq))

        return result


def test_num_smaller_by_frequency():
    solution = Solution()

    # Test case 1: Basic case
    queries1 = ["cbd"]
    words1 = ["zaaaz"]
    result1 = solution.numSmallerByFrequency(queries1, words1)
    assert result1 == [1], f"Test case 1 failed. Expected [1], got {result1}"
    print(f"Test case 1 passed: {result1}")

    # Test case 2: Multiple queries
    queries2 = ["bbb", "cc"]
    words2 = ["a", "aa", "aaa", "aaaa"]
    result2 = solution.numSmallerByFrequency(queries2, words2)
    assert result2 == [
        1, 2], f"Test case 2 failed. Expected [1,2], got {result2}"
    print(f"\nTest case 2 passed: {result2}")

    # Test case 3: Equal frequencies
    queries3 = ["a", "aa"]
    words3 = ["a", "a", "aa"]
    result3 = solution.numSmallerByFrequency(queries3, words3)
    assert result3 == [
        0, 0], f"Test case 3 failed. Expected [0,0], got {result3}"
    print(f"\nTest case 3 passed: {result3}")

    # Test case 4: Empty queries
    queries4 = []
    words4 = ["abc", "def"]
    result4 = solution.numSmallerByFrequency(queries4, words4)
    assert result4 == [], f"Test case 4 failed. Expected [], got {result4}"
    print(f"\nTest case 4 passed: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_num_smaller_by_frequency()
