"""
LeetCode 692: Top K Frequent Words
Problem Statement:
Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Logic:
1. Use Counter to count frequency of each word - O(n)
2. Use max heap (implemented using min heap with negative frequencies) to maintain top k words
3. For same frequency, lexicographical ordering is handled by Python's string comparison
4. Extract top k elements from heap

Time Complexity: O(n log k) where n is number of words
Space Complexity: O(n) for counter + heap
"""

import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count the frequency of each word
        count = Counter(words)

        # Step 2: Use a min-heap to store the top k frequent elements
        heap = []
        for word, freq in count.items():
            # Use negative frequency for max-heap behavior
            heapq.heappush(heap, (-freq, word))

        # Step 3: Extract the k most frequent words
        result = [heapq.heappop(heap)[1] for _ in range(k)]

        return result


def test_top_k_frequent():
    solution = Solution()

    # Test Case 1: Basic case
    words1 = ["i", "love", "leetcode", "i", "love", "coding"]
    k1 = 2
    result1 = solution.topKFrequent(words1, k1)
    assert result1 == [
        "i", "love"], f"Expected ['i','love'], but got {result1}"
    print("Test case 1: Basic frequency sorting ✓")

    # Test Case 2: Lexicographical ordering for same frequency
    words2 = ["the", "day", "is", "sunny",
              "the", "the", "the", "sunny", "is", "is"]
    k2 = 4
    result2 = solution.topKFrequent(words2, k2)
    assert result2 == ["the", "is", "sunny",
                       "day"], f"Expected ['the','is','sunny','day'], but got {result2}"
    print("Test case 2: Lexicographical ordering ✓")

    # Test Case 3: Single word
    words3 = ["hello"]
    k3 = 1
    result3 = solution.topKFrequent(words3, k3)
    assert result3 == ["hello"], f"Expected ['hello'], but got {result3}"
    print("Test case 3: Single word ✓")

    # Test Case 4: All unique words
    words4 = ["a", "b", "c"]
    k4 = 3
    result4 = solution.topKFrequent(words4, k4)
    assert sorted(result4) == [
        "a", "b", "c"], f"Expected ['a','b','c'], but got {result4}"
    print("Test case 4: All unique words ✓")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_top_k_frequent()
