from collections import deque


class HitCounter:
    def __init__(self):
        # Queue to store (timestamp, hit_count) tuples
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        # If the queue is not empty and the latest timestamp is the same, just increment the count
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1] = (timestamp, self.hits[-1][1] + 1)
        else:
            # Otherwise, push a new entry for the timestamp with 1 hit
            self.hits.append((timestamp, 1))

    def getHits(self, timestamp: int) -> int:
        # Remove hits that are older than 300 seconds
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.hits.popleft()

        # Sum up the remaining hit counts
        return sum(hit[1] for hit in self.hits)

# Test cases


def test_hit_counter():
    hit_counter = HitCounter()

    # Test case 1: Record hits at timestamps 1, 2, and 3
    hit_counter.hit(1)
    hit_counter.hit(2)
    hit_counter.hit(3)
    assert hit_counter.getHits(
        4) == 3, f"Test case 1 failed: {hit_counter.getHits(4)}"

    # Test case 2: More hits within 5 minutes
    hit_counter.hit(300)
    assert hit_counter.getHits(
        300) == 4, f"Test case 2 failed: {hit_counter.getHits(300)}"
    assert hit_counter.getHits(
        301) == 3, f"Test case 3 failed: {hit_counter.getHits(301)}"

    # Test case 3: Hit at the same timestamp
    hit_counter.hit(301)
    hit_counter.hit(301)
    assert hit_counter.getHits(
        301) == 5, f"Test case 4 failed: {hit_counter.getHits(301)}"

    # Test case 4: Hits fall outside the window
    hit_counter.hit(600)
    assert hit_counter.getHits(
        600) == 4, f"Test case 5 failed: {hit_counter.getHits(600)}"

    print("All test cases passed!")


# Run the tests
test_hit_counter()
