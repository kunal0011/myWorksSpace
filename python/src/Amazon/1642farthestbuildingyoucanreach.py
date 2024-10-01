import heapq


class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        heap = []

        for i in range(len(heights) - 1):
            # Calculate the difference in height
            diff = heights[i+1] - heights[i]

            # If the next building is taller
            if diff > 0:
                heapq.heappush(heap, diff)  # Push the difference to the heap

            # If the heap size exceeds the number of ladders, we use bricks
            if len(heap) > ladders:
                # Use bricks for the smallest difference in the heap
                bricks -= heapq.heappop(heap)

            # If we run out of bricks, return the index of the current building
            if bricks < 0:
                return i

        # If we manage to go through all the buildings
        return len(heights) - 1

# Test cases


def test_furthestBuilding():
    sol = Solution()

    # Test Case 1: Regular scenario with enough bricks and ladders
    assert sol.furthestBuilding(
        [4, 2, 7, 6, 9, 14, 12], 5, 1) == 4, "Test Case 1 Failed"

    # Test Case 2: Ladders can take care of the largest gaps
    assert sol.furthestBuilding(
        [4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7, "Test Case 2 Failed"

    # Test Case 3: Bricks run out before the end
    assert sol.furthestBuilding(
        [14, 3, 19, 3], 17, 0) == 3, "Test Case 3 Failed"

    # Test Case 4: Can reach the last building with enough resources
    assert sol.furthestBuilding(
        [1, 2, 3, 4, 5, 6, 7, 8, 9], 10, 2) == 8, "Test Case 4 Failed"

    print("All test cases passed!")


# Run the tests
test_furthestBuilding()
