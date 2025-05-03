"""
LeetCode 505 - The Maze II

Problem Statement:
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through empty spaces by rolling
up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.
Given the maze, the ball's start position and the destination, find the shortest distance for the ball to stop at the destination. 
The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). 
If the ball cannot reach the destination, return -1.
"""

from typing import List
import heapq


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])

        def get_next_position(x: int, y: int, dx: int, dy: int) -> tuple:
            """Returns the next stop position and distance for a given direction"""
            distance = 0
            # Keep rolling until hitting a wall
            while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
                distance += 1
            return x, y, distance

        # Priority queue to store (distance, x, y)
        pq = [(0, start[0], start[1])]
        # Dictionary to store shortest distances to each position
        distances = {(start[0], start[1]): 0}

        # Four possible directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            dist, x, y = heapq.heappop(pq)

            # If we've found a longer path to current position, skip
            if dist > distances.get((x, y), float('inf')):
                continue

            # If we've reached the destination
            if [x, y] == destination:
                return dist

            # Try all four directions
            for dx, dy in directions:
                next_x, next_y, d = get_next_position(x, y, dx, dy)
                new_dist = dist + d

                # If we found a shorter path to next position
                if new_dist < distances.get((next_x, next_y), float('inf')):
                    distances[(next_x, next_y)] = new_dist
                    heapq.heappush(pq, (new_dist, next_x, next_y))

        return -1

# Test driver


def run_tests():
    solution = Solution()

    # Test Case 1
    maze1 = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start1 = [0, 4]
    destination1 = [4, 4]
    print("Test Case 1:")
    # Expected: 12
    print(f"Result: {solution.shortestDistance(maze1, start1, destination1)}")

    # Test Case 2
    maze2 = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    start2 = [0, 4]
    destination2 = [3, 2]
    print("\nTest Case 2:")
    # Expected: -1
    print(f"Result: {solution.shortestDistance(maze2, start2, destination2)}")

    # Test Case 3
    maze3 = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [
        0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
    start3 = [4, 3]
    destination3 = [0, 1]
    print("\nTest Case 3:")
    # Expected: 7
    print(f"Result: {solution.shortestDistance(maze3, start3, destination3)}")


if __name__ == "__main__":
    run_tests()
