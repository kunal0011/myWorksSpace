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
