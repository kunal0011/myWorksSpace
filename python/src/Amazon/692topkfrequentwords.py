"""
LeetCode 692: Top K Frequent Words

Given an array of strings words and an integer k, return the k most frequent strings.
Return the answer sorted by the frequency from highest to lowest. Sort the words with 
the same frequency by their lexicographical order.

Example:
Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
"""

from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Count word frequencies
        word_count = Counter(words)
        
        # Create heap entries with (-freq, word) format
        # Using negative frequency for max heap behavior
        heap = [(-freq, word) for word, freq in word_count.items()]
        heapq.heapify(heap)
        
        # Get top k elements
        return [heapq.heappop(heap)[1] for _ in range(k)]

def test_top_k_frequent():
    test_cases = [
        {
            'words': ["i","love","leetcode","i","love","coding"],
            'k': 2,
            'expected': ["i","love"]
        },
        {
            'words': ["the","day","is","sunny","the","the","the","sunny","is","is"],
            'k': 4,
            'expected': ["the","is","sunny","day"]
        }
    ]
    
    solution = Solution()
    for i, test in enumerate(test_cases, 1):
        result = solution.topKFrequent(test['words'], test['k'])
        print(f"Test case {i}:")
        print(f"Input: words = {test['words']}, k = {test['k']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == test['expected'] else '✗ Failed'}\n")

if __name__ == "__main__":
    test_top_k_frequent()
