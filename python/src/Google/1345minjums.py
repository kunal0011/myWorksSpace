"""
LeetCode 1345: Jump Game IV

Problem Statement:
Given an array of integers arr, you are initially positioned at the first index.
In one step you can jump from index i to:
- index i + 1 where: i + 1 < arr.length
- index i - 1 where: i - 1 >= 0
- index j where: arr[i] == arr[j] and i != j
Return the minimum number of steps to reach the last index of the array.

Logic:
1. Use BFS (Breadth-First Search) to find shortest path
2. Create graph of indices with same values using defaultdict
3. For each position, try all possible jumps:
   - Forward one step
   - Backward one step
   - To all indices with same value
4. Optimize by clearing used indices from graph
5. Return steps when last index is reached

Time Complexity: O(n) where n is length of array
Space Complexity: O(n) for graph and queue
"""

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

def test_min_jumps():
    solution = Solution()
    
    # Test case 1: Basic array
    arr1 = [100,-23,-23,404,100,23,23,23,3,404]
    result1 = solution.minJumps(arr1)
    assert result1 == 3, f"Test case 1 failed. Expected 3, got {result1}"
    print(f"Test case 1 passed: {result1}")
    
    # Test case 2: Single element
    arr2 = [7]
    result2 = solution.minJumps(arr2)
    assert result2 == 0, f"Test case 2 failed. Expected 0, got {result2}"
    print(f"\nTest case 2 passed: {result2}")
    
    # Test case 3: Two elements
    arr3 = [7,6]
    result3 = solution.minJumps(arr3)
    assert result3 == 1, f"Test case 3 failed. Expected 1, got {result3}"
    print(f"\nTest case 3 passed: {result3}")
    
    # Test case 4: All same elements
    arr4 = [7,7,7,7,7]
    result4 = solution.minJumps(arr4)
    assert result4 == 1, f"Test case 4 failed. Expected 1, got {result4}"
    print(f"\nTest case 4 passed: {result4}")
    
    print("\nAll test cases passed!")

if __name__ == "__main__":
    test_min_jumps()
