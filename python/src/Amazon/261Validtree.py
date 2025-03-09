from typing import List

"""
LeetCode 261 - Graph Valid Tree

Problem Statement:
You have a graph of n nodes labeled from 0 to n-1. You are given an array of edges where 
edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi.
Return true if the edges make up a valid tree, and false otherwise.

Solution Logic:
1. For a valid tree:
   - Must have exactly n-1 edges
   - Must be fully connected
   - Must not have cycles
2. Use Union-Find (Disjoint Set) algorithm:
   - Initialize each node as its own set
   - For each edge, union the nodes
   - If nodes already in same set -> cycle found
3. Time: O(N*α(N)), Space: O(N)
   where α is inverse Ackermann function
"""

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True

        for x, y in edges:
            if not union(x, y):
                return False

        return True

def test_valid_tree():
    solution = Solution()
    
    # Test Case 1: Valid tree
    n1 = 5
    edges1 = [[0,1], [0,2], [0,3], [1,4]]
    print("Test 1: Valid tree")
    print(f"Nodes: {n1}, Edges: {edges1}")
    print(f"Is valid tree: {solution.validTree(n1, edges1)}")  # Expected: True
    
    # Test Case 2: Contains cycle
    n2 = 4
    edges2 = [[0,1], [1,2], [2,3], [1,3]]
    print("\nTest 2: Graph with cycle")
    print(f"Nodes: {n2}, Edges: {edges2}")
    print(f"Is valid tree: {solution.validTree(n2, edges2)}")  # Expected: False
    
    # Test Case 3: Disconnected components
    n3 = 4
    edges3 = [[0,1], [2,3]]
    print("\nTest 3: Disconnected components")
    print(f"Nodes: {n3}, Edges: {edges3}")
    print(f"Is valid tree: {solution.validTree(n3, edges3)}")  # Expected: False
    
    # Test Case 4: Single node
    n4 = 1
    edges4 = []
    print("\nTest 4: Single node")
    print(f"Nodes: {n4}, Edges: {edges4}")
    print(f"Is valid tree: {solution.validTree(n4, edges4)}")  # Expected: True

if __name__ == "__main__":
    test_valid_tree()
