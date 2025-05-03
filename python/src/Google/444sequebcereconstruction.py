"""
LeetCode 444: Sequence Reconstruction

Problem Statement:
You are given an integer array nums of length n where nums is a permutation of integers in the range [1, n].
You are also given a 2D integer array sequences where sequences[i] is a subsequence of nums.

Check if nums is the shortest possible sequence that reconstructs itself through sequences.
Return true if it is, and false otherwise.

A sequence that reconstructs itself is the shortest sequence that has every subsequence 
in sequences as a subsequence.

Constraints:
- 1 <= nums.length <= 10^4
- nums is a permutation of all integers in the range [1, n].
- 1 <= sequences.length <= 10^4
- 1 <= sequences[i].length <= 10^4
- 1 <= sum(sequences[i].length) <= 10^5
- 1 <= sequences[i][j] <= n
- All the arrays of sequences are unique.
- sequences[i] is a subsequence of nums.
"""

from collections import defaultdict, deque


def sequenceReconstruction(nums: list[int], sequences: list[list[int]]) -> bool:
    n = len(nums)
    # Build graph and in-degree count
    graph = defaultdict(set)
    in_degree = defaultdict(int)

    # Add all nodes to in_degree (some might not have edges)
    for num in nums:
        in_degree[num] = 0

    # Build graph from sequences
    for seq in sequences:
        for i in range(len(seq) - 1):
            if seq[i+1] not in graph[seq[i]]:
                graph[seq[i]].add(seq[i+1])
                in_degree[seq[i+1]] += 1

    # Topological sort using BFS
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    order = []

    while queue:
        # If more than one node has 0 in-degree, multiple sequences possible
        if len(queue) > 1:
            return False

        node = queue.popleft()
        order.append(node)

        # Process neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if reconstructed sequence matches nums
    return len(order) == n and order == nums

# Test driver


def run_tests():
    test_cases = [
        {
            "nums": [1, 2, 3],
            "sequences": [[1, 2], [1, 3], [2, 3]],
            "expected": True,
            "explanation": "[1,2,3] is the only sequence that can be reconstructed"
        },
        {
            "nums": [1, 2, 3],
            "sequences": [[1, 2]],
            "expected": False,
            "explanation": "[1,2,3] is not the shortest sequence"
        },
        {
            "nums": [1, 2, 3],
            "sequences": [[1, 2], [1, 3]],
            "expected": False,
            "explanation": "[1,2,3] and [1,3,2] are both possible"
        },
        {
            "nums": [4, 1, 5, 2, 6, 3],
            "sequences": [[5, 2, 6, 3], [4, 1, 5, 2]],
            "expected": True,
            "explanation": "[4,1,5,2,6,3] is the only possible sequence"
        }
    ]

    for i, test in enumerate(test_cases, 1):
        result = sequenceReconstruction(test["nums"], test["sequences"])
        status = "PASSED" if result == test["expected"] else "FAILED"
        print(f"Test {i}: {status}")
        print(f"Original sequence: {test['nums']}")
        print(f"Input sequences: {test['sequences']}")
        print(f"Expected: {test['expected']}")
        print(f"Got: {result}")
        print(f"Explanation: {test['explanation']}\n")


if __name__ == "__main__":
    print("Running test cases for Sequence Reconstruction problem:\n")
    run_tests()

"""
Solution Logic Explanation:

1. Graph Construction:
   - Build a directed graph from the sequences
   - Each number is a node
   - Edges represent order constraints from sequences
   - Track in-degree (number of prerequisites) for each node

2. Key Algorithm (Topological Sort with Uniqueness Check):
   - Use BFS-based topological sort
   - At each step, ensure exactly one node has 0 in-degree
   - Multiple nodes with 0 in-degree means multiple valid sequences
   - Track the order of nodes processed

3. Time and Space Complexity:
   - Time: O(V + E) where V is number of nodes and E is total edges
   - Space: O(V + E) for graph and queue storage

4. Key Conditions for True:
   - Only one valid topological ordering possible
   - The ordering matches the input nums array
   - All nodes are included in the ordering
"""
