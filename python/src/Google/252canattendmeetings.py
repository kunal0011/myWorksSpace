from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x[0])

        # Check for overlap
        for i in range(1, len(intervals)):
            # If the start time of the current interval is less than the end time of the previous interval
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True
