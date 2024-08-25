from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        result = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        # Initialize BFS with all water cells
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    queue.append((i, j))

        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Perform BFS
        while queue:
            x, y = queue.popleft()
            current_height = result[x][y]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if result[nx][ny] > current_height + 1:
                        result[nx][ny] = current_height + 1
                        queue.append((nx, ny))

        return result
