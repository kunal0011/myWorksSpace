"""
LeetCode 174. Dungeon Game

Problem Statement:
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned 
in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health 
point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (negative values), other rooms will heal the knight 
(positive values), and some rooms are empty (0).

Return the knight's minimum initial health so that he can rescue the princess.

Note:
- Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

Example 1:
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: 
RIGHT-> RIGHT -> DOWN -> DOWN.

Constraints:
- m == dungeon.length
- n == dungeon[i].length
- 1 <= m, n <= 200
- -1000 <= dungeon[i][j] <= 1000
"""

from typing import List, Dict, Tuple


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """
        Calculate minimum initial health needed.
        Time complexity: O(m*n)
        Space complexity: O(m*n)
        """
        if not dungeon or not dungeon[0]:
            return 1

        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n-1] = dp[m-1][n] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])

        return dp[0][0]

    def calculateMinimumHPWithSteps(self, dungeon: List[List[int]]) -> Tuple[int, List[dict]]:
        """
        Calculate minimum initial health with step tracking.
        Time complexity: O(m*n)
        Space complexity: O(m*n)
        """
        steps = []

        if not dungeon or not dungeon[0]:
            steps.append({
                "action": "Early return",
                "reason": "Empty dungeon",
                "result": 1
            })
            return 1, steps

        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n-1] = dp[m-1][n] = 1

        steps.append({
            "action": "Initialize",
            "dungeon": [row[:] for row in dungeon],
            "dimensions": (m, n),
            "dp_initial": [row[:] for row in dp]
        })

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                min_next = min(dp[i+1][j], dp[i][j+1])
                needed = max(1, min_next - dungeon[i][j])
                dp[i][j] = needed

                steps.append({
                    "action": "Process cell",
                    "position": (i, j),
                    "cell_value": dungeon[i][j],
                    "min_next_cell": min_next,
                    "health_needed": needed,
                    "dp_state": [row[:] for row in dp]
                })

        steps.append({
            "action": "Final result",
            "minimum_health": dp[0][0],
            "dp_final": [row[:] for row in dp]
        })

        return dp[0][0], steps


def visualize_steps(steps: List[dict]) -> None:
    """Helper function to visualize calculation steps."""
    print("\nCalculation Steps:")
    for i, step in enumerate(steps, 1):
        print(f"\nStep {i}: {step['action']}")

        if step['action'] == "Early return":
            print(f"Reason: {step['reason']}")
            print(f"Result: {step['result']}")

        elif step['action'] == "Initialize":
            print("Dungeon layout:")
            for row in step['dungeon']:
                print(row)
            print(f"Dimensions: {step['dimensions']}")

        elif step['action'] == "Process cell":
            print(f"Processing position: {step['position']}")
            print(f"Cell value: {step['cell_value']}")
            print(f"Minimum next cell: {step['min_next_cell']}")
            print(f"Health needed: {step['health_needed']}")

        elif step['action'] == "Final result":
            print(f"Minimum initial health needed: {step['minimum_health']}")
            print("Final DP state:")
            for row in step['dp_final'][:-1]:  # Skip padding row
                print(row[:-1])  # Skip padding column


def test_calculate_minimum_hp():
    """
    Test function with various test cases.
    """
    test_cases = [
        {
            "dungeon": [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]],
            "expected": 7,
            "description": "Basic case"
        },
        {
            "dungeon": [[0]],
            "expected": 1,
            "description": "Single cell"
        },
        {
            "dungeon": [[-3]],
            "expected": 4,
            "description": "Single negative cell"
        },
        {
            "dungeon": [[1, -3, 3], [0, -2, 0], [-3, -3, -3]],
            "expected": 3,
            "description": "Multiple paths"
        },
        {
            "dungeon": [[-2, -3, -3], [-5, -10, -1], [-6, -13, -5]],
            "expected": 14,
            "description": "All negative values"
        }
    ]

    solution = Solution()

    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*80}")
        print(f"Test Case {i}: {test_case['description']}")
        print("Dungeon:")
        for row in test_case['dungeon']:
            print(row)

        # Test both implementations
        result1 = solution.calculateMinimumHP(test_case['dungeon'])
        result2, steps = solution.calculateMinimumHPWithSteps(
            test_case['dungeon'])

        print(f"\nResults:")
        print(f"Minimum initial health: {result1}")

        visualize_steps(steps)

        assert result1 == test_case['expected'], \
            f"Basic approach failed. Expected {test_case['expected']}, got {result1}"
        assert result2 == test_case['expected'], \
            f"Step tracking failed. Expected {test_case['expected']}, got {result2}"

        print("✓ Test case passed!")

    print("\nAll test cases passed! 🎉")


if __name__ == "__main__":
    test_calculate_minimum_hp()
