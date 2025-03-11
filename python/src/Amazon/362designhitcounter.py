"""
LeetCode 362 - Design Hit Counter

Design a hit counter which counts the number of hits received in the past 5 minutes (300 seconds).
Each function accepts a timestamp parameter (in seconds) and you may assume that calls are being made 
to the system in chronological order (timestamps are monotonic).

Time Complexity:
- hit(): O(1)
- getHits(): O(1)
Space Complexity: O(1) - uses fixed size arrays
"""


class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        Using two fixed arrays of size 300:
        - times: stores timestamp
        - hits: stores number of hits at that timestamp
        """
        self.times = [0] * 300  # Array to store timestamps
        self.hits = [0] * 300   # Array to store hit counts
        
    def hit(self, timestamp: int) -> None:
        """
        Record a hit at given timestamp.
        :param timestamp: int
        :return: None
        """
        index = timestamp % 300
        if self.times[index] != timestamp:
            # Reset if it's a new timestamp
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            # Increment hits if it's the same timestamp
            self.hits[index] += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        :param timestamp: int
        :return: int
        """
        total = 0
        for i in range(300):
            # Count hits only if they are within last 300 seconds
            if timestamp - self.times[i] < 300:
                total += self.hits[i]
        return total


def test_hit_counter():
    """
    Comprehensive test cases for HitCounter
    """
    print("Running test cases...")
    hit_counter = HitCounter()

    # Test case 1: Basic hits recording
    hit_counter.hit(1)
    hit_counter.hit(2)
    hit_counter.hit(3)
    assert hit_counter.getHits(4) == 3, "Test case 1 failed: Basic hits recording"

    # Test case 2: Hits at same timestamp
    hit_counter.hit(300)
    hit_counter.hit(300)
    assert hit_counter.getHits(300) == 5, "Test case 2 failed: Hits at same timestamp"

    # Test case 3: Expired hits
    assert hit_counter.getHits(301) == 2, "Test case 3 failed: Expired hits check"

    # Test case 4: Large timestamp gap
    hit_counter.hit(600)
    assert hit_counter.getHits(600) == 1, "Test case 4 failed: Large timestamp gap"

    # Test case 5: Empty window
    assert hit_counter.getHits(901) == 0, "Test case 5 failed: Empty window"

    # Test case 6: Multiple hits at same second
    hit_counter = HitCounter()
    for _ in range(5):
        hit_counter.hit(1)
    assert hit_counter.getHits(1) == 5, "Test case 6 failed: Multiple hits at same second"

    print("All test cases passed successfully!")


if __name__ == "__main__":
    test_hit_counter()
