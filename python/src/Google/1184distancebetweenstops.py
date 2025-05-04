"""
LeetCode 1184: Distance Between Bus Stops

Problem Statement:
A bus has n stops numbered from 0 to n - 1 that form a circle. The distance between adjacent stops
is given in an array distance where distance[i] is the distance between stops i and (i + 1) % n.
The bus goes along both directions, clockwise and counterclockwise.
Return the shortest distance between the given start and destination stops.

Logic:
1. Normalize start and destination (ensure start < destination)
2. Calculate clockwise distance:
   - Sum of distances from start to destination
3. Calculate counterclockwise distance:
   - Total sum - clockwise distance
4. Return minimum of both distances

Time Complexity: O(n) where n is number of stops
Space Complexity: O(1) constant space
"""


class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start

        clockwise = sum(distance[start:destination])
        counterclockwise = sum(distance) - clockwise

        return min(clockwise, counterclockwise)


def test_distance_between_bus_stops():
    solution = Solution()

    # Test case 1: Basic case
    distance1 = [1, 2, 3, 4]
    result1 = solution.distanceBetweenBusStops(distance1, 0, 1)
    assert result1 == 1, f"Test case 1 failed. Expected 1, got {result1}"
    print(f"Test case 1 passed: shortest distance = {result1}")

    # Test case 2: Reverse direction shorter
    distance2 = [1, 2, 3, 4]
    result2 = solution.distanceBetweenBusStops(distance2, 0, 3)
    assert result2 == 4, f"Test case 2 failed. Expected 4, got {result2}"
    print(f"\nTest case 2 passed: shortest distance = {result2}")

    # Test case 3: Equal distances both ways
    distance3 = [2, 2, 2, 2]
    result3 = solution.distanceBetweenBusStops(distance3, 0, 2)
    assert result3 == 4, f"Test case 3 failed. Expected 4, got {result3}"
    print(f"\nTest case 3 passed: shortest distance = {result3}")

    # Test case 4: Start > Destination
    distance4 = [1, 2, 3, 4]
    result4 = solution.distanceBetweenBusStops(distance4, 3, 0)
    assert result4 == 4, f"Test case 4 failed. Expected 4, got {result4}"
    print(f"\nTest case 4 passed: shortest distance = {result4}")

    print("\nAll test cases passed!")

if __name__ == "__main__":
    test_distance_between_bus_stops()
