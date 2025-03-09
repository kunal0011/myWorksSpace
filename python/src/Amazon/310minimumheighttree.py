"""
LeetCode 310 - Minimum Height Trees

Problem Statement:
A tree is an undirected graph in which any two vertices are connected by exactly one path.
Given a tree of n nodes labeled from 0 to n-1, and an array of n-1 edges where edges[i] = [ai, bi]
indicates that there is an undirected edge between nodes ai and bi in the tree, find all the root
nodes of minimum height trees (MHTs).

Logic:
1. Use topological sort approach from leaves inward:
   - Start with leaf nodes (nodes with degree 1)
   - Remove leaves level by level
   - Last remaining 1 or 2 nodes are roots of MHTs
2. Key steps:
   - Build adjacency list representation
   - Identify and process leaves iteratively
   - Continue until 2 or fewer nodes remain
3. Time: O(n), Space: O(n)
"""

from collections import deque, defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph (adjacency list)
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        # Collect all leaves
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])

        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_size = len(leaves)
            remaining_nodes -= leaves_size
            for _ in range(leaves_size):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)

def test_find_min_height_trees():
    solution = Solution()
    
    # Test cases
    test_cases = [
        {
            'n': 4,
            'edges': [[1,0],[1,2],[1,3]],
            'expected': [1]           # Star graph, center is root
        },
        {
            'n': 6,
            'edges': [[3,0],[3,1],[3,2],[3,4],[5,4]],
            'expected': [3,4]         # Two possible roots
        },
        {
            'n': 2,
            'edges': [[0,1]],
            'expected': [0,1]         # Both nodes can be root
        },
        {
            'n': 1,
            'edges': [],
            'expected': [0]           # Single node
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        result = solution.findMinHeightTrees(test_case['n'], test_case['edges'])
        # Sort both lists for comparison
        result.sort()
        test_case['expected'].sort()
        assert result == test_case['expected'], \
            f"Test case {i + 1} failed: expected {test_case['expected']}, got {result}"
        print(f"Test case {i + 1} passed:")
        print(f"Nodes: {test_case['n']}")
        print(f"Edges: {test_case['edges']}")
        print(f"MHT roots: {result}\n")

if __name__ == "__main__":
    test_find_min_height_trees()
    print("All test cases passed!")
