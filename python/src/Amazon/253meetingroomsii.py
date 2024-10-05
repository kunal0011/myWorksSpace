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
