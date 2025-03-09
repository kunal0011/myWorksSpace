"""
LeetCode 346: Moving Average from Data Stream

Problem Statement:
Given a stream of integers and a window size, calculate the moving average of all integers 
in the sliding window. Implement the MovingAverage class:
- MovingAverage(int size) Initializes the object with the size of the window size.
- double next(int val) Returns the moving average of the last size values of the stream.

Example 1:
Input:
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output:
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation:
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1);    // return 1.0 = 1 / 1
movingAverage.next(10);   // return 5.5 = (1 + 10) / 2
movingAverage.next(3);    // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5);    // return 6.0 = (10 + 3 + 5) / 3

Logic:
1. Use a queue (deque) to maintain the sliding window:
   - Keep track of the window size
   - Keep a running sum for efficient average calculation
2. For next(val) operation:
   - Add new value to queue and sum
   - If queue size exceeds window size:
     * Remove oldest value from queue
     * Subtract oldest value from sum
   - Return current average (sum / queue size)
"""

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


def run_test_cases():
    # Test case 1: Example from problem statement
    print("Test case 1:")
    movingAverage = MovingAverage(3)
    inputs = [1, 10, 3, 5]
    expected = [1.0, 5.5, 4.66667, 6.0]
    
    for i, val in enumerate(inputs):
        result = movingAverage.next(val)
        print(f"Input: {val}")
        print(f"Expected: {expected[i]:.5f}")
        print(f"Got: {result:.5f}")
        print(f"Pass? {abs(result - expected[i]) < 0.00001}\n")
    
    # Test case 2: Window size 1
    print("Test case 2:")
    movingAverage2 = MovingAverage(1)
    inputs2 = [4, 0, 3, 7]
    expected2 = [4.0, 0.0, 3.0, 7.0]
    
    for i, val in enumerate(inputs2):
        result = movingAverage2.next(val)
        print(f"Input: {val}")
        print(f"Expected: {expected2[i]:.5f}")
        print(f"Got: {result:.5f}")
        print(f"Pass? {abs(result - expected2[i]) < 0.00001}\n")
    
    # Test case 3: Window size 2
    print("Test case 3:")
    movingAverage3 = MovingAverage(2)
    inputs3 = [1, 2, 3, 4]
    expected3 = [1.0, 1.5, 2.5, 3.5]
    
    for i, val in enumerate(inputs3):
        result = movingAverage3.next(val)
        print(f"Input: {val}")
        print(f"Expected: {expected3[i]:.5f}")
        print(f"Got: {result:.5f}")
        print(f"Pass? {abs(result - expected3[i]) < 0.00001}\n")
    
    # Test case 4: Large window size
    print("Test case 4:")
    movingAverage4 = MovingAverage(5)
    inputs4 = [1, 2, 3, 4, 5, 6]
    expected4 = [1.0, 1.5, 2.0, 2.5, 3.0, 4.0]
    
    for i, val in enumerate(inputs4):
        result = movingAverage4.next(val)
        print(f"Input: {val}")
        print(f"Expected: {expected4[i]:.5f}")
        print(f"Got: {result:.5f}")
        print(f"Pass? {abs(result - expected4[i]) < 0.00001}")


if __name__ == "__main__":
    run_test_cases()
