"""
LeetCode 490 - The Maze

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). 
The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling 
until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, determine whether the ball 
can stop at the destination.

The ball can only roll in four directions: left, right, up, or down.
You may assume that the borders of the maze are all walls.
"""

from typing import List

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if not maze or not maze[0]:
            return False
            
        m, n = len(maze), len(maze[0])
        visited = set()
        
        def roll(x: int, y: int, dx: int, dy: int) -> tuple:
            """Roll the ball in a direction until hitting a wall"""
            while (0 <= x + dx < m and 
                   0 <= y + dy < n and 
                   maze[x + dx][y + dy] == 0):
                x += dx
                y += dy
            return x, y
        
        def dfs(x: int, y: int) -> bool:
            """DFS with rolling ball mechanics"""
            if (x, y) in visited:
                return False
                
            if [x, y] == destination:
                return True
                
            visited.add((x, y))
            
            # Try all four directions
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_x, next_y = roll(x, y, dx, dy)
                if dfs(next_x, next_y):
                    return True
                    
            return False
        
        return dfs(start[0], start[1])


def test_maze():
    """Test function to verify the solution with multiple test cases"""
    solution = Solution()
    
    test_cases = [
        # Test case 1: Simple path exists
        {
            "maze": [
                [0,0,1,0,0],
                [0,0,0,0,0],
                [0,0,0,1,0],
                [1,1,0,1,1],
                [0,0,0,0,0]
            ],
            "start": [0,4],
            "destination": [4,4],
            "expected": True
        },
        # Test case 2: No path exists
        {
            "maze": [
                [0,0,1,0,0],
                [0,0,0,0,0],
                [0,0,0,1,0],
                [1,1,0,1,1],
                [0,0,0,0,0]
            ],
            "start": [0,4],
            "destination": [3,2],
            "expected": False
        },
        # Test case 3: Empty maze
        {
            "maze": [],
            "start": [0,0],
            "destination": [0,0],
            "expected": False
        }
    ]
    
    for i, tc in enumerate(test_cases, 1):
        result = solution.hasPath(tc["maze"], tc["start"], tc["destination"])
        status = "✓" if result == tc["expected"] else "✗"
        print(f"Test {i}: {status}")
        print(f"Expected: {tc['expected']}, Got: {result}\n")

if __name__ == "__main__":
    test_maze()
