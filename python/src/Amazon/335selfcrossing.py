from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)

        if n < 4:
            return False  # The path can't cross itself with fewer than 4 moves

        for i in range(3, n):
            # Case 1: Current move crosses the line 3 steps ahead
            if distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]:
                return True

            # Case 2: Current move crosses the line 4 steps ahead
            if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i] + distance[i - 4] >= distance[i - 2]:
                return True

            # Case 3: Current move crosses the line 5 steps ahead
            if i >= 5 and distance[i - 2] >= distance[i - 4] and distance[i] + distance[i - 4] >= distance[i - 2] \
               and distance[i - 1] <= distance[i - 3] and distance[i - 1] + distance[i - 5] >= distance[i - 3]:
                return True

        return False
