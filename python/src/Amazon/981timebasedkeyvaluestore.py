from collections import defaultdict
import bisect


class TimeMap:
    def __init__(self):
        # Dictionary to store key -> list of (timestamp, value) pairs
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append the (timestamp, value) pair to the key's list
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        # Get the list of (timestamp, value) pairs for the key
        values = self.store[key]

        # Use binary search to find the right timestamp
        i = bisect.bisect_right(values, (timestamp, chr(127))) - 1

        # If index is valid, return the corresponding value
        if i >= 0:
            return values[i][1]
        return ""

# Test cases


def test_time_map():
    time_map = TimeMap()

    # Test case 1
    time_map.set("foo", "bar", 1)
    assert time_map.get(
        "foo", 1) == "bar", f"Test case 1 failed: {time_map.get('foo', 1)}"
    assert time_map.get(
        "foo", 3) == "bar", f"Test case 2 failed: {time_map.get('foo', 3)}"

    # Test case 2
    time_map.set("foo", "bar2", 4)
    assert time_map.get(
        "foo", 4) == "bar2", f"Test case 3 failed: {time_map.get('foo', 4)}"
    assert time_map.get(
        "foo", 5) == "bar2", f"Test case 4 failed: {time_map.get('foo', 5)}"

    # Test case 3
    assert time_map.get(
        "foo", 0) == "", f"Test case 5 failed: {time_map.get('foo', 0)}"

    # Test case 4
    time_map.set("test", "alpha", 5)
    assert time_map.get(
        "test", 5) == "alpha", f"Test case 6 failed: {time_map.get('test', 5)}"
    assert time_map.get(
        "test", 6) == "alpha", f"Test case 7 failed: {time_map.get('test', 6)}"

    print("All test cases passed!")


# Run the tests
test_time_map()
