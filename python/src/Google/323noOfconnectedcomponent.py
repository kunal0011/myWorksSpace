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
