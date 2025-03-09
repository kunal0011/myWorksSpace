"""
LeetCode 256 - Paint House

Problem Statement:
There are n houses in a row. Each house can be painted in red, blue, or green. The cost of 
painting each house in each color is different. You have to paint all the houses such that 
no two adjacent houses have the same color. The cost of painting is represented by an n x 3 
cost matrix where costs[i][0] is the cost of painting house i in red, costs[i][1] in blue, 
and costs[i][2] in green.

Solution Logic:
1. Use Dynamic Programming approach
2. For each house i, calculate minimum cost considering:
   - Cannot use same color as previous house
   - Add minimum of previous house's other two colors
3. Final answer is minimum of last house's three colors
4. Time: O(n), Space: O(1) as we modify input array
"""

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0

        # Iterate over each house starting from the second one (index 1)
        for i in range(1, len(costs)):
            # Update the cost of painting the current house red (0)
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            # Update the cost of painting the current house blue (1)
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            # Update the cost of painting the current house green (2)
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])

        # The final answer will be the minimum of the costs of painting the last house
        return min(costs[-1])

def test_paint_house():
    solution = Solution()
    
    # Test Case 1: Regular case
    costs1 = [[17,2,17],[16,16,5],[14,3,19]]
    print("Test 1: Regular case")
    print(f"Costs matrix: {costs1}")
    print(f"Minimum cost: {solution.minCost(costs1)}")  # Expected: 10
    
    # Test Case 2: Single house
    costs2 = [[7,6,2]]
    print("\nTest 2: Single house")
    print(f"Costs matrix: {costs2}")
    print(f"Minimum cost: {solution.minCost(costs2)}")  # Expected: 2
    
    # Test Case 3: Two houses
    costs3 = [[1,2,3],[1,4,6]]
    print("\nTest 3: Two houses")
    print(f"Costs matrix: {costs3}")
    print(f"Minimum cost: {solution.minCost(costs3)}")  # Expected: 3
    
    # Test Case 4: Empty case
    costs4 = []
    print("\nTest 4: No houses")
    print(f"Costs matrix: {costs4}")
    print(f"Minimum cost: {solution.minCost(costs4)}")  # Expected: 0

if __name__ == "__main__":
    test_paint_house()
