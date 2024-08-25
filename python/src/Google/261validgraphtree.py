from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])  # Path compression
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)

        if rootP == rootQ:
            return False  # A cycle detected

        if self.rank[rootP] > self.rank[rootQ]:
            self.parent[rootQ] = rootP
        elif self.rank[rootP] < self.rank[rootQ]:
            self.parent[rootP] = rootQ
        else:
            self.parent[rootQ] = rootP
            self.rank[rootP] += 1

        return True


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree needs exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # Initialize Union-Find
        uf = UnionFind(n)

        # Process each edge
        for p, q in edges:
            if not uf.union(p, q):
                return False  # A cycle detected

        return True
