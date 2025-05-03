"""
LeetCode 362 - Design Hit Counter

Design a hit counter which counts the number of hits received in the past 5 minutes (300 seconds).

Implement the HitCounter class:
- HitCounter() Initializes the hit counter object
- hit(timestamp: int) -> None: Records a hit at the current timestamp
- getHits(timestamp: int) -> int: Returns the number of hits in the past 5 minutes (300 seconds)
  [i.e., the past 300 seconds from the given timestamp]

Note:
- All the calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing)
- Several hits may arrive roughly at the same time
"""

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


def test_hit_counter():
    counter = HitCounter()
    test_cases = [
        ("hit", 1),       # hit at timestamp 1
        ("hit", 2),       # hit at timestamp 2
        ("hit", 3),       # hit at timestamp 3
        ("getHits", 4),   # get hits at timestamp 4, returns 3
        ("hit", 300),     # hit at timestamp 300
        ("getHits", 300), # get hits at timestamp 300, returns 4
        ("getHits", 301), # get hits at timestamp 301, returns 3
        ("getHits", 302), # get hits at timestamp 302, returns 2
        ("getHits", 303), # get hits at timestamp 303, returns 1
        ("getHits", 304), # get hits at timestamp 304, returns 0
    ]

    print("Testing Hit Counter:")
    for operation, timestamp in test_cases:
        if operation == "hit":
            counter.hit(timestamp)
            print(f"hit at timestamp {timestamp}")
        else:
            result = counter.getHits(timestamp)
            print(f"getHits at timestamp {timestamp}: {result}")


if __name__ == "__main__":
    test_hit_counter()
