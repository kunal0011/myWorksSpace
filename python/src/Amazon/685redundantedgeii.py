from typing import List


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        candidate1 = None
        candidate2 = None

        # Step 1: Check whether there is a node with two parents
        for u, v in edges:
            if v in parent:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
            else:
                parent[v] = u

        # Union-Find to detect cycles
        def find(uf, x):
            if uf[x] != x:
                uf[x] = find(uf, uf[x])
            return uf[x]

        def union(uf, x, y):
            rootX = find(uf, x)
            rootY = find(uf, y)
            if rootX == rootY:
                return False
            uf[rootY] = rootX
            return True

        # Step 2: Try to build the tree
        uf = {i: i for i in range(1, len(edges) + 1)}

        for u, v in edges:
            if [u, v] == candidate2:
                continue  # Skip the second candidate edge if it exists
            if not union(uf, u, v):
                # If we find a cycle
                if candidate1:
                    return candidate1
                return [u, v]

        # If no cycle, return the second candidate
        return candidate2


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    edges1 = [[1, 2], [1, 3], [2, 3]]
    print(sol.findRedundantDirectedConnection(edges1))  # Output: [2, 3]

    # Test case 2
    edges2 = [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]
    print(sol.findRedundantDirectedConnection(edges2))  # Output: [4, 1]
