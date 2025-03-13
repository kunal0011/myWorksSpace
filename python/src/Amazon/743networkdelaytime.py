"""
LeetCode 743: Network Delay Time

You are given a network of n nodes, labeled from 1 to n. You are also given times, 
a list of travel times as directed edges times[i] = (ui, vi, wi), where:
- ui is the source node
- vi is the target node
- wi is the time it takes for a signal to travel from source to target

We will send a signal from a given node k. Return the minimum time it takes for all 
n nodes to receive the signal. If it's impossible for all n nodes to receive the signal, return -1.
"""

import heapq
from collections import defaultdict, deque
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Create adjacency list with weights
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))
        
        # Initialize distances
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        
        # Priority queue for Dijkstra's algorithm
        # Format: (current_distance, node)
        pq = [(0, k)]
        visited = set()
        
        while pq:
            curr_dist, curr = heapq.heappop(pq)
            
            if curr in visited:
                continue
                
            visited.add(curr)
            
            # If we've visited all nodes, we can stop
            if len(visited) == n:
                break
            
            # Check all neighbors
            for neighbor, time in graph[curr]:
                distance = curr_dist + time
                
                # Only update if we found a shorter path
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        # Check if all nodes are reachable
        max_time = max(distances.values())
        return max_time if max_time != float('inf') else -1
    
    def networkDelayTime_bfs(self, times: List[List[int]], n: int, k: int) -> int:
        """Alternative BFS solution for comparison"""
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))
            
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        
        queue = deque([(k, 0)])  # (node, time)
        
        while queue:
            curr, curr_time = queue.popleft()
            
            for neighbor, time in graph[curr]:
                new_time = curr_time + time
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    queue.append((neighbor, new_time))
                    
        max_time = max(distances.values())
        return max_time if max_time != float('inf') else -1


def test_network_delay():
    """Test function for Network Delay Time solutions"""
    test_cases = [
        # times, n, k, expected
        ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
        ([[1,2,1]], 2, 1, 1),
        ([[1,2,1]], 2, 2, -1),
        ([[1,2,1],[2,3,2],[1,3,4]], 3, 1, 3),
        ([[1,2,1],[2,1,3]], 2, 2, 3),
        ([], 1, 1, 0),
        ([[1,2,1],[2,3,7],[1,3,4],[2,1,2]], 4, 1, -1)
    ]
    
    solution = Solution()
    
    for i, (times, n, k, expected) in enumerate(test_cases, 1):
        # Test Dijkstra's solution
        result1 = solution.networkDelayTime(times, n, k)
        # Test BFS solution
        result2 = solution.networkDelayTime_bfs(times, n, k)
        
        print(f"\nTest case {i}:")
        print(f"Input: times={times}, n={n}, k={k}")
        print(f"Expected: {expected}")
        print(f"Dijkstra's: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"BFS: {result2} {'✓' if result2 == expected else '✗'}")


if __name__ == "__main__":
    test_network_delay()
