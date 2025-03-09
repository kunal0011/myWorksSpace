"""
LeetCode 286 - Walls and Gates

Problem Statement:
You are given an m x n grid rooms initialized with these three possible values:
- -1: A wall or an obstacle
- 0: A gate
- INF (2^31 - 1): An empty room
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate,
it should be filled with INF.

Logic:
1. Use BFS starting from all gates simultaneously
2. Initialize queue with all gate positions
3. For each position in queue:
   - Check all 4 directions
   - If new position is valid empty room, update distance
   - Add new position to queue
4. BFS ensures shortest path to each room
"""

from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return

        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        # Step 1: Initialize the queue with all gates' positions
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:  # Gate found
                    queue.append((r, c))

        # Step 2: BFS from the gates
        # Right, Left, Down, Up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                # Check bounds and if it's an empty room
                if 0 <= new_r < rows and 0 <= new_c < cols and rooms[new_r][new_c] == float('inf'):
                    rooms[new_r][new_c] = rooms[r][c] + 1  # Update distance
                    # Add to the queue for further exploration
                    queue.append((new_r, new_c))


def test_walls_and_gates():
    solution = Solution()
    
    # Test cases
    INF = float('inf')
    test_cases = [
        # Test case 1: Standard case
        {
            'input': [
                [INF, -1, 0, INF],
                [INF, INF, INF, -1],
                [INF, -1, INF, -1],
                [0, -1, INF, INF]
            ],
            'expected': [
                [3, -1, 0, 1],
                [2, 2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4]
            ]
        },
        # Test case 2: Single cell
        {
            'input': [[0]],
            'expected': [[0]]
        },
        # Test case 3: No gates
        {
            'input': [[INF, -1], [-1, INF]],
            'expected': [[INF, -1], [-1, INF]]
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        rooms = [row[:] for row in test_case['input']]  # Create deep copy
        solution.wallsAndGates(rooms)
        assert rooms == test_case['expected'], f"Test case {i + 1} failed"
        print(f"Test case {i + 1} passed")
        print("Input:")
        for row in test_case['input']:
            print(row)
        print("Output:")
        for row in rooms:
            print(row)
        print()

if __name__ == "__main__":
    test_walls_and_gates()
    print("All test cases passed!")
