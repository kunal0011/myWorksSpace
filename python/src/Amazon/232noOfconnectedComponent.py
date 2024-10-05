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
