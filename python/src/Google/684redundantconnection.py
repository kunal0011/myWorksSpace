from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        rank = [0] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        for edge in edges:
            u, v = edge
            if find(u) == find(v):
                return edge  # This is the redundant edge
            union(u, v)

        return []


# Example usage
solution = Solution()
edges1 = [[1, 2], [1, 3], [2, 3]]
edges2 = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]

print(solution.findRedundantConnection(edges1))  # Output: [2, 3]
print(solution.findRedundantConnection(edges2))  # Output: [1, 4]
