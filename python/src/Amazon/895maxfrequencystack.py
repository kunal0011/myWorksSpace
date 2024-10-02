from collections import defaultdict


class FreqStack:
    def __init__(self):
        # Dictionary to keep track of frequency of elements
        self.freq = defaultdict(int)
        # Dictionary to keep track of stacks of elements by frequency
        self.group = defaultdict(list)
        # Variable to track the current maximum frequency
        self.maxFreq = 0

    def push(self, val: int) -> None:
        # Increase the frequency of the value
        self.freq[val] += 1
        f = self.freq[val]

        # If the frequency is the new max frequency, update maxFreq
        if f > self.maxFreq:
            self.maxFreq = f

        # Push the value to the group corresponding to its frequency
        self.group[f].append(val)

    def pop(self) -> int:
        # Get the most frequent element (from the group with maxFreq)
        val = self.group[self.maxFreq].pop()

        # Decrease the frequency of the popped element
        self.freq[val] -= 1

        # If the group for maxFreq is empty, reduce maxFreq
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return val


# Test the Solution
if __name__ == "__main__":
    # Initialize FreqStack object
    freqStack = FreqStack()

    # Test case
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(4)
    freqStack.push(5)

    # Expected pops: [5, 7, 5, 4]
    print(freqStack.pop())  # Output: 5
    print(freqStack.pop())  # Output: 7
    print(freqStack.pop())  # Output: 5
    print(freqStack.pop())  # Output: 4
