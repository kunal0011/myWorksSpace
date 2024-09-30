from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        # Step 1: Initialize the queue with all gates' positions
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:  # Gate found
                    queue.append((r, c))

        # Step 2: BFS from the gates
        # Right, Left, Down, Up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                # Check bounds and if it's an empty room
                if 0 <= new_r < rows and 0 <= new_c < cols and rooms[new_r][new_c] == float('inf'):
                    rooms[new_r][new_c] = rooms[r][c] + 1  # Update distance
                    # Add to the queue for further exploration
                    queue.append((new_r, new_c))
