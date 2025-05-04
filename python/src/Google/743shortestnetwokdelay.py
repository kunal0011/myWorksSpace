"""
LeetCode 743: Network Delay Time

Problem Statement:
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges 
times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal 
to travel from source to target. We will send a signal from a given node k. Return the minimum time it takes for all 
n nodes to receive the signal. If it is impossible for all n nodes to receive the signal, return -1.

Logic:
1. Use Dijkstra's algorithm to find shortest paths from source node k
2. Build adjacency list representation of graph using defaultdict
3. Use priority queue (min-heap) to process nodes in order of increasing time
4. For each node:
   - Get minimum time node from priority queue
   - If node already processed, skip
   - Update shortest time for current node
   - Add unprocessed neighbors to priority queue
5. Return max time if all nodes reached, else -1

Time Complexity: O(E * log V) where E is number of edges and V is number of vertices
Space Complexity: O(V + E) for adjacency list and priority queue
"""

import heapq
from collections import defaultdict, deque
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the graph as an adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Step 2: Use a priority queue to perform Dijkstra's algorithm
        pq = [(0, k)]  # (time, node)
        shortest_time = {}  # To track the shortest time to reach each node

        while pq:
            time, node = heapq.heappop(pq)

            if node in shortest_time:
                continue  # Skip if we've already found the shortest time for this node

            shortest_time[node] = time

            for neighbor, weight in graph[node]:
                if neighbor not in shortest_time:
                    heapq.heappush(pq, (time + weight, neighbor))

        # Step 3: Check if we have reached all nodes
        if len(shortest_time) == n:
            return max(shortest_time.values())
        else:
            return -1


def test_network_delay():
    solution = Solution()

    # Test case 1: Basic case
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n1, k1 = 4, 2
    result1 = solution.networkDelayTime(times1, n1, k1)
    assert result1 == 2, f"Test case 1 failed. Expected 2, got {result1}"
    print(
        f"Test case 1 passed: times={times1}, n={n1}, k={k1}, result={result1}")

    # Test case 2: Impossible to reach all nodes
    times2 = [[1, 2, 1]]
    n2, k2 = 2, 2
    result2 = solution.networkDelayTime(times2, n2, k2)
    assert result2 == -1, f"Test case 2 failed. Expected -1, got {result2}"
    print(
        f"Test case 2 passed: times={times2}, n={n2}, k={k2}, result={result2}")

    # Test case 3: Single node
    times3 = []
    n3, k3 = 1, 1
    result3 = solution.networkDelayTime(times3, n3, k3)
    assert result3 == 0, f"Test case 3 failed. Expected 0, got {result3}"
    print(
        f"Test case 3 passed: times={times3}, n={n3}, k={k3}, result={result3}")

    # Test case 4: Multiple paths to same node
    times4 = [[1, 2, 1], [2, 3, 2], [1, 3, 4]]
    n4, k4 = 3, 1
    result4 = solution.networkDelayTime(times4, n4, k4)
    assert result4 == 3, f"Test case 4 failed. Expected 3, got {result4}"
    print(
        f"Test case 4 passed: times={times4}, n={n4}, k={k4}, result={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_network_delay()
