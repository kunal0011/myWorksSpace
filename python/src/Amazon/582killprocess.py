"""
LeetCode 582 - Kill Process

You have n processes forming a rooted tree structure. You are given two integer arrays pid and ppid, 
where pid[i] is the ID of the ith process and ppid[i] is the ID of its parent process.

Each process has only one parent process but may have multiple children processes. Only one process has ppid[i] = 0, 
which means this process has no parent process (the root of the tree).

When a process is killed, all of its children processes will also be killed.

Given an integer kill, return a list of the IDs of the processes that will be killed. You may return the answer in any order.

Example 1:
Input: pid = [1,3,10,5], ppid = [3,0,5,3], kill = 5
Output: [5,10]
Explanation: The processes colored in red are the processes that will be killed.
  3
/   \
1     5
     /
    10

Example 2:
Input: pid = [1], ppid = [0], kill = 1
Output: [1]

Constraints:
- n == pid.length
- n == ppid.length
- 1 <= n <= 5 * 10^4
- 1 <= pid[i] <= 5 * 10^4
- 0 <= ppid[i] <= 5 * 10^4
- Only one process has ppid[i] = 0
- All the values of pid are unique
- kill is guaranteed to be in pid
"""

from typing import List
from collections import defaultdict, deque


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        Optimized BFS solution
        Time Complexity: O(n) where n is the number of processes
        Space Complexity: O(n) for storing the process tree
        """
        # Build adjacency list representation of the process tree
        children = defaultdict(list)
        for child, parent in zip(pid, ppid):
            children[parent].append(child)
            
        # BFS to find all processes to kill
        result = []
        queue = deque([kill])
        
        while queue:
            process = queue.popleft()
            result.append(process)
            # Add all children of current process to queue
            queue.extend(children[process])
                
        return result
    
    def killProcess_dfs(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        Alternative DFS solution
        Time Complexity: O(n)
        Space Complexity: O(n) for recursion stack and adjacency list
        """
        # Build adjacency list
        children = defaultdict(list)
        for child, parent in zip(pid, ppid):
            children[parent].append(child)
            
        result = []
        
        def dfs(process: int):
            result.append(process)
            for child in children[process]:
                dfs(child)
                
        dfs(kill)
        return result
    
    def killProcess_union_find(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """
        Alternative solution using Union-Find (for learning purposes)
        Not as efficient as BFS/DFS for this problem, but demonstrates another approach
        Time Complexity: O(n * α(n)) where α is the inverse Ackermann function
        Space Complexity: O(n)
        """
        parent = {p: p for p in pid}
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int):
            parent[find(x)] = find(y)
            
        # Build the tree using union-find
        for child, par in zip(pid, ppid):
            if par != 0:
                union(child, par)
                
        # Find all processes in the same group as kill
        return [p for p in pid if find(p) == find(kill)]


def test_kill_process():
    """
    Test function with comprehensive test cases
    """
    solution = Solution()
    
    test_cases = [
        # Basic test cases
        ([1,3,10,5], [3,0,5,3], 5, [5,10]),  # Example 1
        ([1], [0], 1, [1]),                   # Example 2
        
        # More complex test cases
        ([1,2,3], [0,1,1], 1, [1,2,3]),      # Kill root of subtree
        ([1,2,3,4,5], [0,1,1,2,2], 2, [2,4,5]),  # Multiple levels
        
        # Large tree test cases
        ([1,2,3,4,5,6,7,8,9,10], 
         [0,1,1,2,2,3,3,4,4,5], 
         1, 
         [1,2,3,4,5,6,7,8,9,10]),  # Kill root
        
        # Edge cases
        ([1,2], [0,1], 2, [2]),    # Leaf node
        ([1,2,3,4], [0,1,1,2], 3, [3]),  # Node with no children
        
        # Multiple branches
        ([1,2,3,4,5,6], [0,1,1,2,2,3], 2, [2,4,5]),
        ([1,2,3,4,5,6], [0,1,1,2,2,3], 3, [3,6])
    ]
    
    print("Running tests for Kill Process...\n")
    
    for i, (pid, ppid, kill, expected) in enumerate(test_cases, 1):
        # Test all three implementations
        result_bfs = sorted(solution.killProcess(pid, ppid, kill))
        result_dfs = sorted(solution.killProcess_dfs(pid, ppid, kill))
        result_uf = sorted(solution.killProcess_union_find(pid, ppid, kill))
        expected = sorted(expected)
        
        print(f"Test Case {i}:")
        print(f"PIDs: {pid}")
        print(f"Parent PIDs: {ppid}")
        print(f"Kill Process: {kill}")
        print(f"Expected: {expected}")
        print(f"BFS Solution: {result_bfs} {'✅' if result_bfs == expected else '❌'}")
        print(f"DFS Solution: {result_dfs} {'✅' if result_dfs == expected else '❌'}")
        print(f"Union-Find: {result_uf} {'✅' if result_uf == expected else '❌'}")
        
        if (result_bfs != expected or 
            result_dfs != expected or 
            result_uf != expected):
            print("❌ Test case failed!")
            if result_bfs != expected:
                print(f"BFS solution failed. Got: {result_bfs}")
            if result_dfs != expected:
                print(f"DFS solution failed. Got: {result_dfs}")
            if result_uf != expected:
                print(f"Union-Find solution failed. Got: {result_uf}")
        else:
            print("✅ Test case passed!")
        print()


if __name__ == "__main__":
    test_kill_process()
