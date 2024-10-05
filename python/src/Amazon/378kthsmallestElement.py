import heapq


class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        # Initialize a min-heap
        n = len(matrix)
        min_heap = []

        # Add the first element of each row to the heap
        for i in range(min(n, k)):  # We only need to consider up to k rows
            heapq.heappush(min_heap, (matrix[i][0], i, 0))  # (value, row, col)

        # Extract the smallest element from the heap k times
        count = 0
        while min_heap:
            val, r, c = heapq.heappop(min_heap)
            count += 1
            if count == k:
                return val
            # If there's more elements in the row, add the next one to the heap
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
