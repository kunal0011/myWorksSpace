"""
LeetCode 688: Knight Probability in Chessboard

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves.
The knight has eight possible moves it can make (2,1) or (1,2) in any direction.
Each time the knight is going to move, it chooses one of eight possible moves uniformly at random
(even if the piece would go off the chessboard) and moves there.

Return the probability that the knight remains on the board after exactly k moves.
"""

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Cache for memoization
        cache = {}
        
        def dfs(r: int, c: int, moves: int) -> float:
            # Base cases
            if not (0 <= r < n and 0 <= c < n):
                return 0
            if moves == 0:
                return 1
            
            # Check cache
            if (r, c, moves) in cache:
                return cache[(r, c, moves)]
            
            # Possible knight moves
            directions = [(-2, -1), (-1, -2), (1, -2), (2, -1),
                         (2, 1), (1, 2), (-1, 2), (-2, 1)]
            
            # Calculate probability
            probability = 0
            for dr, dc in directions:
                probability += dfs(r + dr, c + dc, moves - 1) / 8
            
            # Cache and return
            cache[(r, c, moves)] = probability
            return probability
        
        return dfs(row, column, k)

# Test driver
def test_knight_probability():
    test_cases = [
        # n, k, row, column, expected
        (3, 2, 0, 0, 0.0625),
        (1, 0, 0, 0, 1.0),
        (3, 3, 0, 0, 0.015625)
    ]
    
    solution = Solution()
    for i, (n, k, row, column, expected) in enumerate(test_cases):
        result = solution.knightProbability(n, k, row, column)
        print(f"Test case {i + 1}:")
        print(f"Input: n = {n}, k = {k}, row = {row}, column = {column}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'✓ Passed' if abs(result - expected) < 1e-5 else '✗ Failed'}\n")

if __name__ == "__main__":
    test_knight_probability()
