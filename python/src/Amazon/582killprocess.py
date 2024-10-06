from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # Step 1: Build the process tree (adjacency list)
        process_tree = {}

        for i in range(len(pid)):
            if ppid[i] not in process_tree:
                process_tree[ppid[i]] = []
            process_tree[ppid[i]].append(pid[i])

        # Step 2: Perform DFS to collect all processes to be killed
        result = []

        def dfs(process):
            result.append(process)  # Add the current process to the result
            if process in process_tree:
                for child in process_tree[process]:
                    dfs(child)  # Recursively kill child processes

        # Start DFS from the kill process
        dfs(kill)

        return result
