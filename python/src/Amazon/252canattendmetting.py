from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Step 1: Sort the intervals based on their start times
        intervals.sort(key=lambda x: x[0])

        # Step 2: Check for overlaps
        for i in range(1, len(intervals)):
            # If the start time of the current meeting is less than the end time of the previous meeting
            if intervals[i][0] < intervals[i - 1][1]:
                return False  # Overlap found, cannot attend all meetings

        return True  # No overlaps found, can attend all meetings
