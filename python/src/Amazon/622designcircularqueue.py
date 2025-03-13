"""
LeetCode 622 - Design Circular Queue

Design your implementation of the circular queue. The circular queue is a linear data structure in which 
the operations are performed based on FIFO (First In First Out) principle, and the last position is 
connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a 
space in front of the queue. But using the circular queue, we can use the space to store new values.

Implementation the MyCircularQueue class:
- MyCircularQueue(k) Initializes the object with the size of the queue to be k.
- int Front() Gets the front item from the queue. If queue is empty, return -1.
- int Rear() Gets the last item from the queue. If queue is empty, return -1.
- boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
- boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
- boolean isEmpty() Checks whether the circular queue is empty or not.
- boolean isFull() Checks whether the circular queue is full or not.

Example 1:
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4

Constraints:
- 1 <= k <= 1000
- 0 <= value <= 1000
- At most 3000 calls will be made to enQueue, deQueue, Front, Rear, isEmpty, and isFull.
"""

class MyCircularQueue:
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.queue = [0] * k
        self.size = 0
        self.front = 0  # Index for dequeue
        self.rear = -1  # Index for enqueue
        
    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
            
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
            
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.size == self.capacity


def test_circular_queue():
    """
    Test function with comprehensive test cases
    """
    def run_test_case(operations, inputs, expected_outputs):
        queue = None
        actual_outputs = []
        
        for i, (operation, input_val) in enumerate(zip(operations, inputs)):
            if operation == "MyCircularQueue":
                queue = MyCircularQueue(input_val[0])
                actual_outputs.append(None)
            elif operation == "enQueue":
                actual_outputs.append(queue.enQueue(input_val[0]))
            elif operation == "deQueue":
                actual_outputs.append(queue.deQueue())
            elif operation == "Front":
                actual_outputs.append(queue.Front())
            elif operation == "Rear":
                actual_outputs.append(queue.Rear())
            elif operation == "isEmpty":
                actual_outputs.append(queue.isEmpty())
            elif operation == "isFull":
                actual_outputs.append(queue.isFull())
                
        return actual_outputs == expected_outputs
    
    # Test cases
    test_cases = [
        # Basic test case from problem statement
        {
            "operations": ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", 
                         "Rear", "isFull", "deQueue", "enQueue", "Rear"],
            "inputs": [[3], [1], [2], [3], [4], [], [], [], [4], []],
            "expected": [None, True, True, True, False, 3, True, True, True, 4]
        },
        # Test empty queue operations
        {
            "operations": ["MyCircularQueue", "isEmpty", "isFull", "Front", "Rear", "deQueue"],
            "inputs": [[5], [], [], [], [], []],
            "expected": [None, True, False, -1, -1, False]
        },
        # Test full queue operations
        {
            "operations": ["MyCircularQueue", "enQueue", "enQueue", "isFull", "deQueue", "enQueue", "Rear"],
            "inputs": [[2], [1], [2], [], [], [3], []],
            "expected": [None, True, True, True, True, True, 3]
        },
        # Test circular behavior
        {
            "operations": ["MyCircularQueue", "enQueue", "enQueue", "deQueue", "enQueue", 
                         "deQueue", "enQueue", "deQueue", "enQueue"],
            "inputs": [[3], [1], [2], [], [3], [], [4], [], [5]],
            "expected": [None, True, True, True, True, True, True, True, True]
        },
        # Edge case with size 1
        {
            "operations": ["MyCircularQueue", "enQueue", "enQueue", "deQueue", "enQueue", "deQueue", "Front"],
            "inputs": [[1], [1], [2], [], [3], [], []],
            "expected": [None, True, False, True, True, True, -1]
        }
    ]
    
    print("Running tests for Circular Queue...\n")
    
    for i, test_case in enumerate(test_cases, 1):
        result = run_test_case(
            test_case["operations"],
            test_case["inputs"],
            test_case["expected"]
        )
        
        print(f"Test Case {i}:")
        print(f"Operations: {test_case['operations']}")
        print(f"Inputs: {test_case['inputs']}")
        print(f"Expected: {test_case['expected']}")
        print("✅ Test case passed!" if result else "❌ Test case failed!")
        print()


if __name__ == "__main__":
    test_circular_queue()