from collections import deque


class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        queue = deque()

        # Step 1: Add all gates to the queue
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:  # Gate found
                    queue.append((i, j))

        # Step 2: BFS from the gates
        # Down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            i, j = queue.popleft()
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                # If new position is in bounds and is an empty room
                if 0 <= ni < m and 0 <= nj < n and rooms[ni][nj] == 2147483647:
                    rooms[ni][nj] = rooms[i][j] + 1
                    queue.append((ni, nj))
