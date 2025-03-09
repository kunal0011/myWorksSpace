"""
LeetCode 341: Flatten Nested List Iterator

Problem Statement:
You are given a nested list of integers nestedList. Each element is either an integer or a list 
whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:
- NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
- int next() Returns the next integer in the nested list.
- boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

Example 1:
Input: nestedList = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
the order of elements returned should be: [1,1,2,1,1].

Example 2:
Input: nestedList = [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
the order of elements returned should be: [1,4,6].

Logic:
1. Use DFS to flatten the nested list structure at initialization
2. Store all integers in a queue/list for efficient access
3. For next() operation:
   - Return and remove the first element from the queue
4. For hasNext() operation:
   - Check if queue is not empty
"""

from typing import List

# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for el in nestedList:
            if el.isInteger():
                self.stack.append(el.getInteger())
            else:
                self.flatten(el.getList())

    def next(self) -> int:
        return self.stack.pop(0)

    def hasNext(self) -> bool:
        return bool(self.stack)

def create_nested_list(values):
    """Helper function to create NestedInteger objects for testing."""
    class ConcreteNestedInteger(NestedInteger):
        def __init__(self, value):
            self._value = value
            self._is_integer = not isinstance(value, list)
            if not self._is_integer:
                self._list = [create_nested_list(v) for v in value]

        def isInteger(self) -> bool:
            return self._is_integer
        
        def getInteger(self) -> int:
            return self._value if self._is_integer else None
        
        def getList(self):
            return self._list if not self._is_integer else None

    return ConcreteNestedInteger(values)

def run_test_cases():
    # Test case 1
    print("Test case 1:")
    nested_list1 = [create_nested_list(x) for x in [[1,1],2,[1,1]]]
    iterator1 = NestedIterator(nested_list1)
    result1 = []
    while iterator1.hasNext():
        result1.append(iterator1.next())
    print(f"Input: [[1,1],2,[1,1]]")
    print(f"Expected: [1,1,2,1,1]")
    print(f"Got: {result1}")
    print(f"Pass? {result1 == [1,1,2,1,1]}\n")
    
    # Test case 2
    print("Test case 2:")
    nested_list2 = [create_nested_list(x) for x in [1,[4,[6]]]]
    iterator2 = NestedIterator(nested_list2)
    result2 = []
    while iterator2.hasNext():
        result2.append(iterator2.next())
    print(f"Input: [1,[4,[6]]]")
    print(f"Expected: [1,4,6]")
    print(f"Got: {result2}")
    print(f"Pass? {result2 == [1,4,6]}\n")
    
    # Test case 3 - Empty list
    print("Test case 3:")
    nested_list3 = [create_nested_list(x) for x in []]
    iterator3 = NestedIterator(nested_list3)
    result3 = []
    while iterator3.hasNext():
        result3.append(iterator3.next())
    print(f"Input: []")
    print(f"Expected: []")
    print(f"Got: {result3}")
    print(f"Pass? {result3 == []}\n")
    
    # Test case 4 - Deeply nested list
    print("Test case 4:")
    nested_list4 = [create_nested_list(x) for x in [1,[2,[3,[4]]],[5]]]
    iterator4 = NestedIterator(nested_list4)
    result4 = []
    while iterator4.hasNext():
        result4.append(iterator4.next())
    print(f"Input: [1,[2,[3,[4]]],[5]]")
    print(f"Expected: [1,2,3,4,5]")
    print(f"Got: {result4}")
    print(f"Pass? {result4 == [1,2,3,4,5]}")

if __name__ == "__main__":
    run_test_cases()
