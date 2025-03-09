"""
LeetCode 253 - Meeting Rooms II

Problem Statement:
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

Solution Logic:
1. Separate start and end times into sorted arrays
2. Use two pointers approach:
   - When meeting starts before earliest end -> need new room
   - When meeting ends -> free up a room
3. Track maximum rooms needed at any point
4. Time: O(n log n) for sorting, Space: O(n)
"""

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        # Separate the start and end times
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])

        # Use two pointers to track start and end times
        start_pointer, end_pointer = 0, 0
        rooms_needed = 0
        max_rooms = 0

        # Iterate through all the meetings
        while start_pointer < len(starts):
            # If a meeting starts before the earliest meeting ends, we need a new room
            if starts[start_pointer] < ends[end_pointer]:
                rooms_needed += 1
                start_pointer += 1
            else:
                # If the meeting ends, we free a room
                rooms_needed -= 1
                end_pointer += 1

            # Keep track of the maximum number of rooms required
            max_rooms = max(max_rooms, rooms_needed)

        return max_rooms

def test_meeting_rooms():
    solution = Solution()
    
    # Test Case 1: Multiple overlapping meetings
    intervals1 = [[0,30],[5,10],[15,20]]
    print("Test 1: Overlapping meetings")
    print(f"Intervals: {intervals1}")
    print(f"Minimum rooms needed: {solution.minMeetingRooms(intervals1)}")  # Expected: 2
    
    # Test Case 2: No overlap
    intervals2 = [[7,10],[2,4]]
    print("\nTest 2: Non-overlapping meetings")
    print(f"Intervals: {intervals2}")
    print(f"Minimum rooms needed: {solution.minMeetingRooms(intervals2)}")  # Expected: 1
    
    # Test Case 3: Complex overlaps
    intervals3 = [[1,4],[4,5],[2,3],[3,6]]
    print("\nTest 3: Complex overlapping pattern")
    print(f"Intervals: {intervals3}")
    print(f"Minimum rooms needed: {solution.minMeetingRooms(intervals3)}")  # Expected: 2
    
    # Test Case 4: Empty case
    intervals4 = []
    print("\nTest 4: No meetings")
    print(f"Intervals: {intervals4}")
    print(f"Minimum rooms needed: {solution.minMeetingRooms(intervals4)}")  # Expected: 0

if __name__ == "__main__":
    test_meeting_rooms()
