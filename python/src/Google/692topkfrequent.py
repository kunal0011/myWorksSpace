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
