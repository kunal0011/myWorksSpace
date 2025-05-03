"""
LeetCode 323 - Number of Connected Components in an Undirected Graph

Problem Statement:
You have a graph of n nodes. You are given an integer n and an array edges where 
edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi 
in the graph.

Return the number of connected components in the graph.
"""

from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjacency list
        adj_list = {i: [] for i in range(n)}
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node):
            # Mark the node as visited
            visited.add(node)
            # Visit all neighbors
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        visited = set()
        num_components = 0

        # Perform DFS for each node
        for i in range(n):
            if i not in visited:
                dfs(i)
                num_components += 1

        return num_components


def run_tests():
    solution = Solution()

    test_cases = [
        (
            5,
            [[0, 1], [1, 2], [3, 4]],
            2,  # Two components: [0-1-2] and [3-4]
        ),
        (
            5,
            [[0, 1], [1, 2], [2, 3], [3, 4]],
            1,  # One component: [0-1-2-3-4]
        ),
        (
            3,
            [],
            3,  # Three isolated nodes
        ),
        (
            6,
            [[0, 1], [1, 2], [2, 3], [4, 5]],
            2,  # Two components: [0-1-2-3] and [4-5]
        ),
    ]

    for i, (n, edges, expected) in enumerate(test_cases, 1):
        result = solution.countComponents(n, edges)
        print(f"\nTest case {i}:")
        print(f"n: {n}")
        print(f"edges: {edges}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if result == expected else '✗ Failed'}")


if __name__ == "__main__":
    run_tests()
