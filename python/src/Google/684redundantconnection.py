"""
LeetCode 684: Redundant Connection

Problem Statement:
In an undirected graph with n vertices, where each edge is represented by a pair [u, v], 
find an edge that can be removed so that the graph becomes a tree.
Return the edge that appears last in the input if there are multiple answers.

Example:
Input: edges = [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: Either [1,2] or [2,3] can be removed, but [2,3] is the last edge in input.

Logic:
1. Use Union-Find (Disjoint Set) data structure
2. For each edge, check if vertices are already connected
3. If vertices are connected, this edge is redundant
4. Use path compression and union by rank for optimization

Time Complexity: O(N * α(N)) where α is the inverse Ackermann function
Space Complexity: O(N)
"""

from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        for edge in edges:
            u, v = edge
            if find(u) == find(v):
                return edge  # This is the redundant edge
            union(u, v)

        return []


def test_redundant_connection():
    solution = Solution()

    # Test case 1: Simple cycle
    print("Test Case 1:")
    edges = [[1, 2], [1, 3], [2, 3]]
    print(f"Input: {edges}")
    # Expected: [2,3]
    print(f"Output: {solution.findRedundantConnection(edges)}")

    # Test case 2: Complex cycle
    print("\nTest Case 2:")
    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    print(f"Input: {edges}")
    # Expected: [1,4]
    print(f"Output: {solution.findRedundantConnection(edges)}")

    # Test case 3: Multiple possible answers
    print("\nTest Case 3:")
    edges = [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6], [4, 6]]
    print(f"Input: {edges}")
    # Expected: [4,6]
    print(f"Output: {solution.findRedundantConnection(edges)}")


if __name__ == "__main__":
    test_redundant_connection()
