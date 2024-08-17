# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


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
