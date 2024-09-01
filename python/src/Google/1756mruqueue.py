class MRUQueue:

    def __init__(self, n: int):
        # Initialize the queue with elements from 1 to n
        self.queue = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        # Get the k-th element (1-indexed)
        value = self.queue[k - 1]
        # Remove the k-th element
        self.queue.pop(k - 1)
        # Append it to the end of the queue
        self.queue.append(value)
        # Return the fetched element
        return value
