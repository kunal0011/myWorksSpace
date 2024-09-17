from collections import defaultdict
from typing import List


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # Build adjacency list for the graph representation of the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS function to calculate probability
        def dfs(node, parent, time, prob):
            # If we are at the target and either no more time is left or it's a leaf node, return the probability
            if node == target:
                if time == 0 or len(graph[node]) == 1 and node != 1:
                    return prob
                return 0

            # If time is exhausted, return 0
            if time == 0:
                return 0

            # Calculate the number of children (ignore the parent)
            children = [child for child in graph[node] if child != parent]
            if not children:  # If no children, this is a leaf node
                return 0

            # Spread the probability equally among the children
            prob_per_child = prob / len(children)
            for child in children:
                result = dfs(child, node, time - 1, prob_per_child)
                if result > 0:
                    return result

            return 0

        # Start DFS from node 1 (root), with initial probability of 1.0 and time t
        return dfs(1, -1, t, 1.0)


# Testing
solution = Solution()
n = 7
edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]]
t = 2
target = 4
print("Python Test Result:", solution.frogPosition(
    n, edges, t, target))  # Output should be 0.3333 (1/3)
