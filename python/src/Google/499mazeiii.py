"""
LeetCode 499 - The Maze III

Problem Statement:
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up (u), down (d), left (l) or right (r), 
but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. 
The ball will drop into the hole if it rolls onto the hole.

Given the maze, the ball's starting position, the hole position and the dimensions of the maze, find the shortest distance for the ball to drop 
into the hole by following a path. The distance is defined by the number of empty spaces the ball needs to traverse from the starting position 
(excluded) to the hole (included). Output the moving directions by using 'u', 'd', 'l' or 'r'. Since there could be several different shortest 
ways, output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".
"""

from typing import List
import heapq


class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])

        def get_next_positions(x: int, y: int, dx: int, dy: int) -> tuple:
            """Returns the next stop position and distance for a given direction"""
            distance = 0
            # Keep rolling until hitting a wall or the hole
            while 0 <= x + dx < m and 0 <= y + dy < n and maze[x + dx][y + dy] == 0:
                x += dx
                y += dy
                distance += 1
                if [x, y] == hole:  # Stop if we hit the hole
                    break
            return x, y, distance

        # Priority queue to store (distance, path, x, y)
        pq = [(0, "", ball[0], ball[1])]
        # Dictionary to store visited states with their distances
        seen = {(ball[0], ball[1]): [0, ""]}  # (x, y) -> [distance, path]

        # Directions: up, left, down, right (lexicographical order)
        directions = [(-1, 0, 'u'), (0, -1, 'l'), (1, 0, 'd'), (0, 1, 'r')]

        while pq:
            dist, path, x, y = heapq.heappop(pq)

            # If we've found a shorter/lexicographically smaller path to current position
            if [x, y] == hole:
                return path

            # Try all four directions
            for dx, dy, direction in directions:
                next_x, next_y, d = get_next_positions(x, y, dx, dy)
                new_dist = dist + d

                # If new position not seen or we found a better path
                if (next_x, next_y) not in seen or \
                   [new_dist, path + direction] < seen[(next_x, next_y)]:
                    seen[(next_x, next_y)] = [new_dist, path + direction]
                    heapq.heappush(
                        pq, (new_dist, path + direction, next_x, next_y))

        return "impossible"

# Test driver


def run_tests():
    solution = Solution()

    # Test Case 1
    maze1 = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0]
    ]
    ball1 = [4, 3]
    hole1 = [0, 1]
    print("Test Case 1:")
    # Expected: "lul"
    print(f"Result: {solution.findShortestWay(maze1, ball1, hole1)}")

    # Test Case 2
    maze2 = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [0, 1, 0, 0, 0]
    ]
    ball2 = [4, 3]
    hole2 = [3, 0]
    print("\nTest Case 2:")
    # Expected: "impossible"
    print(f"Result: {solution.findShortestWay(maze2, ball2, hole2)}")

    # Test Case 3
    maze3 = [[0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [
        0, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 0, 0]]
    ball3 = [0, 0]
    hole3 = [1, 1]
    print("\nTest Case 3:")
    # Expected: "impossible"
    print(f"Result: {solution.findShortestWay(maze3, ball3, hole3)}")


if __name__ == "__main__":
    run_tests()
