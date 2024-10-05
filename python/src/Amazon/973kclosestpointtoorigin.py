import heapq


class Solution:
    def kClosest(self, points, k):
        # Create a min-heap
        heap = []

        # Push each point into the heap with its negative squared distance
        for x, y in points:
            dist = -(x * x + y * y)  # Use negative to simulate a max-heap
            if len(heap) < k:
                heapq.heappush(heap, (dist, [x, y]))
            else:
                heapq.heappushpop(heap, (dist, [x, y]))

        # Return the points corresponding to the k closest
        return [point for (_, point) in heap]
