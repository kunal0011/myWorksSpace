"""
LeetCode 1756. Design Most Recently Used Queue

Problem Statement:
Design a queue-like data structure that moves the most recently used element to the end of the queue.
Implement the MRUQueue class:
- MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n]
- fetch(int k) moves the kth element (1-indexed) to the end of the queue and returns it.

Time Complexity: 
- Constructor: O(n)
- Fetch: O(n) for array operations
Space Complexity: O(n) for storing n elements
"""

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


# Test driver
if __name__ == "__main__":
    # Test cases
    print("Test Case 1:")
    mru = MRUQueue(8)  # Initialize queue as [1,2,3,4,5,6,7,8]
    print(f"Initial queue: {mru.queue}")
    
    operations = [
        (3, "fetch(3)"),  # returns 3, queue = [1,2,4,5,6,7,8,3]
        (1, "fetch(1)"),  # returns 1, queue = [2,4,5,6,7,8,3,1]
        (2, "fetch(2)"),  # returns 4, queue = [2,5,6,7,8,3,1,4]
        (2, "fetch(2)")   # returns 5, queue = [2,6,7,8,3,1,4,5]
    ]
    
    for k, op in operations:
        result = mru.fetch(k)
        print(f"{op} returned {result}")
        print(f"Queue state: {mru.queue}")
        
    print("\nTest Case 2:")
    mru2 = MRUQueue(3)  # Initialize queue as [1,2,3]
    print(f"Initial queue: {mru2.queue}")
    
    operations2 = [
        (1, "fetch(1)"),  # returns 1, queue = [2,3,1]
        (2, "fetch(2)"),  # returns 3, queue = [2,1,3]
        (2, "fetch(2)")   # returns 1, queue = [2,3,1]
    ]
    
    for k, op in operations2:
        result = mru2.fetch(k)
        print(f"{op} returned {result}")
        print(f"Queue state: {mru2.queue}")
