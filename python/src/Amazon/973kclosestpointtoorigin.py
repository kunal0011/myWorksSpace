"""
LeetCode 973: K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane 
and an integer k, return the k closest points to the origin (0, 0).

The distance between two points is the Euclidean distance: √((x1 - x2)² + (y1 - y2)²).

You may return the answer in any order. The answer is guaranteed to be unique 
(except for the order that it is in).

Constraints:
- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4
"""

from typing import List
import heapq
from math import sqrt
from time import perf_counter

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # No need for sqrt since we just need relative distances
        return heapq.nsmallest(k, points, key=lambda p: p[0]*p[0] + p[1]*p[1])
    
    def kClosest_heap(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Alternative implementation using max heap"""
        heap = []
        for x, y in points:
            dist = x*x + y*y
            if len(heap) < k:
                heapq.heappush(heap, (-dist, [x, y]))
            elif -dist > heap[0][0]:
                heapq.heapreplace(heap, (-dist, [x, y]))
        return [point for (_, point) in heap]

def validate_input(points: List[List[int]], k: int) -> bool:
    """Validate input according to constraints"""
    if not 1 <= k <= len(points) <= 10**4:
        return False
    return all(-10**4 <= x <= 10**4 and -10**4 <= y <= 10**4 
              for x, y in points)

def visualize_points(points: List[List[int]], closest: List[List[int]]) -> None:
    """Create ASCII visualization of points"""
    scale = 10
    grid_size = 10
    grid = [[' ' for _ in range(2*grid_size+1)] for _ in range(2*grid_size+1)]
    
    # Mark origin
    grid[grid_size][grid_size] = '+'
    
    # Plot points
    for x, y in points:
        scaled_x = grid_size + round(x/scale)
        scaled_y = grid_size - round(y/scale)
        if 0 <= scaled_x < 2*grid_size+1 and 0 <= scaled_y < 2*grid_size+1:
            grid[scaled_y][scaled_x] = '·'
    
    # Mark closest points
    for x, y in closest:
        scaled_x = grid_size + round(x/scale)
        scaled_y = grid_size - round(y/scale)
        if 0 <= scaled_x < 2*grid_size+1 and 0 <= scaled_y < 2*grid_size+1:
            grid[scaled_y][scaled_x] = '*'
    
    # Print grid
    for row in grid:
        print(''.join(row))

def test_k_closest():
    """Test function for K Closest Points to Origin"""
    test_cases = [
        ([[1,3],[-2,2]], 1, [[-2,2]]),
        ([[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]),
        ([[1,1],[-1,-1],[2,2],[-2,-2]], 2, [[1,1],[-1,-1]]),
        ([[1,1]], 1, [[1,1]]),
        ([[2,2],[-2,2],[-2,-2],[2,-2]], 3, [[2,2],[-2,2],[-2,-2]])
    ]
    
    solution = Solution()
    
    for i, (points, k, expected) in enumerate(test_cases, 1):
        is_valid = validate_input(points, k)
        
        start_time = perf_counter()
        result1 = solution.kClosest(points, k)
        time1 = perf_counter() - start_time
        
        start_time = perf_counter()
        result2 = solution.kClosest_heap(points, k)
        time2 = perf_counter() - start_time
        
        print(f"\nTest case {i}:")
        print(f"Points: {points}")
        print(f"k: {k}")
        print("\nVisualization:")
        visualize_points(points, result1)
        
        # Sort results for comparison
        result1.sort()
        result2.sort()
        expected.sort()
        
        print(f"\nHeapsort solution: {result1}")
        print(f"Max-heap solution: {result2}")
        print(f"Time (heapsort): {time1*1000:.3f}ms")
        print(f"Time (max-heap): {time2*1000:.3f}ms")
        print(f"Valid input: {'✓' if is_valid else '✗'}")
        print(f"Test passed: {'✓' if result1 == expected else '✗'}")
        
        # Additional statistics
        distances = [sqrt(x*x + y*y) for x, y in result1]
        print(f"\nDistances of closest points: {[f'{d:.2f}' for d in distances]}")
        print(f"Average distance: {sum(distances)/len(distances):.2f}")

if __name__ == "__main__":
    test_k_closest()
