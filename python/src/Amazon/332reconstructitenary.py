from collections import defaultdict
import heapq
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Graph to store all the flights (from -> list of to airports)
        flights = defaultdict(list)

        # Build the graph, and use a min-heap to keep destinations in lexicographical order
        for frm, to in tickets:
            heapq.heappush(flights[frm], to)

        # List to store the final itinerary
        itinerary = []

        # DFS function
        def dfs(airport):
            # Visit all destinations from this airport in lexicographical order
            while flights[airport]:
                # Get the smallest lexicographical destination
                next_destination = heapq.heappop(flights[airport])
                dfs(next_destination)
            # Once all destinations from this airport are visited, add airport to itinerary
            itinerary.append(airport)

        # Start DFS from "JFK"
        dfs("JFK")

        # The itinerary is built in reverse order, so reverse it before returning
        return itinerary[::-1]
