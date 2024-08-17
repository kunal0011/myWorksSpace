from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        # Convert the time points to minutes
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(":"))
            total_minutes = h * 60 + m
            minutes.append(total_minutes)

        # Sort the list of minutes
        minutes.sort()

        # Initialize the minimum difference to a large value
        min_diff = float('inf')

        # Compare each pair of consecutive times
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)

        # Compare the first and last time (circular comparison)
        circular_diff = (minutes[0] + 1440) - minutes[-1]
        min_diff = min(min_diff, circular_diff)

        return min_diff
