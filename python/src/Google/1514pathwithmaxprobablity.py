import heapq
from collections import defaultdict


class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        # Build graph as an adjacency list
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        # Use a max-heap (priority queue) to keep track of the highest probability
        max_heap = [(-1.0, start)]  # (probability, node)
        probabilities = [0.0] * n
        probabilities[start] = 1.0

        while max_heap:
            current_prob, node = heapq.heappop(max_heap)
            current_prob = -current_prob

            # Early exit if we reached the end node
            if node == end:
                return current_prob

            for neighbor, prob in graph[node]:
                new_prob = current_prob * prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))

        return 0.0
