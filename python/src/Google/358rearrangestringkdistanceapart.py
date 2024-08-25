import heapq
from collections import Counter, deque


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s

        # Step 1: Count frequency of each character
        char_count = Counter(s)

        # Step 2: Use a max-heap to store characters by frequency
        max_heap = [(-freq, char) for char, freq in char_count.items()]
        heapq.heapify(max_heap)

        queue = deque()  # To store characters that are waiting to be reinserted
        result = []

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            # Decrement the frequency and add to queue with current index
            queue.append((freq+1, char))

            # If the queue length has reached k, reinsert the character at the front
            if len(queue) >= k:
                to_reinsert = queue.popleft()
                if to_reinsert[0] < 0:
                    heapq.heappush(max_heap, to_reinsert)

        # If the result length equals the original string length, return result as string
        if len(result) == len(s):
            return ''.join(result)
        else:
            return ""


# Example usage:
solution = Solution()
s = "aaadbbcc"
k = 3
print(solution.rearrangeString(s, k))  # Output: "abacabcd"
