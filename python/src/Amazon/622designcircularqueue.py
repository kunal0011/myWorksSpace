class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None] * k  # Initialize the queue with a fixed size of k
        self.max_size = k
        self.front = 0  # Points to the front of the queue
        self.rear = -1  # Points to the rear of the queue
        self.size = 0   # To keep track of the number of elements in the queue

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Move the rear pointer in a circular manner
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = None  # Remove the element at the front
        # Move the front pointer in a circular manner
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]  # Return the front element

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]  # Return the rear element

    def isEmpty(self) -> bool:
        return self.size == 0  # The queue is empty if size is 0

    def isFull(self) -> bool:
        return self.size == self.max_size  # The queue is full if size equals max_size
