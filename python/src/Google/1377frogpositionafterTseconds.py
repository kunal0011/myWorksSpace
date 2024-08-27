from collections import defaultdict


class Solution:
    def frogPosition(self, n: int, edges: list[list[int]], t: int, target: int) -> float:
        # Build the tree as an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS to find the probability of reaching the target at time t
        def dfs(node: int, parent: int, time: int, prob: float) -> float:
            # If no more moves possible
            if time == 0 or len(graph[node]) == (1 if node != 1 else 0):
                return prob if node == target else 0.0

            # Number of valid next moves
            count = len(graph[node]) - (1 if node != 1 else 0)
            for neighbor in graph[node]:
                if neighbor != parent:  # Avoid going back to the parent node
                    result = dfs(neighbor, node, time - 1, prob / count)
                    if result > 0:  # If the result is non-zero, we've reached the target
                        return result

            return 0.0

        # Start DFS from the root node (1) with probability 1.0
        return dfs(1, -1, t, 1.0)
