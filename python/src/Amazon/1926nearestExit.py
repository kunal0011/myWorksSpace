from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        # right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(entrance[0], entrance[1], 0)])  # (row, col, steps)
        visited = set()
        visited.add((entrance[0], entrance[1]))

        while queue:
            r, c, steps = queue.popleft()

            # Check if we're at a boundary that's not the entrance
            if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and [r, c] != entrance:
                return steps

            # Explore neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and maze[nr][nc] == '.':
                    visited.add((nr, nc))
                    queue.append((nr, nc, steps + 1))

        return -1  # No exit found


# Testing the solution
if __name__ == "__main__":
    solution = Solution()

    # Test case
    maze = [
        ["+", "+", ".", "+"],
        [".", ".", ".", "+"],
        ["+", "+", "+", "."]
    ]
    entrance = [1, 2]
    print("Nearest Exit:", solution.nearestExit(
        maze, entrance))  # Expected output: 1
