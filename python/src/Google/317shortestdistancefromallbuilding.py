from collections import deque

# Problem Description
# You want to build a house on an empty land which reaches all buildings in the shortest total travel distance. The total travel distance is the sum of the distances from the house to all the buildings. You can only move up, down, left, and right. The goal is to find the minimum sum of distances to all buildings.

# Given a 2D grid, each cell in the grid can be one of the following three types:

# 0 represents an empty land where you can build the house.
# 1 represents a building.
# 2 represents an obstacle that you cannot pass through.


class Solution:
    def shortestDistance(self, grid):
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        total_buildings = sum(val == 1 for row in grid for val in row)
        distance_sum = [[0] * n for _ in range(m)]
        reachable_count = [[0] * n for _ in range(m)]

        def bfs(start_x, start_y):
            visited = [[False] * n for _ in range(m)]
            q = deque([(start_x, start_y, 0)])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            while q:
                x, y, dist = q.popleft()
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if 0 <= new_x < m and 0 <= new_y < n and not visited[new_x][new_y]:
                        visited[new_x][new_y] = True
                        if grid[new_x][new_y] == 0:
                            distance_sum[new_x][new_y] += dist + 1
                            reachable_count[new_x][new_y] += 1
                            q.append((new_x, new_y, dist + 1))

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    bfs(x, y)

        result = float('inf')
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0 and reachable_count[x][y] == total_buildings:
                    result = min(result, distance_sum[x][y])

        return result if result != float('inf') else -1
