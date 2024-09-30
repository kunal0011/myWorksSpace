from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size  # Size of the moving window
        self.queue = deque()  # To store the elements in the window
        self.sum = 0  # Running sum of the elements in the window

    def next(self, val: int) -> float:
        # Add the new value to the queue
        self.queue.append(val)
        self.sum += val

        # If the size of the queue exceeds the window size, pop the oldest value
        if len(self.queue) > self.size:
            removed_val = self.queue.popleft()
            self.sum -= removed_val

        # Return the current moving average
        return self.sum / len(self.queue)
