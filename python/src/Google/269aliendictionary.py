from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Build the graph
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        unique_chars = set()

        # Initialize graph nodes and in-degree map
        for word in words:
            for char in word:
                unique_chars.add(char)
                if char not in in_degree:
                    in_degree[char] = 0

        # Build the graph
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            found_diff = False

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    found_diff = True
                    break

            # Check for invalid case (e.g., prefix condition)
            if not found_diff and len(w1) > len(w2):
                return ""

        # Step 2: Topological Sort (Kahn's Algorithm)
        queue = deque([char for char in unique_chars if in_degree[char] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Check if the result contains all unique characters
        if len(result) != len(unique_chars):
            return ""

        return "".join(result)
