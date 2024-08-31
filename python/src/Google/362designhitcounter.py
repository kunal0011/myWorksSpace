from collections import deque


class HitCounter:

    def __init__(self):
        # A deque to store timestamps of hits
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        # Record a hit at the given timestamp
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # Remove hits that are older than 5 minutes (300 seconds)
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()

        # The number of hits within the last 5 minutes
        return len(self.hits)
