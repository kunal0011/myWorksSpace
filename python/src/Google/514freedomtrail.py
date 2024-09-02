from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Step 1: Preprocessing - Create a map of each character in the ring to its positions
        char_to_indices = defaultdict(list)
        for i, c in enumerate(ring):
            char_to_indices[c].append(i)

        # Step 2: Memoization cache
        memo = {}

        # Step 3: DFS function
        def dfs(ring_index, key_index):
            if key_index == len(key):
                return 0
            if (ring_index, key_index) in memo:
                return memo[(ring_index, key_index)]

            # Current character we need to match in the key
            target_char = key[key_index]
            min_steps = float('inf')

            # Step 4: Try all positions of the target character in the ring
            for i in char_to_indices[target_char]:
                # Calculate the distance in clockwise and counterclockwise
                clockwise_dist = abs(i - ring_index)
                counterclockwise_dist = len(ring) - clockwise_dist
                # Choose the minimum rotation and recurse for the next character
                steps = min(clockwise_dist, counterclockwise_dist) + \
                    1  # +1 for pressing the button
                next_steps = dfs(i, key_index + 1)
                min_steps = min(min_steps, steps + next_steps)

            # Store the result in the memoization table
            memo[(ring_index, key_index)] = min_steps
            return min_steps

        # Step 5: Start DFS from the 12 o'clock position (index 0) and the first character of the key
        return dfs(0, 0)
