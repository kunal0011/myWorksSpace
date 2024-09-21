from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([start])
        visited = set()
        visited.add(tuple(start))

        while queue:
            x, y = queue.popleft()
            # If we reach the destination
            if [x, y] == destination:
                return True

            for dx, dy in directions:
                nx, ny = x, y
                # Roll the ball in the current direction until hitting a wall
                while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy

                # If the new position is not visited, add it to the queue
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

        return False


# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    maze1 = [[0, 0, 0],
             [0, 1, 0],
             [0, 0, 0]]
    start1 = [0, 0]
    destination1 = [0, 2]
    print(sol.hasPath(maze1, start1, destination1))  # Expected output: True

    # Test case 2
    maze2 = [[0, 0, 0],
             [0, 1, 0],
             [0, 0, 0]]
    start2 = [0, 0]
    destination2 = [1, 2]
    print(sol.hasPath(maze2, start2, destination2))  # Expected output: False
