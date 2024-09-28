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

# Example usage:
# solution = Solution()
# costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
# print(solution.minCost(costs))  # Output: 10
