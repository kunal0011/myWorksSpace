"""
LeetCode 1496. Path Crossing

Problem Statement:
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west.
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited.
Return false otherwise.

Time Complexity: O(n) where n is the length of path
Space Complexity: O(n) to store visited points
"""


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


# Test driver
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        "NES",          # Expected: False (no crossing)
        "NESWW",        # Expected: True (crosses at origin)
        "NNSWWEWSS",    # Expected: True (crosses path)
        "NEWS",         # Expected: True (returns to origin)
        "NESW"          # Expected: True (returns to origin)
    ]

    for i, path in enumerate(test_cases):
        result = solution.isPathCrossing(path)
        print(f"Test case {i + 1}:")
        print(f"Path: {path}")
        print(f"Does path cross?: {result}")
        print(f"Final coordinates can be calculated by following the path")
        print()
