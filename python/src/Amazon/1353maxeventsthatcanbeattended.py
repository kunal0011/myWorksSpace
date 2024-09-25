import heapq


class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        # Sort events by their start day
        events.sort()

        total_events = 0
        min_heap = []
        day = 0
        i = 0
        n = len(events)

        # Iterate day by day until all events have been processed
        while i < n or min_heap:
            if not min_heap:
                # Move to the next day with an event if no events are in the heap
                day = events[i][0]

            # Add all events that start on the current day to the heap
            while i < n and events[i][0] <= day:
                # Add event's end day to the heap
                heapq.heappush(min_heap, events[i][1])
                i += 1

            # Attend the event that ends the earliest
            heapq.heappop(min_heap)
            total_events += 1
            day += 1  # Move to the next day

            # Remove events from the heap that have already expired
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

        return total_events
