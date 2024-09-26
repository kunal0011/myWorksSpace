from collections import deque
from typing import List


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # Get the dimensions of the forest
        m, n = len(forest), len(forest[0])

        # Function to perform BFS from (sr, sc) to (tr, tc)
        def bfs(sr, sc, tr, tc):
            if sr == tr and sc == tc:
                return 0
            queue = deque([(sr, sc, 0)])  # queue stores (row, col, distance)
            visited = set((sr, sc))
            # right, down, left, up
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while queue:
                r, c, dist = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and forest[nr][nc] != 0:
                        if nr == tr and nc == tc:
                            return dist + 1
                        queue.append((nr, nc, dist + 1))
                        visited.add((nr, nc))

            return -1  # Return -1 if the target is unreachable

        # Collect all the trees (height > 1) with their positions
        trees = [(forest[r][c], r, c) for r in range(m)
                 for c in range(n) if forest[r][c] > 1]
        # Sort the trees by height
        trees.sort()

        # Start from (0, 0)
        sr, sc = 0, 0
        total_steps = 0

        for height, tr, tc in trees:
            steps = bfs(sr, sc, tr, tc)
            if steps == -1:
                return -1  # If any tree is unreachable, return -1
            total_steps += steps
            sr, sc = tr, tc  # Move to the position of the tree we just cut

        return total_steps
