"""
LeetCode 789: Escape The Ghosts

Problem Statement:
You are playing a game with n ghosts. You start at position [0, 0] and your destination is [target[0], target[1]].
Each ghost starts at a location [ghosts[i][0], ghosts[i][1]]. In each turn, you and all ghosts move exactly one unit
in any of the 4 cardinal directions: north, east, south, or west. All moves happen simultaneously.
Return true if you can reach the target without any ghost catching you, and false if you cannot.
A ghost catches you if it ends up in the same position as you at any point in time.

Logic:
1. Key insight: If a ghost can reach the target before or at the same time as you, it can catch you
2. Use Manhattan distance to calculate shortest path:
   - For player: |target_x - 0| + |target_y - 0|
   - For each ghost: |target_x - ghost_x| + |target_y - ghost_y|
3. If any ghost's distance <= player's distance, ghost can catch you
4. Time Complexity: O(n) where n is number of ghosts
5. Space Complexity: O(1) as we only use constant extra space

Test cases cover:
- Basic escape scenario
- Ghost interception scenario
- Multiple ghosts
- Target at origin
- Negative coordinates
"""

from typing import List


class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        # Calculate the player's Manhattan distance to the target
        player_distance = abs(target[0] - 0) + abs(target[1] - 0)

        # Check each ghost's distance to the target
        for ghost in ghosts:
            ghost_distance = abs(target[0] - ghost[0]) + \
                abs(target[1] - ghost[1])
            # If any ghost can reach the target before or at the same time as the player, return False
            if ghost_distance <= player_distance:
                return False

        # If no ghost can reach the target before or at the same time as the player, return True
        return True


def test_escape_ghosts():
    solution = Solution()

    # Test case 1: Basic escape possible
    ghosts1 = [[1, 0], [0, 3]]
    target1 = [0, 1]
    result1 = solution.escapeGhosts(ghosts1, target1)
    assert result1 == True, f"Test case 1 failed. Expected True, got {result1}"
    print(
        f"Test case 1 passed: ghosts={ghosts1}, target={target1}, result={result1}")

    # Test case 2: Ghost intercepts
    ghosts2 = [[1, 0]]
    target2 = [2, 0]
    result2 = solution.escapeGhosts(ghosts2, target2)
    assert result2 == False, f"Test case 2 failed. Expected False, got {result2}"
    print(
        f"\nTest case 2 passed: ghosts={ghosts2}, target={target2}, result={result2}")

    # Test case 3: Multiple ghosts, escape possible
    ghosts3 = [[2, 0], [0, 2]]
    target3 = [1, 1]
    result3 = solution.escapeGhosts(ghosts3, target3)
    assert result3 == True, f"Test case 3 failed. Expected True, got {result3}"
    print(
        f"\nTest case 3 passed: ghosts={ghosts3}, target={target3}, result={result3}")

    # Test case 4: Target at origin
    ghosts4 = [[2, 2], [-2, -2]]
    target4 = [0, 0]
    result4 = solution.escapeGhosts(ghosts4, target4)
    assert result4 == False, f"Test case 4 failed. Expected False, got {result4}"
    print(
        f"\nTest case 4 passed: ghosts={ghosts4}, target={target4}, result={result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_escape_ghosts()
