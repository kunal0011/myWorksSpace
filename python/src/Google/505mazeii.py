import heapq


class Solution:
    def shortestDistance(self, maze: list[list[int]], start: list[int], destination: list[int]) -> int:
        def roll(maze, x, y, dx, dy):
            steps = 0
            while 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[0]) and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
                steps += 1
            return x, y, steps

        m, n = len(maze), len(maze[0])
        distances = [[float('inf')] * n for _ in range(m)]
        distances[start[0]][start[1]] = 0
        heap = [(0, start[0], start[1])]

        while heap:
            dist, x, y = heapq.heappop(heap)

            if [x, y] == destination:
                return dist

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny, steps = roll(maze, x, y, dx, dy)
                new_dist = dist + steps

                if new_dist < distances[nx][ny]:
                    distances[nx][ny] = new_dist
                    heapq.heappush(heap, (new_dist, nx, ny))

        return -1
