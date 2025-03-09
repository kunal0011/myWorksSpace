"""
LeetCode 332: Reconstruct Itinerary

Problem Statement:
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and arrival airports 
of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are 
multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Example 1:
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Example 2:
Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

Logic:
1. Build a graph using defaultdict and min-heap (priority queue) to ensure lexicographical ordering
2. For each airport, store its destinations in a min-heap
3. Use DFS with backtracking to find the path:
   - Start from JFK
   - For each airport, visit the smallest lexicographical destination first
   - When we reach a dead end (no more destinations), add current airport to result
4. Reverse the final result as we built it backwards
"""

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


def run_test_cases():
    solution = Solution()
    
    # Test case 1
    tickets1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    expected1 = ["JFK","MUC","LHR","SFO","SJC"]
    result1 = solution.findItinerary(tickets1)
    print(f"Test case 1:")
    print(f"Input: {tickets1}")
    print(f"Expected: {expected1}")
    print(f"Got: {result1}")
    print(f"Pass? {result1 == expected1}\n")
    
    # Test case 2
    tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    expected2 = ["JFK","ATL","JFK","SFO","ATL","SFO"]
    result2 = solution.findItinerary(tickets2)
    print(f"Test case 2:")
    print(f"Input: {tickets2}")
    print(f"Expected: {expected2}")
    print(f"Got: {result2}")
    print(f"Pass? {result2 == expected2}\n")
    
    # Test case 3 - More complex case with multiple possible paths
    tickets3 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    expected3 = ["JFK","NRT","JFK","KUL"]
    result3 = solution.findItinerary(tickets3)
    print(f"Test case 3:")
    print(f"Input: {tickets3}")
    print(f"Expected: {expected3}")
    print(f"Got: {result3}")
    print(f"Pass? {result3 == expected3}")


if __name__ == "__main__":
    run_test_cases()
