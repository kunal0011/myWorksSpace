"""
LeetCode 685: Redundant Connection II

In this problem, a rooted tree is a directed graph such that, there is exactly one node (the root) 
for which all other nodes are descendants of this node, plus every node has exactly one parent, 
except for the root node which has no parents.

Given the edges of a directed graph where edges[i] = [ai, bi] indicates there is an edge 
between nodes ai and bi, return an edge that can be removed so that the resulting graph is a rooted tree.
If there are multiple answers, return the answer that occurs last in the given 2D-array.

Key Points:
1. The graph might have two types of issues:
   - A node having two parents
   - A cycle in the graph
2. The answer is guaranteed to be unique in the case that the given graph is a rooted tree plus one edge.
"""
from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent_map, node):
            if parent_map[node] != node:
                parent_map[node] = find(parent_map, parent_map[node])
            return parent_map[node]

        def union(parent_map, node1, node2):
            root1 = find(parent_map, node1)
            root2 = find(parent_map, node2)
            if root1 == root2:
                return False
            parent_map[root2] = root1
            return True

        n = len(edges)
        parent = {}
        edge1 = edge2 = None

        # Find nodes with two parents
        for edge in edges:
            child = edge[1]
            if child in parent:
                edge1 = [parent[child], child]  # First edge to the child
                edge2 = edge  # Second edge to the child
                break
            parent[child] = edge[0]

        # Initialize union-find data structure
        uf = {i: i for i in range(1, n + 1)}

        # Case 1: No node has two parents
        if edge1 is None:
            for edge in edges:
                if not union(uf, edge[0], edge[1]):
                    return edge
            return []

        # Case 2: One node has two parents
        # Try removing edge2 first
        for edge in edges:
            if edge != edge2:
                if not union(uf, edge[0], edge[1]):
                    return edge1
        return edge2


def test_redundant_connection():
    test_cases = [
        (
            [[1,2], [1,3], [2,3]],
            [2,3],
            "Case 1: Simple cycle"
        ),
        (
            [[1,2], [2,3], [3,4], [4,1], [1,5]],
            [4,1],
            "Case 2: Cycle with branch"
        ),
        (
            [[2,1], [3,1], [4,2], [1,4]],
            [2,1],
            "Case 3: Multiple possible answers"
        ),
        (
            [[1,2], [2,3], [3,1], [4,1]],
            [3,1],
            "Case 4: Cycle with two parents"
        )
    ]

    solution = Solution()
    for i, (edges, expected, description) in enumerate(test_cases, 1):
        result = solution.findRedundantDirectedConnection(edges)
        assert result == expected, \
            f"Test {i} failed: Expected {expected}, got {result}"
        print(f"\nTest {i}: {description}")
        print(f"Edges: {edges}")
        print(f"Expected: {expected}")
        print(f"Result: {result}")
        print("-" * 50)


if __name__ == "__main__":
    test_redundant_connection()
