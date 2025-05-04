"""
LeetCode 1557. Minimum Number of Vertices to Reach All Nodes

Problem Statement:
Given a directed acyclic graph (DAG) with n nodes labeled from 0 to n-1. Each node has at most one 
outgoing edge. Find the smallest set of vertices from which all nodes in the graph are reachable.
It's guaranteed that a unique solution exists.

Time Complexity: O(V + E) where V is number of vertices and E is number of edges
Space Complexity: O(V) for storing in-degrees
"""

from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Logic:
        # 1. In a DAG, nodes with no incoming edges must be included in the result
        #    because they can't be reached from any other node
        # 2. Any node with incoming edges can be reached from other nodes
        # 3. Therefore, the minimum set is all nodes with in-degree = 0

        # Initialize an in-degree list
        in_degree = [0] * n

        # Update in-degrees based on edges
        for u, v in edges:
            in_degree[v] += 1

        # Collect vertices with zero in-degrees
        result = [i for i in range(n) if in_degree[i] == 0]

        return result


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        (6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]),          # Expected: [0,3]
        # Expected: [0,2,3]
        (5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]),
        (3, [[1, 2], [2, 0], [0, 1]]),                       # Expected: [1]
        (4, [[0, 1], [1, 2], [2, 3], [3, 0]]),                # Expected: []
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]])                 # Expected: [0]
    ]

    for i, (n, edges) in enumerate(test_cases):
        result = solution.findSmallestSetOfVertices(n, edges)
        print(f"Test case {i + 1}:")
        print(f"Number of nodes: {n}")
        print(f"Edges: {edges}")
        print(f"Minimum set of vertices: {result}")
        print(f"Explanation: From these vertices, all other nodes can be reached")
        print()
