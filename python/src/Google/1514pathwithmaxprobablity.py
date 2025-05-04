"""
LeetCode 1514. Path with Maximum Probability

Problem Statement:
You are given an undirected weighted graph of n nodes (0-indexed), represented by edges where 
edges[i] = [a, b] is an undirected edge connecting the nodes a and b with probability succProb[i].
Given two nodes start and end, find the path with the maximum probability of success to go from 
start to end and return its success probability.
If there is no path from start to end, return 0. Your answer will be accepted if it differs 
from the correct answer by at most 1e-5.

Time Complexity: O(E * log(V)) where E is number of edges and V is number of vertices
Space Complexity: O(V + E) for graph and heap storage
"""

import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float],
                       start: int, end: int) -> float:
        # Logic:
        # 1. Build undirected graph using adjacency list with probabilities
        # 2. Use Dijkstra's algorithm with max heap (instead of min heap for shortest path)
        # 3. Keep track of maximum probabilities to reach each node
        # 4. Use negative probabilities with heap to simulate max heap
        # 5. Return probability of reaching end node, or 0 if unreachable

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


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        # n, edges, succProb, start, end
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2),  # Expected: 0.25
        (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2),  # Expected: 0.3
        (3, [[0, 1]], [0.5], 0, 2),                       # Expected: 0.0
        (5, [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
            [0.37, 0.17, 0.93, 0.23, 0.39, 0.04], 3, 4),      # Expected: 0.2139
    ]

    for i, (n, edges, succProb, start, end) in enumerate(test_cases):
        result = solution.maxProbability(n, edges, succProb, start, end)
        print(f"Test case {i + 1}:")
        print(f"Number of nodes: {n}")
        print(f"Edges: {edges}")
        print(f"Success Probabilities: {succProb}")
        print(f"Start node: {start}, End node: {end}")
        print(f"Maximum probability: {result:.4f}")
        print()
