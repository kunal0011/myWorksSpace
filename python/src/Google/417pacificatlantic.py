from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific_reachable = [[False for _ in range(cols)] for _ in range(rows)]
        atlantic_reachable = [
            [False for _ in range(cols)] for _ in range(rows)]

        def dfs(r, c, reachable):
            reachable[r][c] = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < rows and 0 <= new_c < cols and not reachable[new_r][new_c]:
                    if heights[new_r][new_c] >= heights[r][c]:
                        dfs(new_r, new_c, reachable)

        # DFS for Pacific Ocean
        for i in range(rows):
            dfs(i, 0, pacific_reachable)
            dfs(i, cols - 1, atlantic_reachable)

        # DFS for Atlantic Ocean
        for j in range(cols):
            dfs(0, j, pacific_reachable)
            dfs(rows - 1, j, atlantic_reachable)

        result = []
        for i in range(rows):
            for j in range(cols):
                if pacific_reachable[i][j] and atlantic_reachable[i][j]:
                    result.append([i, j])

        return result
