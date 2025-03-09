"""
LeetCode 284 - Peeking Iterator

Problem Statement:
Design an iterator that supports the peek operation on an existing iterator
in addition to the hasNext and next operations.

Implement the PeekingIterator class:
- PeekingIterator(Iterator<int> iter) initializes the object with an existing iterator.
- int next() returns the next element in the iterator. 
- boolean hasNext() returns true if there are still elements in the iterator.
- int peek() returns the next element without advancing the iterator.

Logic:
1. Cache the next element during initialization and after each next() call
2. peek() returns the cached element without advancing
3. next() returns cached element and updates cache with new next element
4. hasNext() checks if cached element exists
"""

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

from typing import Iterator


class PeekingIterator:
    def __init__(self, iterator: 'Iterator'):
        self.iterator = iterator
        self.next_element = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self) -> int:
        return self.next_element

    def next(self) -> int:
        current_element = self.next_element
        self.next_element = self.iterator.next() if self.iterator.hasNext() else None
        return current_element

    def hasNext(self) -> bool:
        return self.next_element is not None


def test_peeking_iterator():
    # Mock Iterator class for testing
    class MockIterator:
        def __init__(self, nums):
            self.nums = nums
            self.index = 0
            
        def hasNext(self):
            return self.index < len(self.nums)
            
        def next(self):
            if self.hasNext():
                result = self.nums[self.index]
                self.index += 1
                return result
    
    # Test cases
    test_cases = [
        [1, 2, 3],           # Multiple elements
        [1],                 # Single element
        []                   # Empty list
    ]
    
    for i, nums in enumerate(test_cases):
        print(f"\nTest case {i + 1}: nums={nums}")
        iter = PeekingIterator(MockIterator(nums))
        
        # Test operations
        while iter.hasNext():
            peek_val = iter.peek()
            next_val = iter.next()
            assert peek_val == next_val, f"Peek/Next mismatch: peek={peek_val}, next={next_val}"
            print(f"Peek={peek_val}, Next={next_val}")

if __name__ == "__main__":
    test_peeking_iterator()
    print("All test cases passed!")
