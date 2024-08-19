from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        # If start or end is blocked, return -1
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        # Directions for moving in 8 possible ways
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]

        # Initialize the BFS queue
        queue = deque([(0, 0, 1)])  # (row, col, path_length)
        grid[0][0] = 1  # Mark as visited by setting the value to 1

        while queue:
            r, c, path_length = queue.popleft()

            # If we reached the bottom-right corner
            if r == n-1 and c == n-1:
                return path_length

            # Explore all 8 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr, nc, path_length + 1))
                    grid[nr][nc] = 1  # Mark the cell as visited

        # If there's no valid path, return -1
        return -1
