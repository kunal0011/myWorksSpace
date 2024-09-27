class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        def dfs(city: int):
            # Mark this city as visited
            visited[city] = True
            # Visit all directly connected cities that haven't been visited
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        province_count = 0

        # Traverse all cities
        for i in range(n):
            if not visited[i]:
                # If a city is not visited, we found a new province
                dfs(i)
                province_count += 1

        return province_count
