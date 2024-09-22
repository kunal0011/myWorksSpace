class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic_reachable = [
            [False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, reachable):
            reachable[r][c] = True
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and not reachable[new_r][new_c]:
                    if heights[new_r][new_c] >= heights[r][c]:
                        dfs(new_r, new_c, reachable)

        # Perform DFS for all cells adjacent to the Pacific Ocean (top and left edges)
        for r in range(rows):
            dfs(r, 0, pacific_reachable)  # Left edge
            dfs(r, cols - 1, atlantic_reachable)  # Right edge

        for c in range(cols):
            dfs(0, c, pacific_reachable)  # Top edge
            dfs(rows - 1, c, atlantic_reachable)  # Bottom edge

        # Collect all cells that can reach both oceans
        result = []
        for r in range(rows):
            for c in range(cols):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])

        return result


# Example usage:
solution = Solution()
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]
# Expected output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
print(solution.pacificAtlantic(heights))
