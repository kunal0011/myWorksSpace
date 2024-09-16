class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        # Step 1: Initialize an array to keep track of in-degrees
        in_degree = [0] * n

        # Step 2: Calculate the in-degree of each node
        for u, v in edges:
            in_degree[v] += 1

        # Step 3: Collect all nodes with zero in-degree
        result = [i for i in range(n) if in_degree[i] == 0]

        return result


# Testing
solution = Solution()
n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
print("Python Test Result:", solution.findSmallestSetOfVertices(
    n, edges))  # Output should be [0, 3]
