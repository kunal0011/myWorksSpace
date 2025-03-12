"""
LeetCode 547 - Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, 
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly 
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
- 1 <= n <= 200
- n == isConnected.length
- n == isConnected[i].length
- isConnected[i][j] is 1 or 0
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]
"""

from typing import List
from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        DFS solution to find number of provinces
        Time Complexity: O(n^2) where n is the number of cities
        Space Complexity: O(n) for the visited set
        """
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city: int) -> None:
            visited.add(city)
            # Check connections with all other cities
            for next_city in range(n):
                if isConnected[city][next_city] == 1 and next_city not in visited:
                    dfs(next_city)
        
        # Check each unvisited city
        for city in range(n):
            if city not in visited:
                dfs(city)
                provinces += 1
                
        return provinces
    
    def findCircleNum_bfs(self, isConnected: List[List[int]]) -> int:
        """
        Alternative BFS solution
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def bfs(start: int) -> None:
            queue = deque([start])
            visited.add(start)
            
            while queue:
                city = queue.popleft()
                for next_city in range(n):
                    if isConnected[city][next_city] == 1 and next_city not in visited:
                        visited.add(next_city)
                        queue.append(next_city)
        
        for city in range(n):
            if city not in visited:
                bfs(city)
                provinces += 1
                
        return provinces
    
    def findCircleNum_unionfind(self, isConnected: List[List[int]]) -> int:
        """
        Union-Find solution (most efficient for dense graphs)
        Time Complexity: O(n^2 * α(n)) where α is the inverse Ackermann function
        Space Complexity: O(n)
        """
        n = len(isConnected)
        parent = list(range(n))
        rank = [0] * n
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]
        
        def union(x: int, y: int) -> None:
            px, py = find(x), find(y)
            if px == py:
                return
            # Union by rank
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
        
        # Process all edges
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        # Count unique parents (provinces)
        return len({find(i) for i in range(n)})


def test_number_of_provinces():
    """
    Test function to verify all solution approaches
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([[1,1,0],
          [1,1,0],
          [0,0,1]], 2),
          
        ([[1,0,0],
          [0,1,0],
          [0,0,1]], 3),
          
        # Complex test cases
        ([[1,1,1],
          [1,1,1],
          [1,1,1]], 1),  # All connected
          
        ([[1,0,0,0],
          [0,1,0,0],
          [0,0,1,0],
          [0,0,0,1]], 4),  # No connections
          
        ([[1,1,0,0],
          [1,1,1,0],
          [0,1,1,0],
          [0,0,0,1]], 2),  # Multiple connections
          
        # Edge cases
        ([[1]], 1),  # Single city
        
        ([[1,1],
          [1,1]], 1),  # Two connected cities
    ]
    
    for i, (isConnected, expected) in enumerate(test_cases, 1):
        # Test all three solutions
        result_dfs = solution.findCircleNum(isConnected)
        result_bfs = solution.findCircleNum_bfs(isConnected)
        result_uf = solution.findCircleNum_unionfind(isConnected)
        
        print(f"\nTest Case {i}:")
        print("Input matrix:")
        for row in isConnected:
            print(row)
        print(f"Expected provinces: {expected}")
        print(f"DFS Solution: {'✓' if result_dfs == expected else '✗'} (Got: {result_dfs})")
        print(f"BFS Solution: {'✓' if result_bfs == expected else '✗'} (Got: {result_bfs})")
        print(f"Union-Find: {'✓' if result_uf == expected else '✗'} (Got: {result_uf})")
        
        if result_dfs != expected or result_bfs != expected or result_uf != expected:
            print("❌ Test case failed!")
        else:
            print("✅ Test case passed!")


if __name__ == "__main__":
    test_number_of_provinces()