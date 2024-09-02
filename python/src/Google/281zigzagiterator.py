class ZigzagIterator:
    def __init__(self, v1, v2):
        self.queue = []
        if v1:
            self.queue.append(iter(v1))
        if v2:
            self.queue.append(iter(v2))

    def next(self):
        # Pop the first iterator
        iterator = self.queue.pop(0)
        # Get the next value from the iterator
        val = next(iterator)
        # If there are more elements in the iterator, append it back to the queue
        if next(iterator, None) is not None:
            self.queue.append(iterator)
        return val

    def hasNext(self):
        return len(self.queue) > 0
