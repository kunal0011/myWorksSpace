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
