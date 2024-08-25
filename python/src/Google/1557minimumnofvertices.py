from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Initialize an in-degree list
        in_degree = [0] * n

        # Step 2: Update in-degrees based on edges
        for u, v in edges:
            in_degree[v] += 1

        # Step 3: Collect vertices with zero in-degrees
        result = [i for i in range(n) if in_degree[i] == 0]

        return result
