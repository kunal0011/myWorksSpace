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
