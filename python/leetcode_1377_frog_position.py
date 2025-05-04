"""
LeetCode 1377. Frog Position After T Seconds

Problem Statement:
Given an undirected tree with n vertices numbered from 1 to n. A frog starts at vertex 1 and wants to jump to vertex target.
At each second, the frog jumps from its current vertex to a neighboring vertex.
The frog can only jump from vertex x to vertex y if (x, y) is an edge and if the frog hasn't visited y before.
Return the probability that the frog is on vertex target after t seconds. If the frog can't reach the target, return 0.

Logic:
1. Use BFS to traverse the tree level by level
2. For each vertex, calculate probability based on number of unvisited neighbors
3. Keep track of visited nodes to avoid cycles
4. Track time and position to match target conditions
5. Handle special cases where frog reaches target early or can't reach in time

Time Complexity: O(n) where n is the number of vertices
Space Complexity: O(n) for the queue and visited set
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if n == 1:
            return 1.0
        
        # Create adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Queue stores (vertex, probability, time)
        queue = deque([(1, 1.0, 0)])
        visited = {1}
        
        while queue:
            vertex, prob, time = queue.popleft()
            
            # Get unvisited neighbors
            neighbors = [v for v in graph[vertex] if v not in visited]
            
            # If we're at target
            if vertex == target:
                # Return probability if either time exactly matches
                # or no more moves possible and time less than t
                if time == t or (not neighbors and time < t):
                    return prob
                return 0.0
            
            # If we've used all time or no neighbors, continue
            if time == t or not neighbors:
                continue
            
            # Calculate probability for each neighbor
            next_prob = prob / len(neighbors)
            for next_vertex in neighbors:
                visited.add(next_vertex)
                queue.append((next_vertex, next_prob, time + 1))
        
        return 0.0

# Test driver
def run_tests():
    solution = Solution()
    
    # Test case 1
    n1, edges1, t1, target1 = 7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4
    print(f"Test 1: n={n1}, target={target1}, t={t1}")
    print(f"Expected: 0.16666666666666666")
    print(f"Got: {solution.frogPosition(n1, edges1, t1, target1)}\n")
    
    # Test case 2
    n2, edges2, t2, target2 = 7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1, 7
    print(f"Test 2: n={n2}, target={target2}, t={t2}")
    print(f"Expected: 0.3333333333333333")
    print(f"Got: {solution.frogPosition(n2, edges2, t2, target2)}\n")
    
    # Test case 3
    n3, edges3, t3, target3 = 3, [[2,1],[3,2]], 1, 2
    print(f"Test 3: n={n3}, target={target3}, t={t3}")
    print(f"Expected: 1.0")
    print(f"Got: {solution.frogPosition(n3, edges3, t3, target3)}")

if __name__ == "__main__":
    run_tests()