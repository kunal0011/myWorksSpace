"""
LeetCode 675: Cut Off Trees for Golf Event

Problem Statement:
You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. 
In this matrix:
- 0 represents the obstacle that can't be traversed
- 1 represents the ground that can be walked through
- A number greater than 1 represents a tree that can be walked through, and this number is the tree's height.

You must cut off all the trees in the forest in the order of tree's height (from lowest to highest). 
You can walk in any of the four directions (up, down, left, right) in one step.

Return the minimum steps you need to walk to cut off all the trees. If you can't cut off all the trees, return -1.
"""

from typing import List
import heapq
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0] or forest[0][0] == 0:
            return -1
            
        m, n = len(forest), len(forest[0])
        
        def manhattan_distance(r1: int, c1: int, r2: int, c2: int) -> int:
            return abs(r1 - r2) + abs(c1 - c2)
        
        def a_star(sr: int, sc: int, tr: int, tc: int) -> int:
            if sr == tr and sc == tc:
                return 0
                
            heap = [(manhattan_distance(sr, sc, tr, tc), 0, sr, sc)]
            visited = {(sr, sc)}
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            
            while heap:
                _, steps, r, c = heapq.heappop(heap)
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if (0 <= nr < m and 0 <= nc < n and 
                        (nr, nc) not in visited and 
                        forest[nr][nc] != 0):
                        
                        if nr == tr and nc == tc:
                            return steps + 1
                            
                        visited.add((nr, nc))
                        priority = steps + 1 + manhattan_distance(nr, nc, tr, tc)
                        heapq.heappush(heap, (priority, steps + 1, nr, nc))
            
            return -1
        
        # Collect and sort trees
        trees = sorted((forest[r][c], r, c) 
                      for r in range(m) 
                      for c in range(n) 
                      if forest[r][c] > 1)
        
        total_steps = curr_r = curr_c = 0
        
        # Cut trees in order
        for _, target_r, target_c in trees:
            steps = a_star(curr_r, curr_c, target_r, target_c)
            if steps == -1:
                return -1
            total_steps += steps
            curr_r, curr_c = target_r, target_c
            
        return total_steps

def test_cut_off_trees():
    solution = Solution()
    
    test_cases = [
        (
            [[1,2,3],[0,0,4],[7,6,5]], 
            6,
            "Basic case with valid path"
        ),
        (
            [[1,2,3],[0,0,0],[7,6,5]], 
            -1,
            "Impossible case - blocked path"
        ),
        (
            [[2,3,4],[0,0,5],[8,7,6]], 
            6,
            "Complex path required"
        ),
        (
            [[1]], 
            0,
            "Single cell, no trees"
        ),
        (
            [[0]], 
            -1,
            "Single obstacle"
        ),
        (
            [[1,2],[3,4]], 
            3,
            "Small grid with all trees"
        ),
        (
            [[2,3,4],[5,6,7],[8,9,10]], 
            8,
            "All cells are trees"
        ),
    ]
    
    for i, (forest, expected, description) in enumerate(test_cases, 1):
        result = solution.cutOffTree(forest)
        assert result == expected, \
            f"Test {i} failed: Expected {expected}, got {result}"
        print(f"\nTest {i}: {description}")
        print(f"Forest: {forest}")
        print(f"Expected steps: {expected}")
        print(f"Result: {result}")
        print("-" * 50)

if __name__ == "__main__":
    test_cut_off_trees()
