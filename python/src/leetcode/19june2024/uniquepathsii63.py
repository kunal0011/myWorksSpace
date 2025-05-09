from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # Initialize dp array
        dp = [[0] * n for _ in range(m)]

        # Initialize dp[0][0]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        # Initialize first row (can only come from left)
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:

                dp[0][j] = dp[0][j-1]

        # Initialize first column (can only come from above)

        for i in range(1, m):

            if obstacleGrid[i][0] == 0:

                dp[i][0] = dp[i-1][0]

        # Fill the dp table

        for i in range(1, m):

            for j in range(1, n):

                if obstacleGrid[i][j] == 0:

                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


if __name__ == '__main__':

    s = Solution()

    print(s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
