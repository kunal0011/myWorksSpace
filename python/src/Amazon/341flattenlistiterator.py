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
