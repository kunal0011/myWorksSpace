"""
LeetCode 281 - Zigzag Iterator

Problem Statement:
Given two 1d vectors, implement an iterator to return their elements alternately.
For example, given two 1d vectors:
v1 = [1, 2]
v2 = [3, 4, 5, 6]
The iterator should return: [1, 3, 2, 4, 5, 6]

Logic:
1. Use a queue to store iterators of both vectors
2. For next():
   - Pop iterator from front of queue
   - Get next value from iterator
   - If iterator has more elements, append it back to queue
3. hasNext() checks if queue is not empty
"""

from typing import List


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.queue = []
        if v1:
            self.queue.append(iter(v1))
        if v2:
            self.queue.append(iter(v2))

    def next(self) -> int:
        if self.hasNext():
            curr_iter = self.queue.pop(0)
            next_val = next(curr_iter)
            if next(curr_iter, None) is not None:
                self.queue.append(curr_iter)
            return next_val

    def hasNext(self) -> bool:
        return len(self.queue) > 0


def test_zigzag_iterator():
    # Test cases
    test_cases = [
        ([1, 2], [3, 4, 5, 6], [1, 3, 2, 4, 5, 6]),      # Different lengths
        ([1], [2, 3], [1, 2, 3]),                         # v1 shorter
        ([1, 2, 3], [4], [1, 4, 2, 3]),                   # v2 shorter
        ([], [1, 2], [1, 2]),                             # v1 empty
        ([1, 2], [], [1, 2]),                             # v2 empty
        ([], [], [])                                       # Both empty
    ]
    
    for i, (v1, v2, expected) in enumerate(test_cases):
        iterator = ZigzagIterator(v1, v2)
        result = []
        while iterator.hasNext():
            result.append(iterator.next())
            
        assert result == expected, f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed: v1={v1}, v2={v2}, result={result}")

if __name__ == "__main__":
    test_zigzag_iterator()
    print("All test cases passed!")
