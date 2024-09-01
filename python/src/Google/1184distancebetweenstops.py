class Solution:
    def distanceBetweenBusStops(self, distance: list[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start

        clockwise = sum(distance[start:destination])
        counterclockwise = sum(distance) - clockwise

        return min(clockwise, counterclockwise)
