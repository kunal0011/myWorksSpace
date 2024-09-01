import heapq


class Solution:
    def cheapestJump(self, A, B):
        n = len(A)
        if A[-1] == -1:
            return []

        dp = [float('inf')] * n
        path = [-1] * n
        dp[-1] = A[-1]

        for i in range(n - 2, -1, -1):
            if A[i] == -1:
                continue
            for j in range(i + 1, min(n, i + B + 1)):
                if dp[j] + A[i] < dp[i]:
                    dp[i] = dp[j] + A[i]
                    path[i] = j

        if dp[0] == float('inf'):
            return []

        result = []
        i = 0
        while i != -1:
            result.append(i + 1)
            i = path[i]

        return result
