from collections import Counter, deque
from typing import List


class FirstUnique:
    def __init__(self, nums: List[int]):
        # Initialize a counter to keep track of the count of each number
        self.counter = Counter(nums)
        # Initialize a queue to store the unique numbers in order
        self.queue = deque(nums)

    def showFirstUnique(self) -> int:
        # Loop until we find the first unique number or the queue is empty
        while self.queue and self.counter[self.queue[0]] != 1:
            # If the first element in the queue is not unique, remove it
            self.queue.popleft()
        # If the queue is empty return -1, otherwise return the first unique number
        return -1 if not self.queue else self.queue[0]

    def add(self, value: int) -> None:
        # Increment the count of the new value in the counter
        self.counter[value] += 1
        # Add the new value to the queue
        self.queue.append(value)


# Example usage:
if __name__ == "__main__":
    firstUnique = FirstUnique([2, 3, 5])
    print(firstUnique.showFirstUnique())  # Output: 2
    firstUnique.add(5)
    print(firstUnique.showFirstUnique())  # Output: 2
    firstUnique.add(2)
    print(firstUnique.showFirstUnique())  # Output: 3
    firstUnique.add(3)
    print(firstUnique.showFirstUnique())  # Output: -1
