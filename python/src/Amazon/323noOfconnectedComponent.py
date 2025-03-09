"""
LeetCode 323 - Number of Connected Components in an Undirected Graph

Problem Statement:
You have a graph of n nodes. You are given an integer n and an array edges where 
edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi.
Return the number of connected components in the graph.

Solution Logic:
1. Create adjacency list representation of graph
2. Use DFS to explore each component:
   - Start from unvisited node
   - Mark all reachable nodes as visited
   - Each new DFS start = new component
3. Time: O(V + E), Space: O(V + E)
   where V = vertices, E = edges
"""

class Solution:
    def countComponents(self, n: int, edges: list) -> int:
        # Create an adjacency list
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Keep track of visited nodes
        visited = set()

        def dfs(node):
            visited.add(node)
            # Visit all the neighbors of the node
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # Count the number of connected components
        components = 0
        for node in range(n):
            if node not in visited:
                # Start a DFS from this unvisited node
                dfs(node)
                components += 1

        return components

def test_count_components():
    solution = Solution()
    
    # Test Case 1: Basic case
    n1 = 5
    edges1 = [[0,1], [1,2], [3,4]]
    print("Test 1: Basic case")
    print(f"Nodes: {n1}, Edges: {edges1}")
    print(f"Number of components: {solution.countComponents(n1, edges1)}")  # Expected: 2
    
    # Test Case 2: All connected
    n2 = 4
    edges2 = [[0,1], [1,2], [2,3], [3,0]]
    print("\nTest 2: All connected")
    print(f"Nodes: {n2}, Edges: {edges2}")
    print(f"Number of components: {solution.countComponents(n2, edges2)}")  # Expected: 1
    
    # Test Case 3: No edges
    n3 = 3
    edges3 = []
    print("\nTest 3: No edges")
    print(f"Nodes: {n3}, Edges: {edges3}")
    print(f"Number of components: {solution.countComponents(n3, edges3)}")  # Expected: 3

if __name__ == "__main__":
    test_count_components()
