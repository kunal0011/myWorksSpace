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


# Example usage:
if __name__ == "__main__":
    snapshotArr = SnapshotArray(3)  # Initialize the array with length 3
    snapshotArr.set(0, 5)  # Set index 0 to value 5
    snap_id = snapshotArr.snap()  # Take a snapshot, return snap_id = 0
    snapshotArr.set(0, 6)  # Set index 0 to value 6
    # Get the value at index 0 from snap_id 0, returns 5
    print(snapshotArr.get(0, snap_id))
