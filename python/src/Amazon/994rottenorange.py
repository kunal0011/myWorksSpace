from collections import deque


class Solution:
    def orangesRotting(self, grid) -> int:
        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])

        # Queue to hold the positions of all initially rotten oranges
        queue = deque()
        fresh_count = 0

        # Step 1: Add all the initially rotten oranges to the queue and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # If there are no fresh oranges, return 0 (no time needed)
        if fresh_count == 0:
            return 0

        # Step 2: BFS to spread the rot
        minutes_passed = 0
        # Right, Down, Left, Up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            minutes_passed += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # Check all 4 directions
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If the adjacent cell is a fresh orange, rot it and add it to the queue
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Rotten the fresh orange
                        fresh_count -= 1  # Decrease the fresh orange count
                        queue.append((nr, nc))

        # If there are still fresh oranges left, return -1 (not all could rot)
        return minutes_passed - 1 if fresh_count == 0 else -1
