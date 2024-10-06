from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        # Step 1: Create a graph (adjacency list) and indegree dictionary
        graph = defaultdict(list)
        indegree = {char: 0 for word in words for char in word}

        # Step 2: Build the graph by comparing consecutive words
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))

            # Check if word2 is a prefix of word1
            if len(word1) > len(word2) and word1[:min_length] == word2[:min_length]:
                return ""

            # Compare characters to determine the ordering
            for j in range(min_length):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]] += 1
                    break

        # Step 3: Perform topological sort using BFS (Kahn's Algorithm)
        queue = deque([char for char in indegree if indegree[char] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if we have a valid topological order (no cycles)
        if len(order) == len(indegree):
            return ''.join(order)
        else:
            return ""
