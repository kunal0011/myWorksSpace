"""
LeetCode 1146: Snapshot Array

Problem Statement:
Implement a SnapshotArray that supports the following interface:
- SnapshotArray(int length): Initializes an array of length length
- void set(index, val): Sets the element at the given index to be equal to val
- int snap(): Takes a snapshot of the array and returns the snap_id (starting at 0)
- int get(index, snap_id): Returns the value at the given index in the snapshot with snap_id

Logic:
1. Use dictionary for each index to store only modified values with their snap_id
2. For get operation, find the closest snap_id <= requested snap_id
3. Use binary search (bisect_right) to efficiently find the correct snapshot
4. Optimize space by storing only changed values, not entire array for each snapshot

Time Complexity:
- set(): O(1)
- snap(): O(1)
- get(): O(log s) where s is number of snapshots for that index
Space Complexity: O(n + s) where n is array length and s is total snapshots taken
"""

from collections import defaultdict
from bisect import bisect_right


class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.array = [defaultdict(int) for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.array[index][self.snap_id] = val

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # Get the dictionary of snaps for the given index
        snaps = self.array[index]
        # Get the list of snap_ids in the dictionary and find the right-most one <= snap_id
        keys = sorted(snaps.keys())
        i = bisect_right(keys, snap_id) - 1
        if i >= 0:
            return snaps[keys[i]]
        return 0


def test_snapshot_array():
    # Test case 1: Basic operations
    print("Test case 1: Basic operations")
    arr1 = SnapshotArray(3)
    arr1.set(0, 5)
    snap1 = arr1.snap()
    arr1.set(0, 6)
    result1 = arr1.get(0, snap1)
    assert result1 == 5, f"Test case 1 failed. Expected 5, got {result1}"
    print(f"Value at index 0, snapshot {snap1}: {result1}")

    # Test case 2: Multiple snapshots
    print("\nTest case 2: Multiple snapshots")
    arr2 = SnapshotArray(4)
    arr2.set(1, 10)
    snap2_1 = arr2.snap()
    arr2.set(1, 20)
    snap2_2 = arr2.snap()
    arr2.set(1, 30)
    result2_1 = arr2.get(1, snap2_1)
    result2_2 = arr2.get(1, snap2_2)
    assert result2_1 == 10 and result2_2 == 20, f"Test case 2 failed. Expected 10,20 got {result2_1},{result2_2}"
    print(
        f"Values at index 1: snapshot {snap2_1}: {result2_1}, snapshot {snap2_2}: {result2_2}")

    # Test case 3: Unset values
    print("\nTest case 3: Unset values")
    arr3 = SnapshotArray(2)
    snap3 = arr3.snap()
    result3 = arr3.get(1, snap3)
    assert result3 == 0, f"Test case 3 failed. Expected 0, got {result3}"
    print(f"Unset value at index 1, snapshot {snap3}: {result3}")

    # Test case 4: Multiple sets between snaps
    print("\nTest case 4: Multiple sets between snaps")
    arr4 = SnapshotArray(3)
    arr4.set(0, 1)
    arr4.set(0, 2)
    arr4.set(0, 3)
    snap4 = arr4.snap()
    result4 = arr4.get(0, snap4)
    assert result4 == 3, f"Test case 4 failed. Expected 3, got {result4}"
    print(f"Value after multiple sets at index 0, snapshot {snap4}: {result4}")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_snapshot_array()
