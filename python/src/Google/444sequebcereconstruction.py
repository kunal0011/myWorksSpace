from collections import defaultdict, deque


class Solution:
    def sequenceReconstruction(self, org, seqs):
        if not seqs:
            return False

        graph = defaultdict(list)
        in_degree = defaultdict(int)
        nodes = set()

        # Build the graph
        for seq in seqs:
            for i in range(len(seq)):
                if seq[i] not in nodes:
                    nodes.add(seq[i])
                if i > 0:
                    graph[seq[i-1]].append(seq[i])
                    in_degree[seq[i]] += 1

        # Check if all elements in org are in nodes
        if len(nodes) != len(org) or set(org) != nodes:
            return False

        # Initialize the queue with nodes of in-degree 0
        queue = deque([node for node in org if in_degree[node] == 0])
        index = 0

        # Topological sort
        while queue:
            if len(queue) > 1:
                return False  # More than one node with in-degree 0 means no unique order
            current = queue.popleft()
            if org[index] != current:
                return False  # The topological order doesn't match the original sequence
            index += 1
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return index == len(org)
