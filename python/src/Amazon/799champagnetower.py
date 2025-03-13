"""
LeetCode 799: Champagne Tower

We stack glasses in a pyramid, where the first row has 1 glass, the second row has 2 glasses, 
and so on until the 100th row. Each glass holds one cup of champagne.

Then, some champagne is poured into the first glass at the top. When the topmost glass is full, 
any excess liquid poured will fall equally to the left and right glasses (half to each glass). 
When those glasses become full, any excess champagne will fall equally to the left and right 
of those glasses, and so on.

Return how full the jth glass in the ith row is (both i and j are 0-indexed).

Constraints:
- 0 <= poured <= 10^9
- 0 <= query_row <= 99
- 0 <= query_glass <= query_row
"""

from typing import List


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Optimized solution using space-efficient DP
        Time complexity: O(query_row^2)
        Space complexity: O(query_row)
        """
        # Only need to maintain current and next row
        curr_row = [poured]
        
        for row in range(query_row):
            next_row = [0] * (row + 2)
            
            for glass in range(len(curr_row)):
                excess = (curr_row[glass] - 1) / 2.0
                if excess > 0:
                    next_row[glass] += excess
                    next_row[glass + 1] += excess
                    
            curr_row = next_row
            
        return min(1.0, curr_row[query_glass])
    
    def champagneTower_recursive(self, poured: int, query_row: int, query_glass: int) -> float:
        """
        Alternative recursive solution with memoization
        Less space-efficient but more intuitive
        """
        def flow(row: int, col: int, cache: dict) -> float:
            if col < 0 or col > row:
                return 0.0
            if row == 0 and col == 0:
                return poured
                
            key = (row, col)
            if key in cache:
                return cache[key]
                
            # Calculate flow from above glasses
            left = max(0.0, (flow(row-1, col-1, cache) - 1) / 2)
            right = max(0.0, (flow(row-1, col, cache) - 1) / 2)
            
            cache[key] = left + right
            return cache[key]
            
        return min(1.0, flow(query_row, query_glass, {}))


def validate_champagne_flow(poured: float, result: float) -> bool:
    """Validate if the result is physically possible"""
    return 0 <= result <= 1 and (poured == 0 or result >= 0)


def test_champagne_tower():
    """Test function for Champagne Tower solutions"""
    test_cases = [
        (1, 1, 1, 0.0),
        (2, 1, 1, 0.5),
        (100000009, 33, 17, 1.0),
        (0, 0, 0, 0.0),
        (1, 0, 0, 1.0),
        (4, 2, 1, 1.0),
        (6, 3, 1, 1.0),
        (10, 4, 2, 1.0)
    ]
    
    solution = Solution()
    
    for i, (poured, row, glass, expected) in enumerate(test_cases, 1):
        # Test both implementations
        result1 = solution.champagneTower(poured, row, glass)
        result2 = solution.champagneTower_recursive(poured, row, glass)
        
        print(f"\nTest case {i}:")
        print(f"Poured: {poured}")
        print(f"Query: row={row}, glass={glass}")
        print(f"Expected: {expected}")
        print(f"DP solution: {result1:.6f} {'✓' if abs(result1 - expected) < 1e-5 else '✗'}")
        print(f"Recursive: {result2:.6f} {'✓' if abs(result2 - expected) < 1e-5 else '✗'}")
        
        # Validate the solution
        is_valid = validate_champagne_flow(poured, result1)
        print(f"Valid flow: {'✓' if is_valid else '✗'}")


if __name__ == "__main__":
    test_champagne_tower()
