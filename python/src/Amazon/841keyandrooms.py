class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        def dfs(room):
            # Mark this room as visited
            visited.add(room)
            # Visit all rooms for which we have keys
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        # Initialize a set to keep track of visited rooms
        visited = set()

        # Start DFS from room 0
        dfs(0)

        # Check if we visited all rooms
        return len(visited) == len(rooms)

# Test cases


def test_can_visit_all_rooms():
    sol = Solution()

    # Test case 1: All rooms can be visited
    assert sol.canVisitAllRooms([[1], [2], [3], []]) == True

    # Test case 2: Not all rooms can be visited
    assert sol.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]) == False

    # Test case 3: Only room 0 is accessible
    assert sol.canVisitAllRooms([[1], [], [2], [3]]) == False

    print("All test cases passed!")


# Run the tests
test_can_visit_all_rooms()
