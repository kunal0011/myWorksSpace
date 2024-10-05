from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        # Sort the intervals based on the start times
        intervals.sort(key=lambda x: x[0])

        # Initialize the list of merged intervals with the first interval
        merged = [intervals[0]]

        for current in intervals[1:]:
            # Get the last interval in the merged list
            last = merged[-1]

            # If the current interval overlaps with the last merged interval, merge them
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                # Otherwise, add the current interval to the list of merged intervals
                merged.append(current)

        return merged
