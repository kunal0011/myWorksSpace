from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)

        for i in range(3, n):
            # First type: current line crosses the line 3 steps ahead of it
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True

            # Second type: current line crosses the line 4 steps ahead of it
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                return True

            # Third type: current line crosses the line 5 steps ahead of it
            if i >= 5 and distance[i-2] >= distance[i-4] and distance[i] + distance[i-4] >= distance[i-2] and distance[i-1] <= distance[i-3] and distance[i-1] + distance[i-5] >= distance[i-3]:
                return True

        return False
