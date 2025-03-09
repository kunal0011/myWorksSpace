"""
LeetCode 252 - Meeting Rooms

Problem Statement:
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings (i.e., there are no overlapping meetings).

Solution Logic:
1. Sort intervals by start time
2. Check for overlapping meetings:
   - Current meeting starts before previous meeting ends = overlap
   - No overlaps = can attend all meetings
3. Time: O(n log n) for sorting, Space: O(1)
"""

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


def test_can_attend_meetings():
    solution = Solution()
    
    # Test Case 1: No overlap
    intervals1 = [[0,30],[45,50],[51,60]]
    print("Test 1: No overlapping meetings")
    print(f"Intervals: {intervals1}")
    print(f"Can attend all meetings: {solution.canAttendMeetings(intervals1)}")  # Expected: True
    
    # Test Case 2: With overlap
    intervals2 = [[0,30],[5,10],[15,20]]
    print("\nTest 2: Overlapping meetings")
    print(f"Intervals: {intervals2}")
    print(f"Can attend all meetings: {solution.canAttendMeetings(intervals2)}")  # Expected: False
    
    # Test Case 3: Single meeting
    intervals3 = [[7,10]]
    print("\nTest 3: Single meeting")
    print(f"Intervals: {intervals3}")
    print(f"Can attend all meetings: {solution.canAttendMeetings(intervals3)}")  # Expected: True
    
    # Test Case 4: Back-to-back meetings
    intervals4 = [[1,5],[5,10]]
    print("\nTest 4: Back-to-back meetings")
    print(f"Intervals: {intervals4}")
    print(f"Can attend all meetings: {solution.canAttendMeetings(intervals4)}")  # Expected: True

if __name__ == "__main__":
    test_can_attend_meetings()
