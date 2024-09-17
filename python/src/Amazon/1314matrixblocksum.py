from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # Step 1: Build the prefix sum matrix
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = mat[i][j] + \
                    prefix[i + 1][j] + prefix[i][j + 1] - prefix[i][j]

        # Step 2: Compute the result matrix using the prefix sum matrix
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                # Define the bounds for the block
                r1, c1 = max(0, i - K), max(0, j - K)
                r2, c2 = min(m - 1, i + K), min(n - 1, j + K)

                # Using prefix sum to compute the block sum
                result[i][j] = prefix[r2 + 1][c2 + 1] - \
                    prefix[r1][c2 + 1] - prefix[r2 + 1][c1] + prefix[r1][c1]

        return result


# Testing
solution = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
K = 1
# Output: [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
print("Python Test Result:", solution.matrixBlockSum(mat, K))
