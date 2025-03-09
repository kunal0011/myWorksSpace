"""
LeetCode 339: Nested List Weight Sum

Problem Statement:
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements 
may also be integers or other lists. The depth of an integer is the number of lists that it is inside of.
For example, the nested list [1,[2,2],[[3],2],1] has each integer's value for its depth:
- 1 is at depth 1 because it's not inside any lists
- 2,2 are at depth 2 because they're inside one list
- 3 is at depth 3 because it's inside two lists
- 2 is at depth 2 because it's inside one list
Return the sum of each integer in nestedList multiplied by its depth.

Example 1:
Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1*1 + 4*2 + 6*3 = 27

Example 2:
Input: nestedList = [1,[4,[[6]]]]
Output: 44
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 4; 1*1 + 4*2 + 6*4 = 44

Logic:
1. Use DFS (Depth-First Search) to traverse the nested structure
2. Keep track of the current depth as we traverse deeper into nested lists
3. For each element:
   - If it's an integer, multiply it by its depth and add to total
   - If it's a list, recursively process it with depth + 1
4. Return the total sum of all depth-weighted integers
"""

from typing import List, Union

# This class definition is given in the problem for representing the nested list structure
class NestedInteger:
    def isInteger(self) -> bool:
        """Return True if this NestedInteger holds a single integer, rather than a nested list."""
        pass
    
    def getInteger(self) -> Union[int, None]:
        """Return the single integer that this NestedInteger holds, if it holds a single integer.
        Return None if this NestedInteger holds a nested list."""
        pass
    
    def getList(self) -> Union[List['NestedInteger'], None]:
        """Return the nested list that this NestedInteger holds, if it holds a nested list.
        Return None if this NestedInteger holds a single integer."""
        pass

class Solution:
    def depthSum(self, nestedList: List[NestedInteger], depth: int = 1) -> int:
        total = 0
        for ni in nestedList:
            if ni.isInteger():
                # Multiply the integer by its depth
                total += ni.getInteger() * depth
            else:
                # Recursively calculate the sum for the nested list, increasing the depth
                total += self.depthSum(ni.getList(), depth + 1)
        return total

def create_nested_integer(value):
    """Helper function to create NestedInteger objects for testing."""
    class ConcreteNestedInteger(NestedInteger):
        def __init__(self, value):
            self._value = value
            self._is_integer = not isinstance(value, list)
            if not self._is_integer:
                self._list = [create_nested_integer(v) for v in value]

        def isInteger(self) -> bool:
            return self._is_integer
        
        def getInteger(self) -> Union[int, None]:
            return self._value if self._is_integer else None
        
        def getList(self) -> Union[List['NestedInteger'], None]:
            return self._list if not self._is_integer else None

    return ConcreteNestedInteger(value)

def run_test_cases():
    solution = Solution()
    
    # Test case 1: Example from problem statement
    test1 = [create_nested_integer(x) for x in [1,[4,[6]]]]
    result1 = solution.depthSum(test1)
    print("Test case 1:")
    print("Input: [1,[4,[6]]]")
    print(f"Expected: 27")
    print(f"Got: {result1}")
    print(f"Pass? {result1 == 27}\n")
    
    # Test case 2: More complex nesting
    test2 = [create_nested_integer(x) for x in [1,[4,[[6]]]]]
    result2 = solution.depthSum(test2)
    print("Test case 2:")
    print("Input: [1,[4,[[6]]]]")
    print(f"Expected: 44")
    print(f"Got: {result2}")
    print(f"Pass? {result2 == 44}\n")
    
    # Test case 3: All integers at same depth
    test3 = [create_nested_integer(x) for x in [1,2,3,4,5]]
    result3 = solution.depthSum(test3)
    print("Test case 3:")
    print("Input: [1,2,3,4,5]")
    print(f"Expected: 15")
    print(f"Got: {result3}")
    print(f"Pass? {result3 == 15}\n")
    
    # Test case 4: Empty nested lists
    test4 = [create_nested_integer(x) for x in [[]]]
    result4 = solution.depthSum(test4)
    print("Test case 4:")
    print("Input: [[]]")
    print(f"Expected: 0")
    print(f"Got: {result4}")
    print(f"Pass? {result4 == 0}")


if __name__ == "__main__":
    run_test_cases()
