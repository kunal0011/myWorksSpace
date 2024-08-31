import heapq


class Solution:
    def findShortestWay(self, maze: list[list[int]], ball: list[int], hole: list[int]) -> str:
        m, n = len(maze), len(maze[0])

        # Define possible moves and corresponding directions
        directions = [(-1, 0, 'u'), (1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r')]

        # Priority queue: (distance, path, x, y)
        heap = [(0, "", ball[0], ball[1])]
        # Distance map to store the shortest path to each cell
        distance = {(ball[0], ball[1]): (0, "")}

        def roll(x, y, dx, dy):
            steps = 0
            while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
                steps += 1
                if [x, y] == hole:
                    break
            return x, y, steps

        while heap:
            dist, path, x, y = heapq.heappop(heap)

            if [x, y] == hole:
                return path

            for dx, dy, d in directions:
                nx, ny, steps = roll(x, y, dx, dy)
                new_dist = dist + steps
                new_path = path + d

                if (nx, ny) not in distance or (new_dist, new_path) < distance[(nx, ny)]:
                    distance[(nx, ny)] = (new_dist, new_path)
                    heapq.heappush(heap, (new_dist, new_path, nx, ny))

        return "impossible"
