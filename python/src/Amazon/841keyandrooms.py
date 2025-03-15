"""
LeetCode 841: Keys and Rooms

There are n rooms labeled from 0 to n-1 and all rooms are locked except for room 0. 
Your goal is to visit all the rooms. When you visit a room, you may find a set of 
distinct keys in it. Each key has a number on it, denoting which room it unlocks, 
and you can take all of them with you to unlock the other rooms.

Return true if you can visit all the rooms, or false otherwise.

Constraints:
- n == rooms.length
- 2 <= n <= 1000
- 0 <= rooms[i].length <= 1000
- 1 <= sum(rooms[i].length) <= 3000
- 0 <= rooms[i][j] < n
- All the values of rooms[i] are unique
"""

from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """
        Optimized iterative DFS solution
        Time: O(N + K) where N = rooms, K = total keys
        Space: O(N)
        """
        visited = {0}  # Start with room 0
        stack = [0]
        
        while stack:
            room = stack.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
                    
        return len(visited) == len(rooms)
    
    def canVisitAllRooms_bfs(self, rooms: List[List[int]]) -> bool:
        """
        Alternative BFS solution
        Time: O(N + K)
        Space: O(N)
        """
        visited = {0}
        queue = deque([0])
        
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
                    
        return len(visited) == len(rooms)


def validate_rooms(rooms: List[List[int]]) -> bool:
    """Validate rooms configuration"""
    n = len(rooms)
    if not 2 <= n <= 1000:
        return False
        
    total_keys = sum(len(room) for room in rooms)
    if not 1 <= total_keys <= 3000:
        return False
        
    # Check if keys are valid and unique in each room
    for room in rooms:
        if len(room) > 1000:
            return False
        if len(set(room)) != len(room):
            return False
        if any(key >= n or key < 0 for key in room):
            return False
            
    return True


def test_keys_and_rooms():
    """Test function for Keys and Rooms"""
    test_cases = [
        ([[1], [2], [3], []], True),
        ([[1,3], [3,0,1], [2], [0]], False),
        ([[1], [], [2], [3]], False),
        ([[1], [1]], True),
        ([[1,2,3], [2], [3], []], True),
        ([[1], [2], [], [3]], False),
        ([[1,2], [2,3], [1,3], [0,1]], True)
    ]
    
    solution = Solution()
    
    for i, (rooms, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.canVisitAllRooms(rooms)
        result2 = solution.canVisitAllRooms_bfs(rooms)
        
        print(f"\nTest case {i}:")
        print(f"Rooms configuration:")
        for j, room in enumerate(rooms):
            print(f"Room {j}: keys={room}")
        print(f"Expected: {expected}")
        print(f"DFS solution: {result1} {'✓' if result1 == expected else '✗'}")
        print(f"BFS solution: {result2} {'✓' if result2 == expected else '✗'}")
        
        # Validate room configuration
        is_valid = validate_rooms(rooms)
        print(f"Valid configuration: {'✓' if is_valid else '✗'}")
        
        # If solution is True, show possible path
        if result1:
            path = []
            visited = {0}
            stack = [0]
            while stack:
                room = stack.pop()
                path.append(room)
                for key in rooms[room]:
                    if key not in visited:
                        visited.add(key)
                        stack.append(key)
            print(f"Possible path: {' -> '.join(map(str, path))}")


if __name__ == "__main__":
    test_keys_and_rooms()
