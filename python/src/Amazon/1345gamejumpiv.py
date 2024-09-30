from collections import deque, defaultdict


class Solution:
    def minJumps(self, arr):
        if len(arr) == 1:
            return 0

        # Dictionary to keep track of indices with the same value
        graph = defaultdict(list)
        for i, value in enumerate(arr):
            graph[value].append(i)

        # BFS initialization
        queue = deque([0])  # Start BFS from index 0
        visited = {0}  # Mark index 0 as visited
        steps = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                index = queue.popleft()

                # Check if we've reached the last index
                if index == len(arr) - 1:
                    return steps

                # Get all possible jumps (neighbors)
                neighbors = graph[arr[index]] + [index - 1, index + 1]

                # Clear the list of the current value to avoid redundant checks
                graph[arr[index]] = []

                for neighbor in neighbors:
                    if 0 <= neighbor < len(arr) and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            steps += 1

        return -1  # If we somehow don't find the last index (shouldn't happen)
