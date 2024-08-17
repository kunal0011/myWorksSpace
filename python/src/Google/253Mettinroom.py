import heapq


def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Initialize a heap
    free_rooms = []

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Add the first meeting's end time to the heap
    heapq.heappush(free_rooms, intervals[0][1])

    for i in range(1, len(intervals)):
        # If the earliest room is free, reuse it
        if free_rooms[0] <= intervals[i][0]:
            heapq.heappop(free_rooms)

        # Add the current meeting's end time to the heap
        heapq.heappush(free_rooms, intervals[i][1])

    return len(free_rooms)
