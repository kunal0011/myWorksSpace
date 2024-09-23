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
