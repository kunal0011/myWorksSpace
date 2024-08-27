class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # Starting point (0, 0)
        x, y = 0, 0

        # Set to store visited points
        visited = set()
        visited.add((x, y))

        # Traverse the path
        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1

            # Check if this point has been visited
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))

        # No crossing occurred
        return False
